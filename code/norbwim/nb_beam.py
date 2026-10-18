"""Beam model of the Smart Road Bridge (5 spans 86.5+3x144+86.5 m, continuous).

Uses cm_multispan (imported, not modified). Euler-Bernoulli, uniform EI or parabolic
haunch (box depth 3.8 m at mid-span to 9.5 m at piers, dissertation Sec. 2.2.1),
I ~ h^n (n = 2 default, n = 2.5 sensitivity).
Outputs (all per unit load / unit EI_mid; only ratios and shapes are used):
  moment_il(xm)        : bending-moment influence line M_m(x) (sagging +)
  udl_moment()         : M_q(x) under unit uniform load on all spans (sagging +)
  top-fibre strain proxy: eps ~ -M h / I ~ -M / h^(n-1)  (compression negative)
"""
import os
import sys
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..",
                                                "analysis")))
import cm_multispan as cm  # noqa: E402

SPANS = [86.5, 144.0, 144.0, 144.0, 86.5]
LTOT = sum(SPANS)
EDGES = np.concatenate([[0.0], np.cumsum(SPANS)])
X_SENSOR = 86.5 + 72.0          # mid-span of span 2 ("144/2 m from piers")
H_MID, H_PIER = 3.8, 9.5


def model(haunch=True, n=2.0, ne=240):
    if haunch:
        EI = cm.haunch_EI(SPANS, H_MID, H_PIER, n=n)
        hfun = cm.haunch_depth(SPANS, H_MID, H_PIER)
        extra = cm.haunch_nodes(SPANS) + (X_SENSOR,)
    else:
        EI = lambda x: 1.0  # noqa: E731
        hfun = lambda x: H_MID  # noqa: E731
        extra = (X_SENSOR,)
    x, K, free, Fe = cm.beam_fe(SPANS, ne_per_span=ne, EI=EI, extra_nodes=extra,
                                ngauss=3, return_load=True)
    return dict(x=x, K=K, free=free, Fe=Fe, EI=EI, h=hfun, n=n, haunch=haunch)


def _curv(m, u):
    """Element-midpoint curvature (theta2-theta1)/h and EI -> moment (sign: sagging +
    checked by udl_moment on span 2)."""
    x = m["x"]
    h = np.diff(x)
    th = u[1::2]
    xm = 0.5 * (x[:-1] + x[1:])
    EIm = np.array([m["EI"](v) for v in xm])
    return xm, EIm * (th[1:] - th[:-1]) / h


def udl_moment(m):
    x = m["x"]
    F = np.zeros(2 * len(x))
    for e in range(len(x) - 1):
        F[2 * e:2 * e + 4] += m["Fe"][e]
    u = cm._solve(m["K"], m["free"], F)
    xm, M = _curv(m, u)
    # sign so that mid-span of span 2 is sagging (+)
    s = np.sign(np.interp(X_SENSOR, xm, M))
    return xm, s * M, s


def moment_il(m, xs=X_SENSOR):
    """M at xs for a unit vertical load at each node (multi-RHS solve)."""
    import scipy.sparse.linalg as spla
    import scipy.sparse as sps
    x, K, free = m["x"], m["K"], m["free"]
    Kff = K[free][:, free].tocsc()
    lu = spla.splu(Kff)
    n = len(x)
    e = int(np.searchsorted(x, xs) - 1)              # element containing xs
    e = min(max(e, 0), n - 2)
    il = np.zeros(n)
    # load vectors: unit force at vertical dof of node j
    idx = {d: k for k, d in enumerate(free)}
    B = np.zeros((len(free), n))
    for j in range(n):
        d = 2 * j
        if d in idx:
            B[idx[d], j] = 1.0
    U = lu.solve(B)
    full = np.zeros((2 * n, n))
    full[free] = U
    th1, th2 = full[2 * e + 1], full[2 * e + 3]
    hEl = x[e + 1] - x[e]
    EIe = m["EI"](0.5 * (x[e] + x[e + 1]))
    il = EIe * (th2 - th1) / hEl
    _, _, s = udl_moment(m)
    return x, s * il


def strain_proxy(m, xq, M):
    """Top-fibre strain ~ -M*y_t/I with y_t ~ h, I ~ h^n (EI normalised at h_mid)."""
    h = np.array([m["h"](v) for v in np.atleast_1d(xq)]) / H_MID
    return -M / h ** (m["n"] - 1.0)


def zero_moment_points(xm, M):
    s = np.sign(M)
    k = np.where(s[:-1] * s[1:] < 0)[0]
    return xm[k] - M[k] * (xm[k + 1] - xm[k]) / (M[k + 1] - M[k])


if __name__ == "__main__":
    for hn, n in [(False, 2.0), (True, 2.0), (True, 2.5)]:
        m = model(hn, n)
        xm, M, _ = udl_moment(m)
        z = zero_moment_points(xm, M)
        x, il = moment_il(m)
        area = np.trapezoid(il, x)
        Mq = np.interp(X_SENSOR, xm, M)
        print(f"haunch={hn} n={n}: M_q(sensor)={Mq:.2f}, int IL={area:.2f}, "
              f"zeros={np.round(z, 1)}")
