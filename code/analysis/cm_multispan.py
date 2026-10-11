"""Invariance constant C_m for multi-span continuous beams (Euler-Bernoulli FE).

C_m = area under the deflection influence line at the sensor
    = deflection at the sensor under a unit uniform load on all spans (Maxwell-Betti).
Uniform EI by default; pass an EI(x) callable for haunched girders.
Output is normalised by L_ref^4/(192 EI) so it is comparable with Eq. (11a) of the manuscript.

WP2 extensions (backward compatible; defaults reproduce the original script):
  * extra_nodes: put a node exactly at the sensor for arbitrary x_m;
  * ngauss > 1: element stiffness integrated with Gauss-Legendre points of EI(x)
    (ngauss = 1 is the original mid-point rule);
  * Cm(..., quad="hermite"): exact integral of the cubic Hermite influence line
    (trapezoid kept as default); Cm_udl(): consistent-load route w_q(x_m)/q0,
    optionally loading only selected spans (span-wise contributions);
  * haunch_EI(): parabolic box-girder depth h(x) between h_mid and h_pier, I ~ h^n.
For prismatic elements with nodes at supports and sensor, the FE nodal values and the
Hermite integral are exact, so the FE reproduces closed forms to round-off.
"""
import numpy as np


def beam_fe(spans, ne_per_span=200, EI=lambda x: 1.0, extra_nodes=(), ngauss=1):
    xs = [0.0]
    for L in spans:
        xs += list(np.linspace(xs[-1], xs[-1] + L, ne_per_span + 1)[1:])
    x = np.array(xs)
    for xe in extra_nodes:                          # sensor node(s), if not on the grid
        if np.min(abs(x - xe)) > 1e-9 * x[-1]:
            x = np.sort(np.append(x, xe))
    n = len(x)
    gp, gw = np.polynomial.legendre.leggauss(ngauss)
    K = np.zeros((2 * n, 2 * n))
    for e in range(n - 1):
        h = x[e + 1] - x[e]
        if ngauss == 1:
            k = EI(0.5 * (x[e] + x[e + 1])) / h**3 * np.array(
                [[12, 6 * h, -12, 6 * h], [6 * h, 4 * h * h, -6 * h, 2 * h * h],
                 [-12, -6 * h, 12, -6 * h], [6 * h, 2 * h * h, -6 * h, 4 * h * h]])
        else:                                       # k = int B^T EI(x) B dx
            k = np.zeros((4, 4))
            for g, wg in zip(gp, gw):
                B = np.array([6 * g, (3 * g - 1) * h, -6 * g, (3 * g + 1) * h]) / h**2
                k += wg * 0.5 * h * EI(x[e] + 0.5 * h * (g + 1)) * np.outer(B, B)
        idx = [2 * e, 2 * e + 1, 2 * e + 2, 2 * e + 3]
        K[np.ix_(idx, idx)] += k
    supports = np.concatenate([[0.0], np.cumsum(spans)])
    fixed = [2 * int(np.argmin(abs(x - s))) for s in supports]
    free = np.setdiff1d(np.arange(2 * n), fixed)
    return x, K, free


def _solve(K, free, F):
    u = np.zeros_like(F)
    u[free] = np.linalg.solve(K[np.ix_(free, free)], F[free])
    return u


def influence_line(spans, xm, **kw):
    kw.setdefault("extra_nodes", (xm,))
    x, K, free = beam_fe(spans, **kw)
    F = np.zeros(2 * len(x))
    F[2 * int(np.argmin(abs(x - xm)))] = 1.0      # unit load at sensor
    u = _solve(K, free, F)
    return x, u[0::2], u[1::2]                      # = eta_m(x) by Maxwell-Betti


def Cm(spans, xm, quad="trapezoid", **kw):
    x, w, th = influence_line(spans, xm, **kw)
    if quad == "hermite":                           # exact for the cubic interpolant
        h = np.diff(x)
        c = np.sum(h / 2 * (w[:-1] + w[1:]) + h**2 / 12 * (th[:-1] - th[1:]))
    else:
        c = np.trapezoid(w, x)
    return c, x, w


def Cm_udl(spans, xm, load_spans=None, **kw):
    """w_q(x_m)/q0 with consistent nodal loads; load_spans = indices of loaded spans."""
    kw.setdefault("extra_nodes", (xm,))
    x, K, free = beam_fe(spans, **kw)
    edges = np.concatenate([[0.0], np.cumsum(spans)])
    F = np.zeros(2 * len(x))
    for e in range(len(x) - 1):
        xc = 0.5 * (x[e] + x[e + 1])
        j = int(np.searchsorted(edges, xc) - 1)
        if load_spans is not None and j not in load_spans:
            continue
        h = x[e + 1] - x[e]
        F[2 * e:2 * e + 4] += np.array([h / 2, h * h / 12, h / 2, -h * h / 12])
    u = _solve(K, free, F)
    return u[2 * int(np.argmin(abs(x - xm)))]


def piecewise_EI(spans, EIs):
    """Piecewise-constant EI, one value per span."""
    edges = np.concatenate([[0.0], np.cumsum(spans)])
    return lambda x: EIs[min(int(np.searchsorted(edges, x) - 1), len(spans) - 1)]


def haunch_depth(spans, h_mid, h_pier, lc_side=None):
    """Parabolic soffit, h = h_mid + (h_pier - h_mid)(1 - d/Lc)^2 for d < Lc, d = distance
    to the nearest interior pier. Interior spans: Lc = L/2 (vertex at mid-span).
    End spans: Lc = lc_side (default: half the adjacent interior span, i.e. the
    balanced-cantilever arm), capped at the span; h = h_mid beyond Lc."""
    edges = np.concatenate([[0.0], np.cumsum(spans)])
    piers = edges[1:-1]
    ns = len(spans)

    def h(x):
        j = min(max(int(np.searchsorted(edges, x) - 1), 0), ns - 1)
        L = spans[j]
        if j == 0 or j == ns - 1:
            Lc = lc_side if lc_side is not None else 0.5 * spans[1 if j == 0 else ns - 2]
            Lc = min(Lc, L)
        else:
            Lc = 0.5 * L
        d = np.min(abs(piers - x))
        return h_mid + (h_pier - h_mid) * (1 - d / Lc)**2 if d < Lc else h_mid
    return h


def haunch_EI(spans, h_mid, h_pier, n=2.5, lc_side=None):
    """EI(x)/EI(h_mid) = (h(x)/h_mid)^n  (assumption: I ~ h^n, constant E)."""
    h = haunch_depth(spans, h_mid, h_pier, lc_side)
    return lambda x: (h(x) / h_mid)**n


if __name__ == "__main__":
    cases = {
        "lab 2x2.5 m, mid span 1": ([2.5, 2.5], 1.25),
        "Cau May 55+90+55, mid side span": ([55, 90, 55], 27.5),
        "Cau May 55+90+55, mid main span": ([55, 90, 55], 100.0),
        "Thai Binh 42+63+42, mid side span": ([42, 63, 42], 21.0),
        "Thai Binh 42+63+42, mid main span": ([42, 63, 42], 73.5),
    }
    for name, (spans, xm) in cases.items():
        c, x, w = Cm(spans, xm)
        # span of the sensor as reference length
        edges = np.concatenate([[0], np.cumsum(spans)])
        Lref = spans[int(np.searchsorted(edges, xm) - 1)]
        pos = np.trapezoid(np.clip(w, 0, None), x)
        neg = np.trapezoid(np.clip(w, None, 0), x)
        print(f"{name:38s} 192EI*Cm/L^4 = {192*c/Lref**4:8.4f}   "
              f"neg/pos = {neg/pos:7.3f}")

    print("\nHaunched box (EI normalised at h_mid; I ~ h^n assumed; side-span haunch"
          " length = L_m/2):")
    for name, spans, hm, hp in [("Cau May", [55, 90, 55], 2.4, 5.4)]:
        for n in (2.0, 2.5, 3.0):
            EIf = haunch_EI(spans, hm, hp, n)
            for lab, xm, Lr in [("mid side", spans[0] / 2, spans[0]),
                                ("mid main", spans[0] + spans[1] / 2, spans[1])]:
                c = Cm_udl(spans, xm, ne_per_span=400, EI=EIf, ngauss=4)
                print(f"{name} n={n:3.1f} {lab:9s} 192EI_mid*Cm/L^4 = {192*c/Lr**4:8.4f}")
