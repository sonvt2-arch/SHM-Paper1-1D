"""
04_parametric_study.py
======================
Section 4.5 of the revised paper.

  1. Numerical verification of the Maxwell-Betti corollary, Eq. (10):
         C_m = integral of the deflected shape produced by a UNIT STATIC
               LOAD applied at the measurement point
     against the closed form l^4 / (192 EI).

  2. Effect of the span ratio l2/l1 on the invariance constant, including
     the critical ratio at which C_m vanishes and the method fails.

  3. Effect of the sensor position along the instrumented span.

Run:  python3 04_parametric_study.py
"""

import numpy as np
from scipy.optimize import brentq

import beam_theory as bt

line = lambda t: print(('\n== %s ' % t).ljust(74, '='))


# --------------------------------------------------------------------------
line("1. Maxwell-Betti corollary, Eq. (10)")
# --------------------------------------------------------------------------
C_fe = bt.C_of(1.0, 1.0, 0.5, ei=1.0, nel=400)
C_cf = 1.0 ** 4 / 192.0
print("finite element  C_m = %.10f" % C_fe)
print("closed form     l^4/192EI = %.10f" % C_cf)
print("ratio                     = %.8f" % (C_fe / C_cf))
print("\n-> the invariance constant really is the area under the deflected")
print("   shape from a unit load at the sensor; on a bridge of unknown EI it")
print("   can therefore be obtained from ONE static calibration test.")


# --------------------------------------------------------------------------
line("2. Span ratio  (sensor at mid-span of span 1)")
# --------------------------------------------------------------------------
print("%8s %16s %14s" % ("l2/l1", "192 EI C_m / l1^4", "1 / C_m"))
for r in (0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.8, 2.0):
    c = bt.C_of(1.0, r, 0.5)
    print("%8.2f %16.4f %14s"
          % (r, 192 * c, "%.1f" % (1 / c) if abs(c) > 1e-6 else "singular"))

r_crit = brentq(lambda r: bt.C_of(1.0, r, 0.5), 1.3, 1.7)
print("\nCRITICAL SPAN RATIO  l2/l1 = %.4f   ->  C_m = 0, Eq. (12) singular"
      % r_crit)
print("Practical rule: instrument the LONGER span and keep the ratio of the")
print("adjacent span to the instrumented span comfortably below %.2f." % r_crit)


# --------------------------------------------------------------------------
line("3. Sensor position along span 1  (equal spans)")
# --------------------------------------------------------------------------
C_mid = bt.C_of(1.0, 1.0, 0.5)
print("%8s %16s %14s" % ("x_m / l", "192 EI C_m / l^4", "vs. mid-span"))
for xm in np.arange(0.10, 0.96, 0.05):
    c = bt.C_of(1.0, 1.0, xm)
    print("%8.2f %16.4f %13.3f" % (xm, 192 * c, c / C_mid))

xf = np.arange(0.30, 0.71, 0.01)
cf = np.array([bt.C_of(1.0, 1.0, v) for v in xf])
i = int(np.argmax(cf))
print("\noptimum at x_m/l = %.2f, only %+.1f %% above mid-span"
      % (xf[i], 100 * (cf[i] / C_mid - 1)))
print("-> mid-span instrumentation is very nearly optimal, and moderate")
print("   placement errors are harmless; placement near a support is not.")
