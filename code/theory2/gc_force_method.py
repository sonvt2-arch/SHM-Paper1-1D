"""Package 1A - independent force-method solution of a three-span girder with
arbitrary EI(x) and rotational springs k at the two inner supports, under a uniform
load on all spans (adaptive quadrature of the flexibility integrals).
Used only to check the non-prismatic FE (gc_fe.Girder, kind='flex').

Unknowns: girder moments at B (left, right), C (left, right), pier rotations.
Node condition from the energy variation: M(B+) = M(B-) - k theta_B.
Span j (local s in [0, L_j]): M(s) = q s(L-s)/2 + M_l (1 - s/L) + M_r s/L,
theta(0) = int M (1-s/L)/EI ds,  theta(L) = -int M (s/L)/EI ds  (theta = dw/dx).
"""
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq


class ForceMethod3:
    def __init__(self, spans, EI, k=0.0, q=1.0, breaks=()):
        self.L = np.asarray(spans, float)
        self.x0 = np.concatenate([[0.0], np.cumsum(self.L)])
        self.EI, self.q, self.k = EI, q, k
        self.breaks = breaks
        a, b, c, p0, p1 = (np.zeros(3) for _ in range(5))
        for j in range(3):
            a[j] = self._int(j, lambda s, L: (1 - s / L)**2)
            b[j] = self._int(j, lambda s, L: (s / L) * (1 - s / L))
            c[j] = self._int(j, lambda s, L: (s / L)**2)
            p0[j] = self._int(j, lambda s, L: q * s * (L - s) / 2 * (1 - s / L))
            p1[j] = self._int(j, lambda s, L: q * s * (L - s) / 2 * (s / L))
        # unknown vector z = [Mb1, Mb2, Mc2, Mc3, thB, thC]
        if np.isinf(k):
            # thB = thC = 0: span 1 right, span 2 both ends, span 3 left clamped
            Mb1 = -p1[0] / c[0]
            Mc3 = -p0[2] / a[2]
            A2 = np.array([[a[1], b[1]], [b[1], c[1]]])
            Mb2, Mc2 = np.linalg.solve(A2, [-p0[1], -p1[1]])
            z = np.array([Mb1, Mb2, Mc2, Mc3, 0.0, 0.0])
        else:
            A = np.zeros((6, 6)); r = np.zeros(6)
            A[0] = [-c[0], 0, 0, 0, -1, 0]; r[0] = p1[0]
            A[1] = [0, a[1], b[1], 0, -1, 0]; r[1] = -p0[1]
            A[2] = [-1, 1, 0, 0, k, 0]; r[2] = 0
            A[3] = [0, -b[1], -c[1], 0, 0, -1]; r[3] = p1[1]
            A[4] = [0, 0, 0, a[2], 0, -1]; r[4] = -p0[2]
            A[5] = [0, 0, -1, 1, 0, k]; r[5] = 0
            z = np.linalg.solve(A, r)
        self.z = z
        self.ends = [(0.0, z[0]), (z[1], z[2]), (z[3], 0.0)]
        self.theta_sup = [p0[0] + b[0] * z[0], z[4], z[5], -(p1[2] + b[2] * z[3])]

    def _int(self, j, f, s_hi=None):
        L = self.L[j]; x0 = self.x0[j]
        hi = L if s_hi is None else s_hi
        pts = [p - x0 for p in self.breaks if 0 < p - x0 < hi]
        val, _ = quad(lambda s: f(s, L) / self.EI(x0 + s), 0, hi, points=pts or None,
                      limit=400, epsabs=0, epsrel=2e-14)
        return val

    def span(self, x):
        j = int(np.clip(np.searchsorted(self.x0, x, side="right") - 1, 0, 2))
        return j, x - self.x0[j]

    def M(self, x, j=None):
        if j is None:
            j, s = self.span(x)
        else:
            s = x - self.x0[j]
        L = self.L[j]; Ml, Mr = self.ends[j]
        return self.q * s * (L - s) / 2 + Ml * (1 - s / L) + Mr * s / L

    def V(self, x, j=None):
        if j is None:
            j, s = self.span(x)
        else:
            s = x - self.x0[j]
        L = self.L[j]; Ml, Mr = self.ends[j]
        return self.q * (L / 2 - s) + (Mr - Ml) / L

    def theta(self, x):
        j, s = self.span(x)
        th0 = self.theta_sup[j]
        L = self.L[j]; Ml, Mr = self.ends[j]
        f = lambda t, L_: self.q * t * (L_ - t) / 2 + Ml * (1 - t / L_) + Mr * t / L_
        return th0 - self._int(j, f, s_hi=s) if s > 0 else th0

    def reactions(self):
        R = np.zeros(4)
        for j in range(3):
            R[j] += self.V(self.x0[j], j)
            R[j + 1] -= self.V(self.x0[j + 1], j)
        return R

    def zeros(self):
        zs = []
        for j in range(3):
            xs = np.linspace(self.x0[j], self.x0[j + 1], 2001)[1:-1]
            Mv = np.array([self.M(x, j) for x in xs])
            for i in np.where(np.sign(Mv[:-1]) != np.sign(Mv[1:]))[0]:
                zs.append(brentq(lambda x: self.M(x, j), xs[i], xs[i + 1], xtol=1e-14,
                                 rtol=1e-15))
        return np.array(zs)
