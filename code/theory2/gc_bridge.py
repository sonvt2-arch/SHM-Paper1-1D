"""Package 1A - Cau May (55+90+55 m) girder models, reusing the WP3 inputs
(code/analysis/wp3_fe.haunch_EI, unmodified; values as in manuscript Sec. 4.2 and
code/analysis/logs/wp3_run.log):
  E = 36 057 MPa, I_mid = 5.482 m^4, I_pier = 59.612 m^4, h 2.40 -> 5.40 m,
  parabolic depth over L_v = 44 m from each inner pier, I ~ h^n, n = 2.943.
Calibrations (rounded as printed in wp3_run.log):
  A: design EI, k = k_FE = 2.748e7 kN m/rad;  B: alpha = 0.716, k = 1.199e8.
Units kN, m.
"""
import os
import sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "analysis"))
from wp3_fe import haunch_EI  # noqa: E402  (reused, unmodified)

SPANS = (55.0, 90.0, 55.0)
E_C45 = 36.057e6
I_MID, I_PIER, H_MID, H_PIER, LV = 5.482, 59.612, 2.40, 5.40, 44.0
EI_MID = E_C45 * I_MID
K_FE, ALPHA_B, K_B = 2.748e7, 0.716, 1.199e8
BREAKS = (55.0 - LV, 55.0, 55.0 + LV, 145.0 - LV, 145.0, 145.0 + LV)
GAUGES = {"N8 0.4L (22 m from T8)": 178.0, "N8 mid side span": 172.5,
          "N7 mid main span": 100.0}


def _haunch():
    EI, h, n = haunch_EI(SPANS, E_C45, I_MID, I_PIER, H_MID, H_PIER, LV)
    return (lambda x: float(EI(x))), (lambda x: float(h(x))), n


def cases():
    EIh, h, n = _haunch()
    const = lambda x: EI_MID
    return {
        "prismatic, pinned": dict(EI=const, k=0.0, alpha=1.0),
        "haunched, pinned": dict(EI=EIh, k=0.0, alpha=1.0),
        "haunched, A (k_FE)": dict(EI=EIh, k=K_FE, alpha=1.0),
        "haunched, B (alpha 0.716, k 1.2e8)": dict(
            EI=(lambda x: ALPHA_B * EIh(x)), k=K_B, alpha=ALPHA_B),
        "haunched, fixed": dict(EI=EIh, k=np.inf, alpha=1.0),
    }


def depth():
    return _haunch()[1]


def exponent():
    return _haunch()[2]
