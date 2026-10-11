"""WP3 - 2D Euler-Bernoulli FE for three-span continuous box girders with
variable EI(x) and rotational springs at the monolithic inner piers.

Independent of code/analysis/cm_multispan.py (WP2); written for WP3.
Units: kN, m.  Deflection positive DOWNWARD (load positive downward).
"""
import numpy as np
import scipy.sparse as sp
from scipy.sparse.linalg import splu


class Bridge:
    """Three-span girder, x = 0 at the first end support.

    spans      : (L1, L2, L3)
    EI         : callable EI(x) [kN m^2]
    k_rot      : rotational spring at the two inner piers [kN m/rad];
                 0 -> continuous beam on knife-edge supports (pier pinned),
                 np.inf -> rotation fully fixed (rigid pier, upper bound).
    ne         : elements per metre (mesh density)
    """

    def __init__(self, spans, EI, k_rot=0.0, ne=10):
        self.spans = np.asarray(spans, float)
        self.sup = np.concatenate([[0.0], np.cumsum(self.spans)])
        xs = [0.0]
        for a, b in zip(self.sup[:-1], self.sup[1:]):
            n = int(round((b - a) * ne))
            xs += list(np.linspace(a, b, n + 1)[1:])
        self.x = np.array(xs)
        n = len(self.x)
        h = np.diff(self.x)
        EIe = EI(0.5 * (self.x[:-1] + self.x[1:])) * np.ones(n - 1)
        rows, cols, vals = [], [], []
        for e in range(n - 1):
            he = h[e]
            k = EIe[e] / he ** 3 * np.array(
                [[12, 6 * he, -12, 6 * he], [6 * he, 4 * he * he, -6 * he, 2 * he * he],
                 [-12, -6 * he, 12, -6 * he], [6 * he, 2 * he * he, -6 * he, 4 * he * he]])
            idx = [2 * e, 2 * e + 1, 2 * e + 2, 2 * e + 3]
            for a in range(4):
                for b_ in range(4):
                    rows.append(idx[a]); cols.append(idx[b_]); vals.append(k[a, b_])
        node = [int(np.argmin(abs(self.x - s))) for s in self.sup]
        fixed = [2 * i for i in node]
        for i in node[1:3]:
            if np.isinf(k_rot):
                fixed.append(2 * i + 1)
            elif k_rot > 0:
                rows.append(2 * i + 1); cols.append(2 * i + 1); vals.append(k_rot)
        K = sp.csc_matrix((vals, (rows, cols)), shape=(2 * n, 2 * n))
        self.free = np.setdiff1d(np.arange(2 * n), fixed)
        self.lu = splu(K[self.free][:, self.free].tocsc())
        self.n = n

    def solve(self, F):
        u = np.zeros(2 * self.n)
        u[self.free] = self.lu.solve(F[self.free])
        return u[0::2]

    def point_load(self, xp, P=1.0):
        """Consistent nodal load for a point load anywhere (Hermite shape fns)."""
        F = np.zeros(2 * self.n)
        e = int(np.clip(np.searchsorted(self.x, xp) - 1, 0, self.n - 2))
        h = self.x[e + 1] - self.x[e]
        s = (xp - self.x[e]) / h
        N = [1 - 3 * s**2 + 2 * s**3, h * (s - 2 * s**2 + s**3),
             3 * s**2 - 2 * s**3, h * (-s**2 + s**3)]
        F[[2 * e, 2 * e + 1, 2 * e + 2, 2 * e + 3]] += P * np.array(N)
        return F

    def influence_line(self, xm):
        """Deflection influence line of point xm, eta_m(x) (Maxwell-Betti:
        deflection line under a unit load at xm)."""
        return self.solve(self.point_load(xm))

    def uniform(self, q=1.0):
        """Deflection under uniform load q on all three spans (consistent)."""
        F = np.zeros(2 * self.n)
        for e in range(self.n - 1):
            h = self.x[e + 1] - self.x[e]
            F[[2 * e, 2 * e + 1, 2 * e + 2, 2 * e + 3]] += q * np.array(
                [h / 2, h * h / 12, h / 2, -h * h / 12])
        return self.solve(F)

    def Cm(self, xm):
        eta = self.influence_line(xm)
        c = np.trapezoid(eta, self.x)
        pos = np.trapezoid(np.clip(eta, 0, None), self.x)
        neg = np.trapezoid(np.clip(eta, None, 0), self.x)
        return c, pos, neg, eta

    def span_of(self, xm):
        i = int(np.clip(np.searchsorted(self.sup, xm) - 1, 0, 2))
        return i, self.spans[i]


def haunch_EI(spans, E, I_mid, I_pier, h_mid, h_pier, Lv):
    """EI(x) for a balanced-cantilever girder: parabolic depth
    h(d) = h_mid + (h_pier-h_mid)(1-d/Lv)^2 for d<Lv (d = distance to the
    nearest inner pier axis), h_mid elsewhere; I(h) = I_mid (h/h_mid)^n with
    n fitted to I_pier/I_mid."""
    sup = np.concatenate([[0.0], np.cumsum(spans)])
    p1, p2 = sup[1], sup[2]
    n = np.log(I_pier / I_mid) / np.log(h_pier / h_mid)

    def h(x):
        d = np.minimum(abs(x - p1), abs(x - p2))
        return np.where(d < Lv, h_mid + (h_pier - h_mid) * (1 - d / Lv) ** 2, h_mid)

    def EI(x):
        return E * I_mid * (h(x) / h_mid) ** n

    return EI, h, n
