"""Package 1C, part 4 - local Fisher information / Cramer-Rao analysis of
theta = (ln alpha, ln kappa, ln gamma'),  gamma' = gamma/e_d (mass scale over
dynamic-modulus factor; enters only the frequencies).

Observation models (log space, relative errors):
  static gauge j : ln y_j = -ln alpha + ln yhat_j(kappa)            row [-1, S_j, 0]
  frequency i    : ln f_i = 0.5 ln alpha - 0.5 ln gamma' + ln fhat_i(kappa)  row [0.5, Sf_i, -0.5]
  rotation r     : ln th_r = -ln alpha + ln thhat_r(kappa)          row [-1, Sr, 0]
FIM = J^T W J + prior.  For (a) the 2x2 static FIM has det = (S_8 - S_7)^2/(s8^2 s7^2):
singular where the ratio y8/y7 is stationary in kappa (= best-fit calibration B).
Run after ident_static.py and ident_freq.py.
"""
import os
import numpy as np
from ident_core import (Model, EI_law, mass_fn, X_N8, X_N7, X_N8MID, Logger, LOGD,
                        static_pred, schemes, MEAS_MEAN, norm_index)
from ident_static import KAPPA, K_FE

SIG_STATIC = None          # taken from ident_static (total per-gauge sigma = tau_rec/2)
SIG_F = 0.033              # sd of N6/N7/N8 measured frequencies (ident_freq.log)
SIG_ROT = 0.03             # assumed tiltmeter accuracy, 3 % of a ~1e-4 rad reading


def responses(m, k, sch):
    out = {}
    for key, xm, sc in (("y8", X_N8, "CM_III_N8"), ("y7", X_N7, "CM_IV_N7")):
        u = m.full(m.solve(m.axle_load(sch[sc]["x"], sch[sc]["P"]), k))
        out[key] = m.defl_at(u, xm)
        if sc == "CM_III_N8":
            out["rotT8"] = abs(u[2 * m.node[3] + 1])
            out["rotT7"] = abs(u[2 * m.node[2] + 1])
        else:
            out["rotT7_IV"] = abs(u[2 * m.node[2] + 1])
    out["C8"] = m.Cm(X_N8, k)
    out["C7"] = m.Cm(X_N7, k)
    return out


def main():
    log = Logger("ident_fisher.log")
    S = np.load(os.path.join(LOGD, "ident_static_scan.npz"))
    tau_rec = float(S["tau_rec"])
    sig_s = tau_rec / 2
    lnalpha = S["Lv44__lnalpha"]
    FQ = np.load(os.path.join(LOGD, "ident_freq_curves.npz"))
    kap = FQ["kap"]
    lnf = {i: np.log(FQ["f_base"][:, i]) for i in range(3)}
    log(f"sigmas: static per gauge {100*sig_s:.2f} % (tau_rec/2), frequency {100*SIG_F:.1f} %, rotation {100*SIG_ROT:.1f} % (assumed)")
    gl = np.log(np.array([0.889 / 1.2, 1.082]))
    sig_g_wide = (gl[1] - gl[0]) / np.sqrt(12)
    log(f"prior on ln gamma': uniform over [{gl[0]:.3f},{gl[1]:.3f}] (mass low..high, e_d 1.0..1.2) -> sd {sig_g_wide:.3f};"
        f" tight alternative sd 0.03")

    m = Model(EI_law(44.0)[0], None, ne=10)
    sch = schemes()
    eps = 0.02

    def slope_f(i, k):
        return (np.interp(np.log(k * (1 + eps)), np.log(kap), lnf[i]) -
                np.interp(np.log(k / (1 + eps)), np.log(kap), lnf[i])) / (2 * np.log(1 + eps))

    log("\n=== Log-sensitivities d ln(.)/d ln kappa at alpha = 1 ===")
    pts = [1e7, K_FE, 5e7, 1.679e8, 1e9]
    table = []
    for k in pts:
        rp, rm, r0 = responses(m, k * (1 + eps), sch), responses(m, k / (1 + eps), sch), responses(m, k, sch)
        Sx = {key: (np.log(rp[key]) - np.log(rm[key])) / (2 * np.log(1 + eps)) for key in r0}
        Sf = [slope_f(i, k) for i in range(3)]
        a = np.exp(np.interp(np.log(k), np.log(KAPPA), lnalpha))
        table.append((k, a, Sx, Sf, r0))
        log(f"kappa={k:.3e} (alpha*={a:.3f}): S_y8={Sx['y8']:+.3f} S_y7={Sx['y7']:+.3f} (S_y8-S_y7={Sx['y8']-Sx['y7']:+.3f}) "
            f"S_C8={Sx['C8']:+.3f} S_C7={Sx['C7']:+.3f} S_f1={Sf[0]:+.3f} S_f3={Sf[2]:+.3f} "
            f"S_rotT8={Sx['rotT8']:+.3f} S_rotT7={Sx['rotT7']:+.3f}; rotT8={r0['rotT8']/a*1e6:.1f} urad, "
            f"rotT7={r0['rotT7']/a*1e6:.1f} urad (scheme III, alpha*)")

    def crb(rows, sig, prior_g=None):
        """prior_g None -> no frequency rows: gamma' column dropped (2x2)."""
        J = np.array(rows, float)
        if prior_g is None:
            J = J[:, :2]
        Wt = np.diag(1 / np.array(sig) ** 2)
        Fm = J.T @ Wt @ J
        if prior_g is not None:
            Fm[2, 2] += 1 / prior_g ** 2
        ev = np.linalg.eigvalsh(Fm)
        if ev.min() <= 1e-10 * ev.max():
            return None, ev
        C = np.linalg.inv(Fm)
        if prior_g is None:
            C3 = np.zeros((3, 3)); C3[:2, :2] = C
            C = C3
        return C, ev

    log("\n=== Cramer-Rao bounds (1 sigma, log units = relative) on ln kappa, ln alpha, ln C8, ln C7 ===")
    log("C8, C7 with alpha and kappa from the fit: grad ln C = [-1, S_C, 0]; 'C8|y8' = ln(C8/y8), the shape factor a BPM user needs")
    for k, a, Sx, Sf, r0 in table:
        rs = [[-1, Sx["y8"], 0], [-1, Sx["y7"], 0]]
        rf3 = [0.5, Sf[2], -0.5]
        rf1 = [0.5, Sf[0], -0.5]
        rr8 = [-1, Sx["rotT8"], 0]
        rr7 = [-1, Sx["rotT7"], 0]
        cases = {
            "(a) y8,y7": (rs, [sig_s] * 2, None),
            "(b) +f3, gamma' wide": (rs + [rf3], [sig_s] * 2 + [SIG_F], sig_g_wide),
            "(b) +f3, gamma' 3%": (rs + [rf3], [sig_s] * 2 + [SIG_F], 0.03),
            "(b') +f1+f3 (if f1 measured), wide": (rs + [rf1, rf3], [sig_s] * 2 + [SIG_F] * 2, sig_g_wide),
            "(c) +rot T8": (rs + [rr8], [sig_s] * 2 + [SIG_ROT], None),
            "(c) +rot T7 pier": (rs + [rr7], [sig_s] * 2 + [SIG_ROT], None),
            "(b)+(c) f3 wide + rot T8": (rs + [rf3, rr8], [sig_s] * 2 + [SIG_F, SIG_ROT], sig_g_wide),
        }
        log(f"-- kappa={k:.3e}, alpha*={a:.3f}")
        for lab, (rows, sig, pg) in cases.items():
            C, ev = crb(rows, sig, pg)
            if C is None:
                log(f"   {lab:36s}: FIM singular (eig {ev.min():.2e}/{ev.max():.2e})")
                continue
            g8 = np.array([-1, Sx["C8"], 0]); g7 = np.array([-1, Sx["C7"], 0])
            gsh = np.array([0, Sx["C8"] - Sx["y8"], 0])
            sd = lambda gg: np.sqrt(gg @ C @ gg)
            cond = ev.max() / ev.min()
            if lab.startswith("(a)"):
                log(f"   (a) closed form: sd ln kappa = sqrt(2)*sigma/|S_y8-S_y7| = {np.sqrt(2)*sig_s/abs(Sx['y8']-Sx['y7']):.3f}")
            log(f"   {lab:36s}: sd ln kappa={np.sqrt(C[1,1]):7.3f}  sd ln alpha={np.sqrt(C[0,0]):6.3f}  "
                f"sd ln C8={sd(g8):6.3f}  sd ln C7={sd(g7):6.3f}  sd ln(C8/y8)={sd(gsh):6.3f}  cond={cond:.1e}")

    # global: shape factor C8/y8 over kappa
    log("\n=== Global: ratio C_m / y_meas-model over kappa (alpha-free), base model ===")
    p8 = S["Lv44__p8"] / 1000; C8 = S["Lv44__C8"]; p7 = S["Lv44__p7"] / 1000; C7 = S["Lv44__C7"]
    sh8 = C8 / p8; sh7 = C7 / p7
    res = S["Lv44__res"]
    for lab, lo, hi in (("static tau_rec", KAPPA[res <= tau_rec].min(), KAPPA[res <= tau_rec].max()),
                        ("static + f3 (wide mass/e_d)", 1.78e7, 1.12e8),
                        ("static + f3 (base mass)", 1.78e7, 2.51e7)):
        sel = (KAPPA >= lo * 0.999) & (KAPPA <= hi * 1.001)
        log(f"{lab:30s}: kappa [{lo:.2e},{hi:.2e}]: C8/y8_model in [{sh8[sel].min():.3e},{sh8[sel].max():.3e}] "
            f"(max/min {sh8[sel].max()/sh8[sel].min():.2f}); C7/y7_model max/min {sh7[sel].max()/sh7[sel].min():.3f}")
    log.save()


if __name__ == "__main__":
    main()
