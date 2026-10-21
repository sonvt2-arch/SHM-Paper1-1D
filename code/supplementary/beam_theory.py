"""beam_theory.py - shared module of the supplementary scripts.

Contents:
  * specimen constants of the laboratory beam (I = 16 529.8 mm^4,
    EI = 3.3060e9 N mm^2, C_m = l^4/(192 EI) = 61.541 mm^2/N),
  * the mid-span influence line of the equal two-span beam,
  * the closed form of C_m for two spans,
  * the laboratory records (Supplementary Section S6) and the load groups,
  * quadrature rules (trapezoid; Simpson with a 3/8 end panel for an odd
    number of intervals),
  * the estimators BPM (P = I_y/C_m) and SLM,
  * a prismatic Euler-Bernoulli FE solver (Hermite cubic elements) with
    stiffness, consistent mass and consistent point-load vectors.

Three-load group as used here: 2550 g leading, second load 500 mm behind,
third a further 250 mm behind; the order does not change any integral.

Units: N, mm (EI in N mm^2, integrals in mm^2) unless stated otherwise.
"""
import numpy as np

# --------------------------------------------------------------------------
# 1. Specimen (Section 3.1)
# --------------------------------------------------------------------------
B_OUT = 25.0                       # outer size of the square tube (mm)
T_WALL = 2.03                      # wall thickness (mm), averaged from measurements
B_IN = B_OUT - 2.0 * T_WALL
I_Z = (B_OUT ** 4 - B_IN ** 4) / 12.0          # 16 529.76 mm^4
AREA = B_OUT ** 2 - B_IN ** 2                  # 186.52 mm^2 (186.5 in Section 6.5)
E_STEEL = 2.0e5                                # N/mm^2 (200 GPa)
EI = E_STEEL * I_Z                             # 3.30595e9 N mm^2
RHO_STEEL = 7850.0e-9                          # kg/mm^3 (7850 kg/m^3)

L_SPAN = 2500.0                    # span l (mm)
G = 9.81                           # m/s^2 (4.143 kg -> 40.64 N)

P0 = 4.143 * G                     # reference load incl. hook (N) = 40.64 N
C_M = L_SPAN ** 4 / (192.0 * EI)   # mm^2/N, = 61.541

RESOLUTION = 0.005                 # LVDT resolution (mm)
DX = 250.0                         # load-position step (mm)

# load groups: masses (g) and offsets behind the leading load (mm)
GROUPS = {
    "single": dict(m=[4143.0], a=[0.0]),
    "two": dict(m=[2145.0, 4684.0], a=[0.0, 250.0]),
    # Section 3.1: 2550 g leading, 5100 g 500 mm behind, 5100 g a further 250 mm
    "three": dict(m=[2550.0, 5100.0, 5100.0], a=[0.0, 500.0, 750.0]),
}


def group_weight(case):
    """Directly weighed total load of a group (N)."""
    return sum(GROUPS[case]["m"]) / 1000.0 * G


W_TWO = group_weight("two")        # 66.99 N
W_THREE = group_weight("three")    # 125.08 N


# --------------------------------------------------------------------------
# 2. Influence line at mid-span of span AB, Eq. (A.2)
# --------------------------------------------------------------------------
def eta(x, P=1.0, l=L_SPAN, ei=EI):
    """Mid-span deflection of span AB (downward positive) for a load P at x.

    Equal spans l, knife-edge interior support; zero outside [0, 2l].
    The third branch carries the denominator 64 EI (Appendix A).
    """
    x = np.asarray(x, dtype=float)
    b1 = x * (9 * l ** 2 - 13 * x ** 2) / 192.0
    b2 = (x - l) * (4 * l ** 2 - 29 * l * x + 19 * x ** 2) / 192.0
    b3 = (2 * l - x) * (3 * l ** 2 - 4 * l * x + x ** 2) / 64.0
    y = np.where(x < 0, 0.0,
                 np.where(x <= l / 2, b1,
                          np.where(x <= l, b2,
                                   np.where(x <= 2 * l, b3, 0.0))))
    return P * y / ei


def record(case, x, l=L_SPAN, ei=EI, a=None, m=None):
    """Analytical record of a load group, Eq. (1); x = position of leading load."""
    g = GROUPS[case]
    a = g["a"] if a is None else a
    m = g["m"] if m is None else m
    x = np.asarray(x, dtype=float)
    return sum(mi / 1000.0 * G * eta(x - ai, 1.0, l, ei) for mi, ai in zip(m, a))


# --------------------------------------------------------------------------
# 3. Two-span closed form, Eqs. (4)-(5)
# --------------------------------------------------------------------------
def mu_two_span(rho_L, rho_EI=1.0):
    """Eq. (5)."""
    return (1.0 + rho_L ** 3 / rho_EI) / (1.0 + rho_L / rho_EI)


def F_xi_mu(xi, mu):
    """Eq. (4): F(xi, mu)."""
    return xi * (1 - 2 * xi ** 2 + xi ** 3) - 0.5 * mu * xi * (1 - xi ** 2)


def Nm_two_span(rho_L, xi=0.5, rho_EI=1.0):
    """Normalised constant 192 EI_1 C_m / L_1^4 = 8 F, Eqs. (4), (13)."""
    return 8.0 * F_xi_mu(xi, mu_two_span(rho_L, rho_EI))


# --------------------------------------------------------------------------
# 4. Laboratory records, Appendix C (Table C.1)
# --------------------------------------------------------------------------
X_1 = np.arange(0, 5001, 250.0)
Y_ANALYTICAL = np.array([
    0, 0.8874, 1.6968, 2.3501, 2.7693, 2.8764, 2.6253, 2.0980, 1.4087,
    0.6713, 0, -0.5132, -0.8644, -1.0715, -1.1526, -1.1255, -1.0085,
    -0.8194, -0.5763, -0.2971, 0])
Y_SINGLE = np.array([
    0, 0.8844, 1.6975, 2.3525, 2.7738, 2.8827, 2.6363, 2.1100, 1.4213,
    0.6838, 0, -0.5069, -0.8556, -1.0600, -1.1438, -1.1200, -1.0013,
    -0.8175, -0.5816, -0.3019, 0])
X_2 = np.arange(0, 5251, 250.0)
Y_TWO = np.array([
    0, 0.4625, 1.8813, 3.1413, 4.0988, 4.6350, 4.6238, 4.0688, 3.1375,
    1.9600, 0.7715, -0.2689, -1.0063, -1.4988, -1.7813, -1.8600, -1.7738,
    -1.5525, -1.2213, -0.8125, -0.3325, 0])
X_3 = np.arange(0, 5751, 250.0)
Y_THREE = np.array([
    0, 0.5525, 1.0450, 2.5413, 4.8700, 6.7588, 7.9350, 8.2775, 7.6825,
    6.2800, 4.3725, 2.2975, 0.3021, -1.2588, -2.3650, -3.0363, -3.3300,
    -3.2663, -2.9450, -2.4125, -1.7088, -1.0713, -0.3650, 0])

CASES = {
    "single": (X_1, Y_SINGLE, P0),
    "two": (X_2, Y_TWO, W_TWO),
    "three": (X_3, Y_THREE, W_THREE),
}


# --------------------------------------------------------------------------
# 5. Quadrature, Eq. (12), and the estimators
# --------------------------------------------------------------------------
def integral_trapz(y, x, axis=-1):
    """Trapezoidal rule of Eq. (12) (half weights at both ends)."""
    return np.trapezoid(y, x, axis=axis)


def integral_simpson(y, x):
    """Simpson rule of Eq. (12) on a uniform grid; for an odd number of
    intervals the last three intervals use Simpson's 3/8 rule (Section 2.4)."""
    y = np.asarray(y, dtype=float)
    x = np.asarray(x, dtype=float)
    n = len(x) - 1
    h = x[1] - x[0]
    if not np.allclose(np.diff(x), h):
        raise ValueError("uniform grid required")
    if n < 2:
        raise ValueError("need at least two intervals")
    if n % 2 == 0:
        m = n
        tail = 0.0
    else:
        if n < 3:
            raise ValueError("odd n needs at least 3 intervals")
        m = n - 3
        yt = y[m:]
        tail = 3.0 * h / 8.0 * (yt[0] + 3 * yt[1] + 3 * yt[2] + yt[3])
    if m > 0:
        ys = y[:m + 1]
        head = h / 3.0 * (ys[0] + 4 * ys[1:m:2].sum() + 2 * ys[2:m - 1:2].sum() + ys[m])
    else:
        head = 0.0
    return head + tail


def bpm(Iy, Cm=C_M):
    """Beam-property method: P_tot = I_y / C_m (Section 2.4)."""
    return Iy / Cm


def slm(Iy, Iy_ref, P_ref=P0):
    """Standard-load method, Eq. (11)."""
    return P_ref * Iy / Iy_ref


# --------------------------------------------------------------------------
# 6. Prismatic Euler-Bernoulli FE (Hermite cubic elements)
# --------------------------------------------------------------------------
def k_elem(ei, Le):
    return ei / Le ** 3 * np.array([
        [12, 6 * Le, -12, 6 * Le],
        [6 * Le, 4 * Le ** 2, -6 * Le, 2 * Le ** 2],
        [-12, -6 * Le, 12, -6 * Le],
        [6 * Le, 2 * Le ** 2, -6 * Le, 4 * Le ** 2]])


def m_elem(m, Le):
    """Consistent mass matrix, m = mass per unit length."""
    return m * Le / 420.0 * np.array([
        [156, 22 * Le, 54, -13 * Le],
        [22 * Le, 4 * Le ** 2, 13 * Le, -3 * Le ** 2],
        [54, 13 * Le, 156, -22 * Le],
        [-13 * Le, -3 * Le ** 2, -22 * Le, 4 * Le ** 2]])


def hermite(s, Le):
    """Hermite shape functions at local coordinate s in [0, Le]."""
    r = s / Le
    return np.array([1 - 3 * r ** 2 + 2 * r ** 3,
                     Le * (r - 2 * r ** 2 + r ** 3),
                     3 * r ** 2 - 2 * r ** 3,
                     Le * (-r ** 2 + r ** 3)])


class Beam:
    """Continuous prismatic beam on rigid point supports.

    spans : list of span lengths; ne : elements per span (int or list);
    ei : flexural rigidity (scalar or per span); m : mass per unit length.
    Supports at the span ends restrain the vertical DOF only.
    extra : additional node coordinates (e.g. the sensor).
    """

    def __init__(self, spans, ne=20, ei=1.0, m=0.0, extra=()):
        spans = list(spans)
        ne = [ne] * len(spans) if np.isscalar(ne) else list(ne)
        eis = [ei] * len(spans) if np.isscalar(ei) else list(ei)
        sup = np.concatenate([[0.0], np.cumsum(spans)])
        pts = [np.linspace(sup[i], sup[i + 1], ne[i] + 1) for i in range(len(spans))]
        xs = np.unique(np.round(np.concatenate(pts + [np.asarray(extra, float)]), 12))
        self.x = xs
        self.sup = sup
        self.ne = len(xs) - 1
        n = 2 * len(xs)
        K = np.zeros((n, n))
        M = np.zeros((n, n))
        self.el_ei = np.empty(self.ne)
        for e in range(self.ne):
            Le = xs[e + 1] - xs[e]
            xm = 0.5 * (xs[e] + xs[e + 1])
            span = min(np.searchsorted(sup, xm) - 1, len(spans) - 1)
            self.el_ei[e] = eis[span]
            idx = [2 * e, 2 * e + 1, 2 * e + 2, 2 * e + 3]
            K[np.ix_(idx, idx)] += k_elem(eis[span], Le)
            M[np.ix_(idx, idx)] += m_elem(m, Le)
        fixed = [2 * self.node(s) for s in sup]
        self.free = np.array([i for i in range(n) if i not in fixed])
        self.K, self.M = K, M
        self.Kf = K[np.ix_(self.free, self.free)]
        self.Mf = M[np.ix_(self.free, self.free)]
        self.ndof = n

    def node(self, xv):
        i = int(np.argmin(np.abs(self.x - xv)))
        if abs(self.x[i] - xv) > 1e-9 * max(1.0, abs(self.x[-1])):
            raise ValueError("no node at x = %g" % xv)
        return i

    def point_load(self, xp, P=1.0):
        """Consistent nodal load vector (full DOF set) of a point load at xp."""
        F = np.zeros(self.ndof)
        if xp < self.x[0] or xp > self.x[-1]:
            return F
        e = min(int(np.searchsorted(self.x, xp, side="right")) - 1, self.ne - 1)
        Le = self.x[e + 1] - self.x[e]
        F[2 * e:2 * e + 4] += P * hermite(xp - self.x[e], Le)
        return F

    def udl(self, q=1.0):
        """Consistent nodal load vector of a uniform load over the whole beam."""
        F = np.zeros(self.ndof)
        for e in range(self.ne):
            Le = self.x[e + 1] - self.x[e]
            F[2 * e:2 * e + 4] += q * np.array([Le / 2, Le ** 2 / 12, Le / 2, -Le ** 2 / 12])
        return F

    def solve(self, F):
        u = np.zeros(self.ndof)
        u[self.free] = np.linalg.solve(self.Kf, F[self.free])
        return u

    def Cm_udl(self, xm):
        """Eq. (3): C_m = w_q(x_m)/q0 (consistent uniform load)."""
        return self.solve(self.udl(1.0))[2 * self.node(xm)]

    def Cm_il(self, xm):
        """Eq. (3), other route: exact integral of the Hermite-interpolated
        deflected shape under a unit load at the sensor (Maxwell)."""
        u = self.solve(self.point_load(xm, 1.0))
        tot = 0.0
        for e in range(self.ne):
            Le = self.x[e + 1] - self.x[e]
            # integral of Hermite interpolant: Le/2 (w1+w2) + Le^2/12 (t1-t2)
            w1, t1, w2, t2 = u[2 * e:2 * e + 4]
            tot += Le / 2 * (w1 + w2) + Le ** 2 / 12 * (t1 - t2)
        return tot

    def eig(self, nmodes=6):
        from scipy.linalg import eigh
        w2, phi = eigh(self.Kf, self.Mf)
        return np.sqrt(w2[:nmodes]) / (2 * np.pi), phi[:, :nmodes]


if __name__ == "__main__":
    print("I   = %.2f mm^4      (Section 3.1: 16 529.8)" % I_Z)
    print("A   = %.2f mm^2      (Section 6.5: 186.5)" % AREA)
    print("EI  = %.5e N mm^2 (Section 3.1: 3.3060e9)" % EI)
    print("P0  = %.4f N        (Section 3.1: 40.64)" % P0)
    print("C_m = l^4/192EI = %.4f mm^2/N (Section 3.1: 61.541)" % C_M)
    print("P0 C_m = %.4f mm^2  (Table 3: 2501.19)" % (C_M * P0))
