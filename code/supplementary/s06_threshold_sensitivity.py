"""Sensitivity of the near-blind bands to the indicator threshold (0.1, 0.2, 0.3).
Closed forms of Section 2.2 (Eqs. (4), (5), (9)); prismatic beams, gamma = 1."""
import numpy as np
from scipy.optimize import brentq

def F(xi, mu):
    return xi * (1 - 2 * xi**2 + xi**3) - mu / 2 * xi * (1 - xi**2)

mu2 = lambda lam: (1 + lam**3) / (1 + lam)            # two spans, gamma = 1
mu3 = lambda b: 2 * (1 + b**3) / (2 + 3 * b)          # symmetric three spans, gamma = 1

def band(f, t, lo, hi):
    """Interval around the blind root where |f| < t (f monotonic there)."""
    x = np.linspace(lo, hi, 20001); y = f(x)
    r = [brentq(lambda s: f(s) - c, x[i], x[i + 1])
         for c in (t, -t) for i in range(len(x) - 1) if (y[i] - c) * (y[i + 1] - c) < 0]
    return min(r), max(r)

print("threshold | strain, two equal spans: distance from interior support (fraction of span) "
      "| deflection, mid-span, two spans: lambda | deflection, mid side span, three spans: beta")
for t in (0.1, 0.2, 0.3):
    a, b = band(lambda xi: 3 * xi - 4 * xi**2, t, 0.5, 0.99)
    l1, l2 = band(lambda lam: 8 * F(0.5, mu2(lam)), t, 1.0, 2.0)
    b1, b2 = band(lambda be: 8 * F(0.5, mu3(be)), t, 1.2, 2.2)
    print(f"{t:.1f} | {1-b:.3f}-{1-a:.3f} | {l1:.3f}-{l2:.3f} | {b1:.3f}-{b2:.3f}")
