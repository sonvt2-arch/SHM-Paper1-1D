"""
beam_theory.py
==============
Shared module for the paper

    "Deflection-integral invariance for indirect identification of total
     service loads on continuous beams"

Contains:
  * the specimen constants,
  * the closed-form mid-span deflection influence line of the two-span
    continuous beam (Eq. 6 of the paper),
  * the measured data sets (Tables 1 and 3 of the paper),
  * the BPM / SLM estimators,
  * a minimal Euler-Bernoulli beam finite element solver used for the
    Maxwell-Betti corollary and the parametric study.

Every other script in this folder imports from here, so the constants and
the data exist in exactly one place.

Units: N, mm  (so EI is in N mm^2 and the deflection integral in mm^2).
"""

import numpy as np
from scipy.integrate import simpson

# --------------------------------------------------------------------------
# 1. Specimen constants
# --------------------------------------------------------------------------
B_OUT = 25.0            # outer size of the hollow square tube (mm)
T_WALL = 2.03           # wall thickness (mm)
B_IN = B_OUT - 2 * T_WALL
I_Z = (B_OUT ** 4 - B_IN ** 4) / 12.0        # second moment of area (mm^4)
E_STEEL = 2.0e5                              # Young modulus (MPa = N/mm^2)
EI = E_STEEL * I_Z                           # flexural rigidity (N mm^2)

L_SPAN = 2500.0         # individual span length l (mm)
G = 9.81                # m/s^2, used to convert the calibrated masses

P0 = 4.143 * G          # reference (standard) load, N   -- 4.143 kg
W_TWO = 6.829 * G       # directly weighed total load, two-load case (N)
W_THREE = 12.750 * G    # directly weighed total load, three-load case (N)

C_M = L_SPAN ** 4 / (192.0 * EI)   # invariance constant, Eq. (11), mm^2/N


# --------------------------------------------------------------------------
# 2. Deflection influence line at mid-span of span AB  --  Eq. (6)
# --------------------------------------------------------------------------
def eta(x, P=1.0, l=L_SPAN, ei=EI):
    """Mid-span deflection of span AB for a load P at abscissa x.

    NOTE the denominator of the third branch: 64*EI, not 192*EI.  The
    factor of three is easily lost when the polynomial is factorised; it
    can be checked at x = 1.5 l, where the correct value is -0.375 P l^3 /
    (64 EI) and matches the measurements.
    """
    x = np.asarray(x, dtype=float)
    return np.where(
        x < 0, 0.0,
        np.where(x <= l / 2, P * (9 * l**2 * x - 13 * x**3) / (192 * ei),
        np.where(x <= l,     P * (-4 * l**3 + 33 * l**2 * x
                                  - 48 * l * x**2 + 19 * x**3) / (192 * ei),
        np.where(x <= 2 * l, P * (6 * l**3 - 11 * l**2 * x
                                  + 6 * l * x**2 - x**3) / (64 * ei),
                             0.0))))


# --------------------------------------------------------------------------
# 3. Measured data  (Tables 1 and 3 of the paper)
# --------------------------------------------------------------------------
# Analytical values reported in the original manuscript, retained for the
# cross-check performed in 01_verify_equations.py
X_1 = np.arange(0, 5001, 250.0)
Y_ANALYTICAL = np.array([
    0, 0.8874, 1.6968, 2.3501, 2.7693, 2.8764, 2.6253, 2.0980, 1.4087,
    0.6713, 0, -0.5132, -0.8644, -1.0715, -1.1526, -1.1255, -1.0085,
    -0.8194, -0.5763, -0.2971, 0])

# Single reference load, 4.143 kg
Y_SINGLE = np.array([
    0, 0.8844, 1.6975, 2.3525, 2.7738, 2.8827, 2.6363, 2.1100, 1.4213,
    0.6838, 0, -0.5069, -0.8556, -1.0600, -1.1438, -1.1200, -1.0013,
    -0.8175, -0.5816, -0.3019, 0])

# Two loads, 2145 g + 4684 g, spacing 250 mm  ->  record to 2l + 250
X_2 = np.arange(0, 5251, 250.0)
Y_TWO = np.array([
    0, 0.4625, 1.8813, 3.1413, 4.0988, 4.6350, 4.6238, 4.0688, 3.1375,
    1.9600, 0.7715, -0.2689, -1.0063, -1.4988, -1.7813, -1.8600, -1.7738,
    -1.5525, -1.2213, -0.8125, -0.3325, 0])

# Three loads, 2550 g + 5100 g + 5100 g, spacings 250 and 500 mm
X_3 = np.arange(0, 5751, 250.0)
Y_THREE = np.array([
    0, 0.5525, 1.0450, 2.5413, 4.8700, 6.7588, 7.9350, 8.2775, 7.6825,
    6.2800, 4.3725, 2.2975, 0.3021, -1.2588, -2.3650, -3.0363, -3.3300,
    -3.2663, -2.9450, -2.4125, -1.7088, -1.0713, -0.3650, 0])

CASES = {
    "single": (X_1, Y_SINGLE, P0),
    "two":    (X_2, Y_TWO,   W_TWO),
    "three":  (X_3, Y_THREE, W_THREE),
}


# --------------------------------------------------------------------------
# 4. Quadrature and the two estimators
# --------------------------------------------------------------------------
def integral_trapz(y, x):
    """Eq. (13) -- trapezoidal rule, with the half-weights at both ends."""
    return np.trapezoid(y, x)


def integral_simpson(y, x):
    """Eq. (14) -- Simpson's rule."""
    return simpson(y, x=x)


def bpm(Iy, l=L_SPAN, ei=EI):
    """Beam Property-based Method, Eq. (12).  Returns the total load in N."""
    return 192.0 * ei * Iy / l ** 4


def slm(Iy, Iy_ref, P_ref=P0):
    """Standard Load-based Method, Eq. (15).  Returns the total load in N."""
    return P_ref * Iy / Iy_ref


# --------------------------------------------------------------------------
# 5. Minimal Euler-Bernoulli beam finite element solver
# --------------------------------------------------------------------------
def _assemble(xs, ei):
    n = len(xs)
    K = np.zeros((2 * n, 2 * n))
    for e in range(n - 1):
        Le = xs[e + 1] - xs[e]
        k = ei / Le ** 3 * np.array([
            [12,      6 * Le,     -12,      6 * Le],
            [6 * Le,  4 * Le * Le, -6 * Le, 2 * Le * Le],
            [-12,    -6 * Le,      12,     -6 * Le],
            [6 * Le,  2 * Le * Le, -6 * Le, 4 * Le * Le]])
        idx = [2 * e, 2 * e + 1, 2 * e + 2, 2 * e + 3]
        K[np.ix_(idx, idx)] += k
    return K


def _mesh(l1, l2, x_extra, nel=200):
    """Uniform mesh over both spans with x_extra inserted, duplicates removed."""
    pts = np.sort(np.concatenate([np.linspace(0, l1, nel + 1),
                                  np.linspace(l1, l1 + l2, nel + 1),
                                  [x_extra]]))
    keep = [pts[0]]
    for p in pts[1:]:
        if p - keep[-1] > 1e-9 * (l1 + l2):
            keep.append(p)
    return np.array(keep)


def deflected_shape(l1, l2, x_load, ei=1.0, nel=200):
    """Deflected shape of the two-span beam under a unit load at x_load.

    Supports: rollers at x = 0 and x = l1 + l2, hinge at x = l1.
    Returns (xs, w) with w the vertical deflection.
    """
    xs = _mesh(l1, l2, x_load, nel)
    idx = lambda v: int(np.argmin(np.abs(xs - v)))
    K = _assemble(xs, ei)
    F = np.zeros(2 * len(xs))
    F[2 * idx(x_load)] = 1.0
    fixed = [0, 2 * idx(l1), 2 * (len(xs) - 1)]
    free = [i for i in range(2 * len(xs)) if i not in fixed]
    u = np.zeros(2 * len(xs))
    u[free] = np.linalg.solve(K[np.ix_(free, free)], F[free])
    return xs, u[0::2]


def C_of(l1, l2, x_m, ei=1.0, nel=200):
    """Invariance constant via the Maxwell-Betti corollary, Eq. (10):

        C_m = integral over the structure of the deflected shape produced
              by a unit static load applied at the measurement point.
    """
    xs, w = deflected_shape(l1, l2, x_m, ei, nel)
    return simpson(w, x=xs)


if __name__ == "__main__":
    print("I  = %.2f mm^4" % I_Z)
    print("EI = %.5e N mm^2" % EI)
    print("P0 = %.4f N" % P0)
    print("C_m = l^4/192EI = %.4f mm^2/N" % C_M)
    print("exact single-load integral = %.4f mm^2" % (C_M * P0))
