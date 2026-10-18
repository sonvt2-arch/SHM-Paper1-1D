"""Package 1A - FE for arbitrary linear response channels of continuous girders.

Reuses the element routine of code/analysis/cm_multispan.py (not modified):
  kind="hermite" : prismatic cubic Hermite element (exact for piecewise-constant EI);
  kind="flex"    : non-prismatic element from flexibility integrals (nodally exact for
                   any EI(x), up to Gauss quadrature of 1/EI).
Adds (i) rotational springs at interior supports (monolithic piers), (ii) recovery of
all channels at a node from exact element end forces:
    w (deflection), theta = dw/dx, M (sagging +, M = -EI w''), V = dM/dx,
    support reactions (upward +),
(iii) the influence-line route: the response r_m(x) to a unit load at an arbitrary
abscissa x (consistent Hermite load + fixed-end-force correction; exact for
prismatic elements) and its exact integral (Simpson per element, exact because
r_m is cubic in the load position inside a prismatic element), and
(iv) a convoy record integrated exactly.

Sign conventions: x from the left end support, w and loads positive downward.
Units: whatever is passed in (kN, m for the bridge).
"""
import os
import sys
import numpy as np
import scipy.sparse as sps
from scipy.sparse.linalg import splu

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "analysis"))
from cm_multispan import element  # noqa: E402  (reused, unmodified)


class Girder:
    def __init__(self, spans, EI=lambda x: 1.0, ne_per_span=40, extra_nodes=(),
                 kind="hermite", ngauss=1, k_rot=0.0, h_max=None):
        self.spans = np.asarray(spans, float)
        self.sup = np.concatenate([[0.0], np.cumsum(self.spans)])
        xs = [0.0]
        for a, b in zip(self.sup[:-1], self.sup[1:]):
            n = ne_per_span if h_max is None else max(ne_per_span,
                                                      int(np.ceil((b - a) / h_max)))
            xs += list(np.linspace(a, b, n + 1)[1:])
        x = np.array(xs)
        for xe in extra_nodes:
            if np.min(abs(x - xe)) > 1e-9 * x[-1]:
                x = np.sort(np.append(x, xe))
        self.x = x
        n = len(x)
        self.n = n
        self.ke, self.fe = [], []
        rows, cols, vals = [], [], []
        for e in range(n - 1):
            k, f = element(x[e], x[e + 1], EI, kind, ngauss)
            self.ke.append(k)
            self.fe.append(f)
            idx = [2 * e, 2 * e + 1, 2 * e + 2, 2 * e + 3]
            for a in range(4):
                for b in range(4):
                    rows.append(idx[a]); cols.append(idx[b]); vals.append(k[a, b])
        self.sup_node = [int(np.argmin(abs(x - s))) for s in self.sup]
        kr = np.broadcast_to(np.asarray(k_rot, float), (len(self.sup) - 2,))
        fixed = [2 * i for i in self.sup_node]
        for i, kk in zip(self.sup_node[1:-1], kr):
            if np.isinf(kk):
                fixed.append(2 * i + 1)
            elif kk > 0:
                rows.append(2 * i + 1); cols.append(2 * i + 1); vals.append(kk)
        self.K = sps.csc_matrix((vals, (rows, cols)), shape=(2 * n, 2 * n))
        self.fixed = np.array(sorted(fixed))
        self.free = np.setdiff1d(np.arange(2 * n), self.fixed)
        Kff = self.K[self.free][:, self.free]
        self.d = 1.0 / np.sqrt(Kff.diagonal())          # Jacobi scaling (round-off)
        D = sps.diags(self.d)
        self.lu = splu((D @ Kff @ D).tocsc())
        self.EI = EI

    # ------------------------------------------------------------ solves
    def solve(self, F):
        F = np.atleast_2d(F.T).T if F.ndim == 1 else F
        u = np.zeros_like(F, dtype=float)
        u[self.free] = self.d[:, None] * self.lu.solve(self.d[:, None] * F[self.free])
        return u

    def node(self, xm):
        i = int(np.argmin(abs(self.x - xm)))
        if abs(self.x[i] - xm) > 1e-9 * self.x[-1]:
            raise ValueError("sensor must be a node (pass it in extra_nodes)")
        return i

    def udl_load(self, q=1.0, load_spans=None):
        F = np.zeros(2 * self.n)
        qe = np.zeros(self.n - 1)
        for e in range(self.n - 1):
            j = int(np.searchsorted(self.sup, 0.5 * (self.x[e] + self.x[e + 1])) - 1)
            if load_spans is not None and j not in load_spans:
                continue
            qe[e] = q
            F[2 * e:2 * e + 4] += q * self.fe[e]
        return F, qe

    # ------------------------------------------------------------ channels
    def end_forces(self, u, e, Fe=None):
        """End-force vector on element e (in DOF sense): k u_e - (element load)."""
        f = self.ke[e] @ u[2 * e:2 * e + 4]
        return f if Fe is None else f - Fe

    @staticmethod
    def M_V_from_end(f, side):
        """Sagging moment and shear V = dM/dx at the element end.
        right end (node e+1): M = -f[3], V = +f[2];  left end: M = +f[1], V = -f[0]
        (checked against the simply supported and two-span textbook values)."""
        if side == "right":
            return -f[3], f[2]
        return f[1], -f[0]

    def channels_udl(self, xm, q=1.0, load_spans=None, side="left"):
        """All channels at node xm under a uniform load q (all spans by default).
        side='left' uses the element ending at xm (one-sided M, V at a pier with a
        spring; V left limit), side='right' the element starting at xm."""
        F, qe = self.udl_load(q, load_spans)
        u = self.solve(F)[:, 0]
        i = self.node(xm)
        out = dict(w=u[2 * i], theta=u[2 * i + 1])
        e = i - 1 if (side == "left" and i > 0) or i == self.n - 1 else i
        f = self.end_forces(u, e, qe[e] * self.fe[e])
        out["M"], out["V"] = self.M_V_from_end(f, "right" if e == i - 1 else "left")
        R = -(self.K @ u - F)                      # upward reaction at support DOFs
        out["R"] = np.array([R[2 * s] for s in self.sup_node])
        return out

    def moment_diagram(self, q=1.0, load_spans=None, nsub=1):
        """Sagging moment and shear at element ends (exact) and, inside elements,
        M(s) = M_l + V_l s - q s^2/2 (exact statics). Returns x, M, V (left limits)."""
        F, qe = self.udl_load(q, load_spans)
        u = self.solve(F)[:, 0]
        X, Mv, Vv = [], [], []
        for e in range(self.n - 1):
            f = self.end_forces(u, e, qe[e] * self.fe[e])
            Ml, Vl = self.M_V_from_end(f, "left")
            h = self.x[e + 1] - self.x[e]
            for s in np.linspace(0, h, nsub + 1)[:-1]:
                X.append(self.x[e] + s)
                Mv.append(Ml + Vl * s - qe[e] * s * s / 2)
                Vv.append(Vl - qe[e] * s)
        f = self.end_forces(u, self.n - 2, qe[-1] * self.fe[-1])
        Mr, Vr = self.M_V_from_end(f, "right")
        X.append(self.x[-1]); Mv.append(Mr); Vv.append(Vr)
        return np.array(X), np.array(Mv), np.array(Vv), u

    def moment_zeros(self, q=1.0):
        """Zeros of the uniform-load moment diagram inside the spans (exact roots of
        the quadratic M(s) in each element), supports excluded."""
        F, qe = self.udl_load(q)
        u = self.solve(F)[:, 0]
        zs = []
        for e in range(self.n - 1):
            f = self.end_forces(u, e, qe[e] * self.fe[e])
            Ml, Vl = self.M_V_from_end(f, "left")
            h = self.x[e + 1] - self.x[e]
            r = np.roots([-qe[e] / 2, Vl, Ml]) if qe[e] else np.array([-Ml / Vl])
            for s in np.atleast_1d(r):
                if abs(np.imag(s)) < 1e-14 and -1e-9 * h <= np.real(s) <= h * (1 + 1e-9):
                    z = self.x[e] + np.real(s)
                    if np.min(abs(self.sup - z)) > 1e-9 * self.x[-1] and \
                            (not zs or abs(z - zs[-1]) > 1e-9 * self.x[-1]):
                        zs.append(z)
        return np.array(sorted(zs))

    # ------------------------------------------------------------ influence lines
    def _point_load_vectors(self, X):
        """Consistent nodal vectors (columns) for unit loads at abscissae X, each
        assigned to element E (left-closed; X = x_end -> last element)."""
        E = np.clip(np.searchsorted(self.x, X, side="right") - 1, 0, self.n - 2)
        return E

    def response_unit_load(self, xm, loads, channel, side="left", sup_index=None):
        """r_m for unit loads given as a list of (element e, local s in [0,1]).
        channel in {'w','theta','M','V','R'}; exact for prismatic elements."""
        i = self.node(xm) if channel != "R" else None
        F = np.zeros((2 * self.n, len(loads)))
        Nl = []
        for c, (e, s) in enumerate(loads):
            h = self.x[e + 1] - self.x[e]
            N = np.array([1 - 3 * s**2 + 2 * s**3, h * (s - 2 * s**2 + s**3),
                          3 * s**2 - 2 * s**3, h * (-s**2 + s**3)])
            F[2 * e:2 * e + 4, c] = N
            Nl.append(N)
        U = self.solve(F)
        if channel == "w":
            return U[2 * i]
        if channel == "theta":
            return U[2 * i + 1]
        if channel == "R":
            Rr = -(self.K @ U - F)
            return Rr[2 * self.sup_node[sup_index]]
        e0 = i - 1 if (side == "left" and i > 0) or i == self.n - 1 else i
        endside = "right" if e0 == i - 1 else "left"
        out = np.empty(len(loads))
        for c, (e, s) in enumerate(loads):
            Fe = Nl[c] if e == e0 else None      # fixed-end-force correction
            f = self.end_forces(U[:, c], e0, Fe)
            M, V = self.M_V_from_end(f, endside)
            out[c] = M if channel == "M" else V
        return out

    def il_integral(self, xm, channel, side="left", sup_index=None, return_il=False):
        """Exact integral of the influence line over the whole girder: Simpson on
        each element with loads at s = 0, 1/2, 1 of that element."""
        loads = [(e, s) for e in range(self.n - 1) for s in (0.0, 0.5, 1.0)]
        r = self.response_unit_load(xm, loads, channel, side, sup_index).reshape(-1, 3)
        h = np.diff(self.x)
        I = np.sum(h / 6 * (r[:, 0] + 4 * r[:, 1] + r[:, 2]))
        if return_il:
            return I, r
        return I

    def il_pos_area(self, xm, channel, side="left", sup_index=None, nsub=8):
        """Positive part A+ of the influence-line area (dense composite Simpson on
        nsub sub-panels per element of the clipped line; not exact where the line
        changes sign inside a sub-panel)."""
        s = np.linspace(0, 1, 2 * nsub + 1)
        loads = [(e, si) for e in range(self.n - 1) for si in s]
        r = self.response_unit_load(xm, loads, channel, side, sup_index)
        r = r.reshape(self.n - 1, -1)
        h = np.diff(self.x)
        wts = np.ones(2 * nsub + 1); wts[1:-1:2] = 4; wts[2:-1:2] = 2
        rp = np.clip(r, 0, None)
        return np.sum(h / (3 * 2 * nsub) * (rp @ wts)), np.sum(h / (3 * 2 * nsub) * (r @ wts))


def convoy_integral(g, xm, channel, P, a, side="left", sup_index=None):
    """Complete-crossing record of a convoy (loads P at offsets a behind the leader,
    every offset an integer number of elements of a uniform mesh), integrated with
    composite Simpson on element panels (exact: each axle term is cubic per panel).
    Returns the record integral and the record itself."""
    h = g.x[1] - g.x[0]
    assert np.allclose(np.diff(g.x), h), "uniform mesh required"
    ka = np.rint(np.asarray(a) / h).astype(int)
    assert np.allclose(ka * h, a)
    ne = g.n - 1
    npan = ne + ka.max()                       # lead from x=0 to L + a_max
    loads = [(e, s) for e in range(ne) for s in (0.0, 0.5, 1.0)]
    r = g.response_unit_load(xm, loads, channel, side, sup_index).reshape(ne, 3)
    rec = np.zeros((npan, 3))
    for Pi, ki in zip(P, ka):
        for p in range(npan):
            e = p - ki                          # element under axle i in panel p
            if 0 <= e < ne:
                rec[p] += Pi * r[e]
    I = np.sum(h / 6 * (rec[:, 0] + 4 * rec[:, 1] + rec[:, 2]))
    return I, rec
