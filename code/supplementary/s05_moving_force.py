"""s05_moving_force.py - constant force crossing the laboratory two-span beam (Section 6.5).

Model (as described in Section 6.5 of the SCHM manuscript):
  * Euler-Bernoulli two-span beam, spans l = 2.5 m, EI = 3305.95 N m^2 (Section 3.1),
    Hermite cubic elements, consistent mass, m = rho A = 7850 x 186.5e-6 = 1.464 kg/m;
  * Rayleigh damping, 2 % at the first and third modes;
  * a constant force P enters at x = 0 at t = 0 and leaves at x = 2l at t = T_cr = 2l/v;
    it is applied through the Hermite shape functions of the element it is on;
  * Newmark average acceleration (gamma = 1/2, beta = 1/4), zero initial conditions;
  * the mid-span deflection of span 1 is integrated over the crossing window,
    I_y = v * integral y dt, and compared with the quasi-static value
    C_m P = P l^4/(192 EI):  E_dyn = I_y/(C_m P) - 1.
  * sweep: 47 speeds, T_cr/T_1 = 2 l f_1 / v log-spaced from 0.6 to 120.

Not stated in the manuscript and therefore chosen here: 40 elements per span
(mesh check below), 4000 time steps per crossing (time-step check below),
logarithmic spacing of the 47 speeds, P = 1 N (the problem is linear).

Reproduces / checks: f_1 = 11.942 Hz (FE and analytical), 1000 -> 16 000 steps
(0.002 percentage points), Table 9 envelope, Eq. (21), the 2.5 / 15 % statement,
39 % exit deflection at T_cr/T_1 = 1.5, window extension by 4 T_1, damping
0.5-5 %, multi-axle spread 0.33 % at 11.9 and 1.95 % at 3.0.

Run:  python3 -I code/supplementary/s05_moving_force.py     (about 1-2 min)
"""
import os
import sys
import time

import numpy as np
from scipy.linalg import lu_factor, lu_solve

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import beam_theory as bt  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))

# ----------------------------------------------------------------- SI constants
L = bt.L_SPAN / 1000.0                       # 2.5 m
EI = bt.EI * 1e-6                            # N m^2 (N mm^2 -> N m^2)
A_MS = 186.5e-6                              # m^2, as printed in Section 6.5
MASS = 7850.0 * A_MS                         # 1.464 kg/m
CM = L ** 4 / (192.0 * EI)                   # m^2/N
NE = 40                                      # elements per span (chosen; see mesh check)
NSTEP = 4000                                 # steps per crossing (chosen; see dt check)
ZETA = 0.02


def head(t):
    print(("\n== %s " % t).ljust(78, "="))


class MovingForceModel:
    def __init__(self, ne=NE, zeta=ZETA, mass=MASS, modes=(1, 3)):
        self.b = bt.Beam([L, L], ne=ne, ei=EI, m=mass, extra=[L / 2])
        b = self.b
        f, _ = b.eig(6)
        self.f = f
        w1, w3 = 2 * np.pi * f[modes[0] - 1], 2 * np.pi * f[modes[1] - 1]
        self.alpha = 2 * zeta * w1 * w3 / (w1 + w3)
        self.beta = 2 * zeta / (w1 + w3)
        self.K, self.M = b.Kf, b.Mf
        self.C = self.alpha * self.M + self.beta * self.K
        self.free_index = -np.ones(b.ndof, dtype=int)
        self.free_index[b.free] = np.arange(len(b.free))
        self.imid = self.free_index[2 * b.node(L / 2)]

    def load(self, xp, P):
        """Consistent load vector (free DOFs) of a point load P at xp."""
        F = np.zeros(len(self.b.free))
        if xp <= 0.0 or xp >= 2 * L:
            return F
        x = self.b.x
        e = min(int(np.searchsorted(x, xp, side="right")) - 1, self.b.ne - 1)
        Le = x[e + 1] - x[e]
        Nn = P * bt.hermite(xp - x[e], Le)
        for k in range(4):
            j = self.free_index[2 * e + k]
            if j >= 0:
                F[j] += Nn[k]
        return F

    def run(self, v, axles=((0.0, 1.0),), nstep=NSTEP, t_extra=0.0):
        """Newmark average acceleration. axles = ((offset behind leader, P), ...).
        Window: entry of the leading axle to exit of the trailing one (+ t_extra).
        Returns t, y_mid (downward positive), T_window."""
        amax = max(a for a, _ in axles)
        Tw = (2 * L + amax) / v
        dt = Tw / nstep
        n_ex = int(round(t_extra / dt))
        gam, bet = 0.5, 0.25
        a0, a1, a2 = 1 / (bet * dt ** 2), gam / (bet * dt), 1 / (bet * dt)
        a3, a4, a5 = 1 / (2 * bet) - 1, gam / bet - 1, dt / 2 * (gam / bet - 2)
        lu = lu_factor(self.K + a1 * self.C + a0 * self.M)
        n = len(self.b.free)
        u, vel, acc = np.zeros(n), np.zeros(n), np.zeros(n)
        nt = nstep + n_ex
        y = np.zeros(nt + 1)
        for i in range(1, nt + 1):
            t = i * dt
            F = np.zeros(n)
            for a, P in axles:
                F += self.load(v * t - a, P)
            rhs = F + self.M @ (a0 * u + a2 * vel + a3 * acc) + self.C @ (a1 * u + a4 * vel + a5 * acc)
            un = lu_solve(lu, rhs)
            an = a0 * (un - u) - a2 * vel - a3 * acc
            vel = vel + dt * ((1 - gam) * acc + gam * an)
            u, acc = un, an
            y[i] = u[self.imid]
        return np.arange(nt + 1) * dt, y, Tw

    def error(self, ratio, **kw):
        """E_dyn (%) for T_cr/T_1 = ratio; T_cr = 2l/v, T_1 = 1/f_1."""
        v = 2 * L * self.f[0] / ratio
        t, y, Tw = self.run(v, **kw)
        P = sum(p for _, p in kw.get("axles", ((0.0, 1.0),)))
        I = v * np.trapezoid(y, t)
        return 100 * (I / (CM * P) - 1), t, y, v


def envelope(ratios, errs, thresholds=(2, 3, 4, 6, 8, 10, 15, 20)):
    return [np.max(np.abs(np.asarray(errs)[np.asarray(ratios) >= T - 1e-12])) for T in thresholds]


t0 = time.time()
head("Model and fundamental frequency")
mdl = MovingForceModel()
f1_an = (np.pi / L) ** 2 * np.sqrt(EI / MASS) / (2 * np.pi)
print("  EI = %.2f N m^2, m = %.4f kg/m (1.464), C_m = %.6e m^2/N" % (EI, MASS, CM))
print("  FE frequencies (Hz): " + ", ".join("%.3f" % v for v in mdl.f[:4]))
print("  f1 FE = %.4f Hz, analytical (pi/l)^2 sqrt(EI/m)/2pi = %.4f Hz  (manuscript: 11.942)"
      % (mdl.f[0], f1_an))
print("  Rayleigh: alpha = %.4f 1/s, beta = %.4e s (2 %% at modes 1 and 3)" % (mdl.alpha, mdl.beta))
print("  check: unit static load at l/2 -> mid deflection %.6e m; Eq. (A.2) %.6e m"
      % (mdl.b.solve(mdl.b.point_load(L / 2))[2 * mdl.b.node(L / 2)], bt.eta(L / 2, 1.0, L, EI)))
for ne in (10, 20, 80):
    print("  mesh %2d el/span: f1 = %.4f Hz" % (ne, MovingForceModel(ne=ne).f[0]))

head("Quasi-static limit")
for r in (240.0, 480.0):
    e, *_ = mdl.error(r, nstep=8000)
    print("  T_cr/T1 = %5.0f: E = %+.4f %%" % (r, e))

head("Time-step convergence (manuscript: 1000 -> 16 000 steps changes E by 0.002 pp)")
print("  %8s " % "Tcr/T1" + " ".join("%10d" % n for n in (1000, 2000, 4000, 8000, 16000)) + "   max-min (pp)")
for r in (1.5, 3.0, 8.0, 30.0, 120.0):
    es = [mdl.error(r, nstep=n)[0] for n in (1000, 2000, 4000, 8000, 16000)]
    print("  %8.1f " % r + " ".join("%+10.4f" % e for e in es) + "   %.4f" % (max(es) - min(es)))

head("Mesh convergence (4000 steps)")
for r in (3.0, 8.0):
    es = [MovingForceModel(ne=ne).error(r)[0] for ne in (10, 20, 40, 80)]
    print("  Tcr/T1 = %4.1f: ne/span 10, 20, 40, 80 -> " % r + ", ".join("%+.4f" % e for e in es))

head("Sweep: 47 speeds, T_cr/T_1 log-spaced 0.6 ... 120 (Fig. 10)")
ratios = np.logspace(np.log10(0.6), np.log10(120.0), 47)
errs = []
rows = []
for r in ratios:
    e, t, y, v = mdl.error(r)
    errs.append(e)
    rows.append((r, v, e, y[-1]))
    print("  Tcr/T1 = %8.3f  v = %8.3f m/s  E_dyn = %+9.4f %%" % (r, v, e))
errs = np.array(errs)
os.makedirs(os.path.join(HERE, "logs"), exist_ok=True)
np.savetxt(os.path.join(HERE, "logs", "s05_sweep47.csv"), np.array(rows), delimiter=",",
           header="Tcr_over_T1,v_m_per_s,E_dyn_percent,y_mid_at_exit_m_per_N", comments="")

TH = (2, 3, 4, 6, 8, 10, 15, 20)
MS = (17.6, 8.6, 3.8, 1.7, 1.00, 0.32, 0.15, 0.08)
head("Table 9: envelope max |E_dyn| over T_cr/T_1 >= threshold")
env47 = envelope(ratios, errs, TH)
print("  threshold      " + " ".join("%7g" % v for v in TH))
print("  this, 47 pts   " + " ".join("%7.2f" % v for v in env47))
print("  manuscript     " + " ".join("%7.2f" % v for v in MS))

head("Dense sweep (300 speeds, 2000 steps) - envelope independent of the speed sampling")
rd = np.logspace(np.log10(0.6), np.log10(120.0), 300)
ed = np.array([mdl.error(r, nstep=2000)[0] for r in rd])
envd = envelope(rd, ed, TH)
print("  threshold      " + " ".join("%7g" % v for v in TH))
print("  dense          " + " ".join("%7.2f" % v for v in envd))
np.savetxt(os.path.join(HERE, "logs", "s05_sweep_dense.csv"), np.c_[rd, ed], delimiter=",",
           header="Tcr_over_T1,E_dyn_percent", comments="")
lo = rd[np.abs(ed) > 15]
print("  largest T_cr/T_1 with |E| > 15 %%: %.2f  (manuscript: error exceeds 15 %% below ~2.5)"
      % (lo.max() if lo.size else float("nan")))
sc = rd[1:][np.sign(ed[1:]) != np.sign(ed[:-1])]
print("  sign changes of E at T_cr/T_1 = " + ", ".join("%.2f" % v for v in sc[:12])
      + (" ..." if len(sc) > 12 else ""))
print("  Eq. (21): max|E| for >= 8: %.2f %% (<~1 %%); for >= 4: %.2f %% (< 4 %%)"
      % (envd[TH.index(8)], envd[TH.index(4)]))

head("Truncation mechanism (T_cr/T_1 = 1.5)")
e, t, y, v = mdl.error(1.5)
peak = bt.eta(np.linspace(0, 2 * L, 20001), 1.0, L, EI).max()
print("  E = %+.2f %%; y_mid at exit / static peak = %.1f %%  (manuscript: 39 %%)" % (e, 100 * y[-1] / peak))
for r in (1.5, 3.0, 8.0):
    vv = 2 * L * mdl.f[0] / r
    t1, y1, Tw = mdl.run(vv)
    t2, y2, _ = mdl.run(vv, t_extra=4.0 / mdl.f[0])
    e1 = 100 * (vv * np.trapezoid(y1, t1) / CM - 1)
    e2 = 100 * (vv * np.trapezoid(y2, t2) / CM - 1)
    print("  T_cr/T1 = %4.1f: window to exit E = %+7.3f %%; extended by 4 T1 E = %+7.3f %% (ratio %.2f)"
          % (r, e1, e2, e2 / e1 if e1 else np.nan))
print("  (manuscript: extending the window by four fundamental periods roughly halves the error)")

head("Damping (manuscript: 0.5-5 % changes E monotonically; less damping, less error)")
for r in (3.0, 5.0, 8.0):
    es = [MovingForceModel(zeta=z).error(r)[0] for z in (0.005, 0.01, 0.02, 0.03, 0.05)]
    mono = np.all(np.diff(np.abs(es)) > 0) or np.all(np.diff(np.abs(es)) < 0)
    print("  Tcr/T1 = %3.0f: zeta 0.5,1,2,3,5 %% -> " % r + ", ".join("%+.3f" % e for e in es)
          + "   |E| monotonic: %s, increasing with zeta: %s" % (mono, bool(np.all(np.diff(np.abs(es)) > 0))))

head("Multi-axle invariance under dynamics (fixed total load 1 N)")
print("  speeds 5 m/s (T_cr/T1 = %.2f) and 20 m/s (%.2f); equal axle loads;" %
      (2 * L * mdl.f[0] / 5, 2 * L * mdl.f[0] / 20))
print("  window from entry of the first to exit of the last axle; ratio uses T_cr = 2l/v")
configs = [((0.0, 1.0),)]
for s_ in (0.5, 1.0, 1.5):
    configs.append(((0.0, 0.5), (s_, 0.5)))
    configs.append(((0.0, 1 / 3), (s_, 1 / 3), (2 * s_, 1 / 3)))
for vv in (5.0, 20.0):
    Is = []
    for ax in configs:
        t, y, Tw = mdl.run(vv, axles=ax, nstep=int(NSTEP * (1 + max(a for a, _ in ax) / (2 * L))))
        Is.append(vv * np.trapezoid(y, t))
    Is = np.array(Is)
    print("  v = %4.1f m/s: I/(C_m P) - 1 per config (%%): " % vv
          + " ".join("%+.2f" % (100 * (i / CM - 1)) for i in Is))
    print("     spread (max-min)/mean = %.2f %%   (manuscript: 0.33 %% at 11.9, 1.95 %% at 3.0)"
          % (100 * (Is.max() - Is.min()) / Is.mean()))
print("  configs: 1 axle; then (2 axles, 3 axles) at spacings 0.5, 1.0, 1.5 m")

print("\n  run time %.0f s" % (time.time() - t0))
