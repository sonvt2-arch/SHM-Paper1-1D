"""Invariance constant C_m for multi-span continuous beams (Euler-Bernoulli FE).

C_m = area under the deflection influence line at the sensor
    = deflection at the sensor under a unit uniform load on all spans (Maxwell-Betti).
Uniform EI by default; pass an EI(x) callable for haunched girders.
Output is normalised by L_ref^4/(192 EI) so it is comparable with Eq. (11a) of the manuscript.
"""
import numpy as np


def beam_fe(spans, ne_per_span=200, EI=lambda x: 1.0):
    xs = [0.0]
    for L in spans:
        xs += list(np.linspace(xs[-1], xs[-1] + L, ne_per_span + 1)[1:])
    x = np.array(xs)
    n = len(x)
    K = np.zeros((2 * n, 2 * n))
    for e in range(n - 1):
        h = x[e + 1] - x[e]
        k = EI(0.5 * (x[e] + x[e + 1])) / h**3 * np.array(
            [[12, 6 * h, -12, 6 * h], [6 * h, 4 * h * h, -6 * h, 2 * h * h],
             [-12, -6 * h, 12, -6 * h], [6 * h, 2 * h * h, -6 * h, 4 * h * h]])
        idx = [2 * e, 2 * e + 1, 2 * e + 2, 2 * e + 3]
        K[np.ix_(idx, idx)] += k
    supports = np.concatenate([[0.0], np.cumsum(spans)])
    fixed = [2 * int(np.argmin(abs(x - s))) for s in supports]
    free = np.setdiff1d(np.arange(2 * n), fixed)
    return x, K, free


def influence_line(spans, xm, **kw):
    x, K, free = beam_fe(spans, **kw)
    F = np.zeros(2 * len(x))
    F[2 * int(np.argmin(abs(x - xm)))] = 1.0      # unit load at sensor
    u = np.zeros_like(F)
    u[free] = np.linalg.solve(K[np.ix_(free, free)], F[free])
    return x, u[0::2]                               # = eta_m(x) by Maxwell-Betti


def Cm(spans, xm, **kw):
    x, w = influence_line(spans, xm, **kw)
    return np.trapezoid(w, x), x, w


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
