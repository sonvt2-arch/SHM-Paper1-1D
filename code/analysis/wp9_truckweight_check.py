"""WP9 - effect of the weighed Cau May test-truck mass (mean 25.06 t of the
10 weighed trucks, authors' answer 2026-10-18, docs/08_...MSSP.md) instead of
the nominal 25 t (5 + 10 + 10 t) used in WP3 (wp3_run.py, logs/wp3_run.log).

Run:  python3 code/analysis/wp9_truckweight_check.py
      (writes code/analysis/logs/wp9_truckweight_check.log; does not touch the
       WP3 result tables)

The per-axle split of the weighed trucks is not known, so all axle loads are
scaled by f = 25.06/25.  Base model varEI_Lv44 (as in the manuscript).

Scenario 0  nominal 25 t (reproduces wp3_run.log).
Scenario 1  models kept as calibrated with 25 t; only the predicted
            deflections are scaled by f (measured/model ratios divided by f).
Scenario 2  report-FE target assumed computed with 25 t (k_FE unchanged);
            calibration B and alpha at k_FE refitted to the measurements with
            25.06 t trucks.
Scenario 3  all calibrations refitted with 25.06 t (report FE assumed to use
            the weighed mass as well).
For every scenario: k_FE, alpha_B, k_B, alpha at k_FE, misfits, the
measured/model ratios of Table 6, and C_m, N_m, R_m of Table 5.
Part P      Truck-positioning error (authors' answer: positions marked with
            tape and paint, error < 20 cm in each direction): change of the
            predicted deflection at N8 and N7 when the whole convoy is shifted
            longitudinally by +/-0.20 m (models of scenario 0, 25.06 t).  The
            transverse error cannot be evaluated with the 1D model.
"""
import os
import sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import wp3_run as W                                    # noqa: E402
from wp3_fe import Bridge                              # noqa: E402

LOG = os.path.join(HERE, "logs", "wp9_truckweight_check.log")
out = []


def pr(*a):
    s = " ".join(str(x) for x in a)
    print(s)
    out.append(s)


F = 25.06 / 25.0
SENS = [("N8 0.4L", 178.0, 55.0, "CM_III_N8"), ("N7 mid", 100.0, 90.0, "CM_IV_N7")]
EIref = W.E_C45 * 5.482
_orig_truck = W.cm_truck


def set_mass(f):
    def truck(x_middle, facing=+1):
        xs, P = _orig_truck(x_middle, facing)
        return xs, P * f
    W.cm_truck = truck


def run(f_fe, f_meas):
    """Calibrate with axle loads scaled by f_fe for the report-FE fit and by
    f_meas for the fits to the measurements."""
    models = W.bridge_models()
    base = {k: v for k, v in models.items() if k[0] == "CM" and k[1] == "varEI_Lv44"}
    silent = lambda *a: None
    set_mass(f_fe)
    cal_fe = W.calibrate(dict(base), silent)
    set_mass(f_meas)
    cal_me = W.calibrate(dict(base), silent)
    mA = cal_fe[("CM", "varEI_Lv44", "kFE")]
    kFE = mA["k"]
    # refit alpha at the (possibly nominal) k_FE and keep calibration B from cal_me
    from scipy.optimize import minimize_scalar
    sch = W.all_schemes()
    me = np.array([np.mean(W.MEAS[k]["all"]) for _, _, k in W.PRIMARY["CM"]])
    spans = (55.0, 90.0, 55.0)

    def pred(alpha, k):
        b = Bridge(spans, lambda x: alpha * mA["EI"](x), k)
        return W.pred_primary(b, "CM", sch), b

    r3 = minimize_scalar(lambda la: (np.log(pred(np.exp(la), kFE)[0] / me) ** 2).sum(),
                         bounds=(-2, 2), method="bounded")
    a3 = np.exp(r3.x)
    mB = cal_me[("CM", "varEI_Lv44", "kMeas")]
    pA, bA = pred(1.0, kFE)
    pa3, _ = pred(a3, kFE)
    pB = W.pred_primary(mB["b"], "CM", sch)
    pr(f"  k_FE = {kFE:.4e}; alpha at k_FE = {a3:.4f} (misfit % "
       f"{np.round(100*(pa3/me-1),2).tolist()}); B: alpha = {mB['alpha']:.4f}, "
       f"k = {mB['k']:.4e} (misfit % {np.round(100*(pB/me-1),2).tolist()})")
    for i, (lab, xm, L, key) in enumerate(SENS):
        pr(f"  {lab}: model A = {pA[i]:.3f} mm, model B = {pB[i]:.3f} mm, "
           f"meas/A = {me[i]/pA[i]:.4f}, meas/B = {me[i]/pB[i]:.4f}")
    for cal, b in (("A", bA), ("B", mB["b"])):
        for lab, xm, L, key in SENS:
            c, pos, neg, _ = b.Cm(xm)
            pr(f"  {cal} {lab}: C_m = {c:.4e} m2/kN, N_m = {192*EIref*c/L**4:.4f}, "
               f"R_m = {c/pos:.4f}")
    return bA, mB["b"]


pr(f"Weighed mean truck mass 25.06 t vs nominal 25 t: factor f = {F:.6f} "
   f"(+{100*(F-1):.2f} %); axle loads scaled uniformly (split unknown)")
pr("\n=== Scenario 0: nominal 25 t (should reproduce wp3_run.log) ===")
models0 = run(1.0, 1.0)
pr("\n=== Scenario 1: models as calibrated with 25 t, loads x f ===")
pr("  measured/model ratios of scenario 0 divided by f: e.g. 0.977/f = "
   f"{0.977/F:.4f}, 0.890/f = {0.890/F:.4f}, 1.029/f = {1.029/F:.4f}, 0.972/f = {0.972/F:.4f}")
pr("\n=== Scenario 2: report FE with 25 t (k_FE fixed), measurement fits with 25.06 t ===")
run(1.0, F)
pr("\n=== Scenario 3: all fits with 25.06 t ===")
run(F, F)
pr("\n=== Part P: longitudinal shift of the convoy by +/-0.20 m (scenario-0 models, 25.06 t) ===")
set_mass(F)
sch = W.all_schemes()
for cal, b in zip(("A", "B"), models0):
    for lab, xm, L, key in SENS:
        eta = b.influence_line(xm)
        d0 = W.predict(b, eta, sch[key]["x"], sch[key]["P"]) * 1000
        line = f"  {cal} {lab}: d(0) = {d0:.3f} mm"
        for dx in (-0.20, 0.20):
            d = W.predict(b, eta, sch[key]["x"] + dx, sch[key]["P"]) * 1000
            line += f" | shift {dx:+.2f} m: {d:.3f} mm ({100*(d/d0-1):+.2f} %)"
        pr(line)
W.cm_truck = _orig_truck

os.makedirs(os.path.dirname(LOG), exist_ok=True)
with open(LOG, "w") as fh:
    fh.write("\n".join(out) + "\n")
