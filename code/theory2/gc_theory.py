"""Package 1A - closed forms for arbitrary response channels (deflection w, rotation
theta, bending moment M / strain eps = c M/EI, shear V, support reactions R) of
continuous beams under a uniform unit load: by the generalised invariance theorem
these are the integration constants C_r of a complete crossing.

Span-level building block (prismatic span of length L, rigidity EI, uniform q0,
sagging end moments M_l, M_r written through the hogging parameters
m_l = -8 M_l/(q0 L^2), m_r = -8 M_r/(q0 L^2); xi = s/L from the left end):

  N_w = 192 EI C_w/L^4  = 8 Phi(xi)
        Phi = xi(1-2xi^2+xi^3) - m_l/2 (2xi-3xi^2+xi^3) - m_r/2 (xi-xi^3)
  N_th = 24 EI C_th/L^3 = Phi'(xi)
  N_M = 8 M_q/(q0 L^2)  = 4xi(1-xi) - m_l(1-xi) - m_r xi      (C_eps = c L^2 N_M/(8EI))
  N_V = 2 V_q/(q0 L)    = 1 - 2xi + (m_l - m_r)/4
  reactions: the span delivers q0 L(4 + m_l - m_r)/8 to its left support and
             q0 L(4 - m_l + m_r)/8 to its right support.

Each normalisation equals 1 for the simply supported reference (mid-span w and M,
end rotation, end shear, end reaction).

Structure-level parameters (piecewise-constant EI; knife-edge supports):
  two-span (L1, L2 = rho_L L1, EI2 = rho_EI EI1):
      mu = (1 + rho_L^3/rho_EI)/(1 + rho_L/rho_EI)  (Eq. (5)),
      span 1: (m_l, m_r) = (0, mu);  span 2 (local xi from B): (mu/rho_L^2, 0)
  symmetric three-span (Ls, Lm = beta Ls, EIm = rho EIs):
      mu = 2(rho + beta^3)/(2 rho + 3 beta)  (Eq. (8)),  side 1: (0, mu),
      main: (m, m) with m = mu/beta^2 = 2 nu/3,  side 3: (mu, 0)
  n-span: support moments from the three-moment equation (three_moment()).
"""
import numpy as np

# ---------------------------------------------------------------- span level

def Phi(xi, ml, mr):
    return (xi * (1 - 2 * xi**2 + xi**3) - ml / 2 * (2 * xi - 3 * xi**2 + xi**3)
            - mr / 2 * (xi - xi**3))


def dPhi(xi, ml, mr):
    return (1 - 6 * xi**2 + 4 * xi**3 - ml / 2 * (2 - 6 * xi + 3 * xi**2)
            - mr / 2 * (1 - 3 * xi**2))


def N_w(xi, ml, mr):
    return 8 * Phi(xi, ml, mr)


def N_th(xi, ml, mr):
    return dPhi(xi, ml, mr)


def N_M(xi, ml, mr):
    return 4 * xi * (1 - xi) - ml * (1 - xi) - mr * xi


def N_V(xi, ml, mr):
    return 1 - 2 * xi + (ml - mr) / 4


def span_channels(xi, L, EI, ml, mr, q0=1.0):
    """Dimensional constants C_r = r_q(x_m)/q0 for a sensor inside the span."""
    return dict(w=L**4 / (192 * EI) * N_w(xi, ml, mr),
                theta=L**3 / (24 * EI) * N_th(xi, ml, mr),
                M=L**2 / 8 * N_M(xi, ml, mr),
                V=L / 2 * N_V(xi, ml, mr))


def moment_zeros(ml, mr):
    """Interior zeros of N_M on (0,1): 4 xi^2 - (4 + ml - mr) xi + ml = 0."""
    r = np.roots([4.0, -(4.0 + ml - mr), ml])
    return sorted(float(z.real) for z in r if abs(z.imag) < 1e-14 and 1e-12 < z.real < 1 - 1e-12)


def band_edges(ml, mr, thr=0.2):
    """Roots on (0,1) of N_M = +thr and N_M = -thr (edges of the strain blind band)."""
    out = []
    for t in (thr, -thr):
        r = np.roots([4.0, -(4.0 + ml - mr), ml + t])
        out += [float(z.real) for z in r if abs(z.imag) < 1e-14 and 0 < z.real < 1]
    return sorted(out)


# ---------------------------------------------------------------- structures

def mu_two(rho_L, rho_EI=1.0):
    return (1 + rho_L**3 / rho_EI) / (1 + rho_L / rho_EI)


def mu_three(beta, rho=1.0):
    return 2 * (rho + beta**3) / (2 * rho + 3 * beta)


def two_span(rho_L, rho_EI=1.0):
    """Span list [(L, EI, ml, mr)] with L1 = EI1 = 1."""
    mu = mu_two(rho_L, rho_EI)
    return [(1.0, 1.0, 0.0, mu), (rho_L, rho_EI, mu / rho_L**2, 0.0)]


def three_span_sym(beta, rho=1.0):
    mu = mu_three(beta, rho)
    m = mu / beta**2
    return [(1.0, 1.0, 0.0, mu), (beta, rho, m, m), (1.0, 1.0, mu, 0.0)]


def three_moment(spans, EIs, q=1.0):
    """Support moments of an n-span continuous beam (knife-edge supports, uniform q,
    piecewise-constant EI) from the three-moment equation; returns (L, EI, ml, mr)."""
    n = len(spans)
    L = np.asarray(spans, float); E = np.asarray(EIs, float)
    A = np.zeros((n - 1, n - 1)); b = np.zeros(n - 1)
    for i in range(1, n):           # support i between span i-1 and span i
        a, c = L[i - 1] / E[i - 1], L[i] / E[i]
        A[i - 1, i - 1] = 2 * (a + c)
        if i - 2 >= 0:
            A[i - 1, i - 2] = a
        if i < n - 1:
            A[i - 1, i] = c
        b[i - 1] = -q * (L[i - 1]**3 / E[i - 1] + L[i]**3 / E[i]) / 4
    Ms = np.concatenate([[0.0], np.linalg.solve(A, b), [0.0]])
    return [(L[j], E[j], -8 * Ms[j] / (q * L[j]**2), -8 * Ms[j + 1] / (q * L[j]**2))
            for j in range(n)]


def reactions(spl, q0=1.0):
    """Support reactions (upward) under q0 on all spans, from span-level shears."""
    R = np.zeros(len(spl) + 1)
    for j, (L, EI, ml, mr) in enumerate(spl):
        R[j] += q0 * L * (4 + ml - mr) / 8
        R[j + 1] += q0 * L * (4 - ml + mr) / 8
    return R


def at(spl, j, xi):
    """Constants at local position xi of span j (dimensional, q0 = 1)."""
    L, EI, ml, mr = spl[j]
    return span_channels(xi, L, EI, ml, mr)


# ---------------------------------------------------------------- special roots

def roots_summary():
    """Exact blind configurations of the non-deflection channels (uniform EI)."""
    out = {}
    # two-span, end reaction / contraflexure leaves span 1: mu = 4 -> rho^2-rho-3 = 0
    out["2span_endR_blind_rhoL"] = (1 + np.sqrt(13)) / 2
    # two-span, end-support rotation: mu = 2 -> rho^2 - rho - 1 = 0 (golden ratio)
    out["2span_endrot_blind_rhoL"] = (1 + np.sqrt(5)) / 2
    # two-span, interior-support rotation: mu = 1 <=> rho_L = 1 (any rho_EI)
    out["2span_Brot_blind_rhoL"] = 1.0
    # three-span: interior-support rotation: mu = 1 <=> 2 beta^3 = 3 beta (any rho)
    out["3span_Brot_blind_beta"] = np.sqrt(1.5)
    # three-span: end rotation mu = 2 -> beta^3 - 3 beta - 1 = 0 (uniform EI)
    out["3span_endrot_blind_beta"] = 2 * np.cos(np.pi / 9)
    # three-span: end reaction mu = 4 -> beta^3 - 6 beta - 3 = 0 (uniform EI)
    out["3span_endR_blind_beta"] = 2 * np.sqrt(2) * np.cos(
        np.arccos(9 / 12 * np.sqrt(0.5)) / 3)
    # three-span: mid main-span strain mu/beta^2 = 1 -> beta^3 + 2 beta^2 - 2 = 0
    r = np.roots([1, 2, 0, -2]); out["3span_midmain_strain_blind_beta"] = float(
        max(z.real for z in r if abs(z.imag) < 1e-12))
    # three-span: main span loses its sagging zone (m >= 1) -> same cubic
    # three-span: mid main-span strain at band edge N_M = 0.2: m = 0.8
    # -> 2(1+b^3) = 0.8 b^2 (2+3b) -> 2 b^3 - 2.4 b^3 ... solved numerically
    r = np.roots([2 - 2.4, -1.6, 0, 2]); out["3span_midmain_strain_N0.2_beta"] = float(
        max(z.real for z in r if abs(z.imag) < 1e-12 and z.real > 0))
    return out
