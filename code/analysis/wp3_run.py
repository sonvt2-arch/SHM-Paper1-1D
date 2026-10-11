"""WP3 - load-observability (C_m) and static consistency check for
Cau May (55+90+55 m) and Thai Binh (42+63+42 m) continuous box girders.

Run:  python3 code/analysis/wp3_run.py  (writes CSV tables, figures, log)
All inputs are listed in INPUTS with their source; see
docs/wp3_continuous_bridges.md.
"""
import os
import sys
import csv
import numpy as np

sys.path.insert(0, os.path.dirname(__file__))
from wp3_fe import Bridge, haunch_EI          # noqa: E402
from wp3_sections import thaibinh, caumay_mid, caumay_pier   # noqa: E402

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
RES = os.path.join(ROOT, "code", "analysis", "results")
FIG = os.path.join(ROOT, "figures")
os.makedirs(RES, exist_ok=True)
os.makedirs(FIG, exist_ok=True)
g = 9.81                     # kN per tonne
E_C45 = 36.057e6             # kN/m2; CM LRFR pdf p.4 (Ec = 36057 MPa, f'c 45);
                             # TB: same f'c = 45 MPa (TB design note, concrete table
                             # item 2) and same TCVN 11823 formula -> same Ec (derived)

# ------------------------------------------------------------------ inputs
TB_GROSS = np.array([31.020, 31.590, 29.200, 31.720, 31.220, 30.400, 30.500,
                     29.850, 29.220, 30.590])   # t, TB report 00 Bao cao, 'Tai trong'


def cm_truck(x_middle, facing=+1):
    """Cau May 3-axle truck (report sec 2.1.1.1): front 5 t, middle 10 t,
    rear 10 t; front-middle 3.60 m, middle-rear 1.35 m.  Returns axle
    positions and loads [t] given the middle-axle position."""
    xs = np.array([x_middle + facing * 3.60, x_middle, x_middle - facing * 1.35])
    return xs, np.array([5.0, 10.0, 10.0])


def tb_truck(x_axle3, facing=+1):
    """Thai Binh 4-axle truck (report 'Tai trong'): spacings 1.80/3.00/1.35 m
    (axle 1 = front).  Positions from axle 3 (front of rear tandem)."""
    return np.array([x_axle3 + facing * 4.80, x_axle3 + facing * 3.00,
                     x_axle3, x_axle3 - facing * 1.35])


def cm_schemes():
    """Longitudinal positions from test plan '06 - De cuong KDCL cau May.doc'
    sec V.4.3 (Hinh 14, 15; text rule) = report schemes III and IV.
    Two trucks side by side in each longitudinal row (report Hinh 2.6)."""
    L = 200.0
    out = {}
    # Scheme III (report) / II (plan): side span N8, 2 rows x 2 trucks,
    # middle axle of first row at 0.4L = 22 m from the end-pier axis (T8),
    # 6 m between rear axle of one truck and front axle of the next.
    d1 = 22.0
    xa, Pa = cm_truck(L - d1, facing=-1)         # facing into the span (towards T7)
    front1 = xa[0]
    xb, Pb = cm_truck(front1 - 6.0 - 1.35, facing=-1)  # rear axle of truck 2 = front1-6
    out["CM_III_N8"] = dict(x=np.r_[xa, xb], P=2 * np.r_[Pa, Pb], n=4)
    # Scheme IV (report) / III (plan): centre span N7, 3 rows x 2 trucks,
    # middle axle of row 2 at mid-span (x=100), 6 m clear axle gap.
    x2, P2 = cm_truck(100.0, +1)
    x1, P1 = cm_truck(x2[2] - 6.0 - 3.60, +1)    # front axle of truck1 = rear2 - 6
    x3, P3 = cm_truck(x2[0] + 6.0 + 1.35, +1)    # rear axle of truck3 = front2 + 6
    out["CM_IV_N7"] = dict(x=np.r_[x1, x2, x3], P=2 * np.r_[P1, P2, P3], n=6)
    return out


def tb_schemes():
    """Positions from TB report PDF (Drive 1J4YgdZ3y7lATFSOsgt7ZUXEHokAyLOCP)
    p.22-24, Hinh 8, 11, 12 (dimensions 16800 / 6000 printed; positions
    checked by pixel measurement at 600 dpi, scale 20.0 px/m)."""
    out = {}
    # Scheme 4, N12: axle 3 of the leading truck at 16.8 m from T11,
    # 6.0 m between front axle of the rear truck and rear axle of the leader.
    lead = tb_truck(16.8)
    rear = tb_truck((lead[3] - 6.0) - 4.80)     # rear truck axle1 = lead axle4 - 6
    out["TB_4_N12"] = dict(x=np.r_[rear, lead], n=4)
    # Scheme 5, N13: 3 trucks, middle truck axle 3 at mid-span (73.5 m),
    # pixel check gives 73.6 m; 6 m gaps.
    mid = tb_truck(73.5)
    t1 = tb_truck((mid[3] - 6.0) - 4.80)
    t3 = tb_truck((mid[0] + 6.0) + 1.35)
    out["TB_5_N13"] = dict(x=np.r_[t1, mid, t3], n=6)
    # Scheme 6, N14: front axle of the left truck at 16.8 m from T14
    # (x = 130.2), right truck rear axle 6 m further (x = 136.2).
    left = tb_truck(130.2 - 4.80)
    right = tb_truck(136.2 + 1.35)
    out["TB_6_N14"] = dict(x=np.r_[left, right], n=4)
    return out


# measured (axis line, centred / eccentric) and reported FE, mm downward
MEAS = {
    # cau-may_main_static_deflection.csv (04 - Do tinh - Cau chinh.xlsx, sheet V)
    "CM_III_N8": dict(axis=(5.56, 5.55), all=(5.32, 5.56, 5.76, 5.91, 5.55, 5.22), fe=5.934775),
    "CM_IV_N7": dict(axis=(15.24, 15.51), all=(14.68, 15.24, 15.83, 14.62, 15.51, 16.67), fe=16.703273),
    # thai_binh_main_bridge_static_deflection.csv (00 Bao cao, Bang 34)
    "TB_4_N12": dict(axis=(3.21, 3.22), all=(3.22, 3.21, 3.19, 3.28, 3.22, 3.15), fe=3.58),
    "TB_5_N13": dict(axis=(6.03, 6.03), all=(6.03, 6.03, 6.03, 6.04, 6.03, 6.01), fe=6.25),
    "TB_6_N14": dict(axis=(3.65, 3.61), all=(3.66, 3.65, 3.64, 3.68, 3.61, 3.54), fe=3.82),
}

# sensors: (label, x, scheme key, note)
CM_SENS = [("CM N8 0.4L (22 m from T8)", 178.0, "CM_III_N8", "plan V.4 / report 2.1.1.4c: 0.4L"),
           ("CM N8 mid-span (alt.)", 172.5, "CM_III_N8", "table label 'giua nhip N8'"),
           ("CM N7 mid-span", 100.0, "CM_IV_N7", "closure segment")]
TB_SENS = [("TB N12 mid-span", 21.0, "TB_4_N12", "report sec 5.3: mid-span"),
           ("TB N12 0.4L (alt.)", 16.8, "TB_4_N12", "plan: 0.4L; strain section 16.8 m"),
           ("TB N13 mid-span", 73.5, "TB_5_N13", ""),
           ("TB N14 mid-span", 126.0, "TB_6_N14", "report: mid-span"),
           ("TB N14 0.6L (alt.)", 130.2, "TB_6_N14", "16.8 m from T14")]


def bridge_models():
    """Returns dict of model variants per bridge."""
    models = {}
    # ---- Cau May: I from LRFR pdf p.5 (Iyy = vertical bending, z = depth axis)
    cm = dict(spans=(55.0, 90.0, 55.0), I_mid=5.482, I_pier=59.612,
              h_mid=2.40, h_pier=5.40)
    for Lv in (40.0, 44.0, 45.0):
        for kr, kname in ((0.0, "pinned"), (np.inf, "fixed")):
            EI, h, n = haunch_EI(cm["spans"], E_C45, cm["I_mid"], cm["I_pier"],
                                 cm["h_mid"], cm["h_pier"], Lv)
            models[("CM", f"varEI_Lv{Lv:g}", kname)] = dict(
                b=Bridge(cm["spans"], EI, kr), EI=EI, h=h, n=n, Lv=Lv,
                I_mid=cm["I_mid"], I_pier=cm["I_pier"])
    for kr, kname in ((0.0, "pinned"), (np.inf, "fixed")):
        EI = lambda x: E_C45 * cm["I_mid"] + 0 * x
        models[("CM", "constEI", kname)] = dict(b=Bridge(cm["spans"], EI, kr), EI=EI,
                                                I_mid=cm["I_mid"], I_pier=cm["I_mid"])
    # ---- Thai Binh: I from polygon (wp3_sections.thaibinh)
    tb_sec = {"tbot_CMabs": (0.25, 0.80), "tbot_CMprop": (0.21, 0.59)}
    for sname, (tm, tp) in tb_sec.items():
        Im = thaibinh(2.0, 5.759, 0.25, tm)[2]
        Ip = thaibinh(4.0, 4.80, 0.60, tp)[2]
        for Lv in (28.0, 30.5, 31.5):
            for kr, kname in ((0.0, "pinned"), (np.inf, "fixed")):
                EI, h, n = haunch_EI((42.0, 63.0, 42.0), E_C45, Im, Ip, 2.0, 4.0, Lv)
                models[("TB", f"varEI_{sname}_Lv{Lv:g}", kname)] = dict(
                    b=Bridge((42.0, 63.0, 42.0), EI, kr), EI=EI, h=h, n=n, Lv=Lv,
                    I_mid=Im, I_pier=Ip)
    Im = thaibinh(2.0, 5.759, 0.25, 0.25)[2]
    for kr, kname in ((0.0, "pinned"), (np.inf, "fixed")):
        EI = lambda x, Im=Im: E_C45 * Im + 0 * x
        models[("TB", "constEI", kname)] = dict(b=Bridge((42.0, 63.0, 42.0), EI, kr), EI=EI,
                                                I_mid=Im, I_pier=Im)
    return models


PRIMARY = {"CM": [("CM N8 0.4L (22 m from T8)", 178.0, "CM_III_N8"),
                  ("CM N7 mid-span", 100.0, "CM_IV_N7")],
           "TB": [("TB N12 mid-span", 21.0, "TB_4_N12"),
                  ("TB N13 mid-span", 73.5, "TB_5_N13"),
                  ("TB N14 mid-span", 126.0, "TB_6_N14")]}


def all_schemes():
    sch = {}
    for k, s in cm_schemes().items():
        sch[k] = dict(x=s["x"], P=s["P"] * g, n=s["n"], kind="CM")
    for k, s in tb_schemes().items():
        n_rows = len(s["x"]) // 4
        # baseline: mean gross, equal split over 4 axles, 2 trucks side by side
        P = np.full(len(s["x"]), 2 * TB_GROSS.mean() * g / 4)
        sch[k] = dict(x=s["x"], P=P, n=s["n"], kind="TB")
    return sch


def pred_primary(b, br, sch):
    out = []
    for lab, xm, key in PRIMARY[br]:
        eta = b.influence_line(xm)
        out.append(predict(b, eta, sch[key]["x"], sch[key]["P"]) * 1000)
    return np.array(out)


def calibrate(models, pr):
    """Pier rotational stiffness k (both inner piers) that makes the design-EI
    model reproduce the report FE deflections ('kFE'), and joint (alpha, k)
    fit to the measured deflections ('kMeas'; alpha = EI_eff / EI_design)."""
    from scipy.optimize import minimize_scalar, minimize
    sch = all_schemes()
    new = {}
    for (br, var, sup), m in list(models.items()):
        if sup != "pinned" or not var.startswith("varEI"):
            continue
        spans = tuple(m["b"].spans)
        fe = np.array([MEAS[k]["fe"] for _, _, k in PRIMARY[br]])
        me = np.array([np.mean(MEAS[k]["all"]) for _, _, k in PRIMARY[br]])

        def res_k(lk, target, alpha=1.0):
            EIa = lambda x: alpha * m["EI"](x)
            b = Bridge(spans, EIa, 10 ** lk)
            return np.log(pred_primary(b, br, sch) / target)

        r = minimize_scalar(lambda lk: (res_k(lk, fe) ** 2).sum(), bounds=(5, 13),
                            method="bounded")
        kFE = 10 ** r.x
        rf = res_k(r.x, fe)
        b = Bridge(spans, m["EI"], kFE)
        new[(br, var, "kFE")] = dict(m, b=b, k=kFE, alpha=1.0)
        r2 = minimize(lambda p: (res_k(p[1], me, np.exp(p[0])) ** 2).sum(),
                      x0=[0.0, r.x], method="Nelder-Mead",
                      options=dict(xatol=1e-6, fatol=1e-12, maxiter=4000))
        al, lk2 = np.exp(r2.x[0]), r2.x[1]
        rm = res_k(lk2, me, al)
        EIa = (lambda a: (lambda x: a * m["EI"](x)))(al)
        new[(br, var, "kMeas")] = dict(m, b=Bridge(spans, EIa, 10 ** lk2), EI=EIa,
                                       k=10 ** lk2, alpha=al)
        # alpha with k fixed at kFE (design support stiffness, EI scaled only)
        r3 = minimize_scalar(lambda la: (res_k(r.x, me, np.exp(la)) ** 2).sum(),
                             bounds=(-2, 2), method="bounded")
        a3 = np.exp(r3.x)
        rr3 = res_k(r.x, me, a3)
        pr(f"[calib] {br} {var}: k_FE = {kFE:.3e} kNm/rad (FE misfit % "
           f"{np.round(100*(np.exp(rf)-1),1).tolist()}); joint fit to measured: "
           f"alpha = EI_eff/EI_design = {al:.3f}, k = {10**lk2:.3e} (misfit % "
           f"{np.round(100*(np.exp(rm)-1),1).tolist()}); alpha at k_FE = {a3:.3f} "
           f"(misfit % {np.round(100*(np.exp(rr3)-1),1).tolist()})")
        new[(br, var, "kFE")]["alpha_at_kFE"] = a3
        new[(br, var, "kFE")]["misfit_FE"] = np.exp(rf) - 1
        new[(br, var, "kFE")]["misfit_meas_alpha"] = np.exp(rr3) - 1
    models.update(new)
    return models


BASE = {"CM": "varEI_Lv44", "TB": "varEI_tbot_CMabs_Lv30.5"}


def predict(b, eta, x_axles, P_kN):
    return sum(P * np.interp(xa, b.x, eta) for xa, P in zip(x_axles, P_kN))


def main():
    log = []
    pr = lambda *a: (print(*a), log.append(" ".join(str(s) for s in a)))
    models = bridge_models()
    models = calibrate(models, pr)

    # ---------------------------------------------------- section table log
    (A, zc, I), _ = caumay_mid()
    pr(f"[check] CM mid polygon: A={A:.3f} I={I:.3f} vs report A=7.233 Iyy=5.482")
    (A, zc, I), _ = caumay_pier()
    pr(f"[check] CM pier-face polygon: A={A:.3f} I={I:.3f} vs report A=14.437 Iyy=59.612")
    for k, m in models.items():
        if k[2] == "pinned" and "n" in m:
            pr(f"[model] {k[0]} {k[1]}: I_mid={m['I_mid']:.3f} I_pier={m['I_pier']:.3f}"
               f" n={m['n']:.3f} Lv={m['Lv']}")

    # ---------------------------------------------------- C_m table
    rows = []
    for (br, var, sup), m in models.items():
        sens = CM_SENS if br == "CM" else TB_SENS
        b = m["b"]
        for lab, xm, key, note in sens:
            c, pos, neg, eta = b.Cm(xm)
            i, L = b.span_of(xm)
            EIsec = float(m["EI"](np.array(xm)))
            EIs = E_C45 * m["I_mid"]           # EI_ref = mid-span (minimum) section
            # uniform-load check of Maxwell-Betti
            wq = np.interp(xm, b.x, b.uniform(1.0))
            rows.append(dict(bridge=br, model=var, pier=sup, sensor=lab, x_m=xm,
                             span_L_m=L, EI_sensor_section_kNm2=EIsec, EI_ref_kNm2=EIs, Cm_m2_per_kN=c,
                             Cm_uniform_check=wq,
                             norm_192EICm_L4=192 * EIs * c / L ** 4,
                             pos_area=pos, neg_area=neg, neg_over_pos=neg / pos, net_over_pos=c / pos,
                             near_blind=abs(192 * EIs * c / L ** 4) < 0.2))
    keys = list(rows[0].keys())
    with open(os.path.join(RES, "wp3_Cm_table.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, keys)
        w.writeheader()
        for r in rows:
            w.writerow({k: (f"{v:.6g}" if isinstance(v, float) else v) for k, v in r.items()})
    maxdev = max(abs(r["Cm_uniform_check"] / r["Cm_m2_per_kN"] - 1) for r in rows)
    pr(f"[check] max |C_m(IL area)/w(uniform) - 1| over all cases = {maxdev:.2e}")
    pr("\n=== Normalised C_m (192 EI_ref C_m / L^4), EI_ref = E I_mid (mid-span section) ===")
    for r in rows:
        if r["model"] in (BASE[r["bridge"]], "constEI"):
            pr(f"{r['bridge']} {r['model']:26s} {r['pier']:6s} {r['sensor']:28s} "
               f"norm={r['norm_192EICm_L4']:7.3f} neg/pos={r['neg_over_pos']:7.3f} "
               f"{'NEAR-BLIND' if r['near_blind'] else ''}")
    # ranges over all variable-EI variants
    pr("\n=== Range of normalised C_m over all variable-EI variants (Lv, t_bot, pier fixity) ===")
    summ = []
    for br, sens in (("CM", CM_SENS), ("TB", TB_SENS)):
        for lab, *_ in sens:
            vals = [r for r in rows if r["bridge"] == br and r["sensor"] == lab
                    and r["model"].startswith("varEI") and r["pier"] != "kMeas"]
            v = np.array([r["norm_192EICm_L4"] for r in vals])
            npr = np.array([r["neg_over_pos"] for r in vals])
            base = [r for r in vals if r["model"] == BASE[br]]
            bp = [r for r in base if r["pier"] == "pinned"][0]
            bf = [r for r in base if r["pier"] == "fixed"][0]
            bk = [r for r in base if r["pier"] == "kFE"][0]
            ce = [r for r in rows if r["bridge"] == br and r["sensor"] == lab
                  and r["model"] == "constEI" and r["pier"] == "pinned"][0]
            pr(f"{lab:30s} base kFE {bk['norm_192EICm_L4']:.3f} (neg/pos {bk['neg_over_pos']:.3f}) | base pinned {bp['norm_192EICm_L4']:.3f} | base fixed "
               f"{bf['norm_192EICm_L4']:.3f} | range [{v.min():.3f}, {v.max():.3f}] | "
               f"constEI pinned {ce['norm_192EICm_L4']:.3f} | neg/pos range "
               f"[{npr.min():.3f}, {npr.max():.3f}]")
            summ.append(dict(bridge=br, sensor=lab,
                             norm_constEI_pinned=ce["norm_192EICm_L4"],
                             norm_base_kFE=bk["norm_192EICm_L4"],
                             negpos_base_kFE=bk["neg_over_pos"],
                             netpos_base_kFE=bk["net_over_pos"],
                             netpos_min=min(r["net_over_pos"] for r in vals),
                             netpos_max=max(r["net_over_pos"] for r in vals),
                             Cm_base_kFE_m2_per_kN=bk["Cm_m2_per_kN"],
                             norm_base_pinned=bp["norm_192EICm_L4"],
                             norm_base_fixed=bf["norm_192EICm_L4"],
                             norm_min=v.min(), norm_max=v.max(),
                             negpos_base_pinned=bp["neg_over_pos"],
                             negpos_base_fixed=bf["neg_over_pos"],
                             Cm_base_pinned_m2_per_kN=bp["Cm_m2_per_kN"],
                             Cm_base_fixed_m2_per_kN=bf["Cm_m2_per_kN"],
                             near_blind_any=bool((abs(v) < 0.2).any()),
                             near_blind_all=bool((abs(v) < 0.2).all())))
    with open(os.path.join(RES, "wp3_Cm_summary.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, list(summ[0].keys()))
        w.writeheader()
        for r in summ:
            w.writerow({k: (f"{v:.4g}" if isinstance(v, float) else v) for k, v in r.items()})

    # ---------------------------------------------------- load tests
    pr("\n=== Static load-test consistency check ===")
    schemes = {}
    for k, s in cm_schemes().items():
        schemes[k] = dict(x=s["x"], P=s["P"] * g, n=s["n"], kind="CM")
    tbs = tb_schemes()
    for k, s in tbs.items():
        schemes[k] = dict(x=s["x"], n=s["n"], kind="TB")
    for k, s in schemes.items():
        pr(f"[positions] {k}: axles x = {np.round(np.sort(s['x']), 2).tolist()}")
    lt_rows = []
    for (br, var, sup), m in models.items():
        b = m["b"]
        sens = CM_SENS if br == "CM" else TB_SENS
        for lab, xm, key, note in sens:
            s = schemes[key]
            eta = b.influence_line(xm)
            if br == "CM":
                d = predict(b, eta, s["x"], s["P"]) * 1000
                dlo = dhi = d
                W = s["P"].sum() / g
            else:
                n = s["n"]
                Wbar = TB_GROSS.mean()
                srt = np.sort(TB_GROSS)
                # 2 trucks side by side per longitudinal position
                ntr = len(s["x"]) // 4
                xs = s["x"].reshape(ntr, 4)
                il = np.interp(xs, b.x, eta)
                d = (2 * Wbar * g * il.mean(axis=1).sum()) * 1000   # equal axle split
                # hard bounds: lightest/heaviest trucks, gross on min/max-IL axle
                dlo = (srt[:n].sum() / n) * 2 * g * il.min(axis=1).sum() * 1000
                dhi = (srt[-n:].sum() / n) * 2 * g * il.max(axis=1).sum() * 1000
                W = n * Wbar
            me = MEAS[key]
            lt_rows.append(dict(bridge=br, model=var, pier=sup, sensor=lab, scheme=key,
                                n_trucks=s["n"], W_total_t=W, pred_mm=d,
                                pred_lo_mm=dlo, pred_hi_mm=dhi,
                                meas_axis_centred_mm=me["axis"][0],
                                meas_axis_eccentric_mm=me["axis"][1],
                                meas_mean6_mm=np.mean(me["all"]), report_FE_mm=me["fe"],
                                meas_over_pred=np.mean(me["all"]) / d,
                                FE_over_pred=me["fe"] / d,
                                meas_over_reportFE=np.mean(me["all"]) / me["fe"]))
    with open(os.path.join(RES, "wp3_loadtest_table.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, list(lt_rows[0].keys()))
        w.writeheader()
        for r in lt_rows:
            w.writerow({k: (f"{v:.4g}" if isinstance(v, float) else v) for k, v in r.items()})
    pr("(pred = this 2D model; meas = mean of 3 lines x 2 transverse cases)")
    for r in lt_rows:
        if r["model"] in (BASE[r["bridge"]], "constEI"):
            pr(f"{r['model']:26s} {r['pier']:6s} {r['sensor']:28s} W={r['W_total_t']:6.1f} t "
               f"pred={r['pred_mm']:6.2f} [{r['pred_lo_mm']:.2f},{r['pred_hi_mm']:.2f}] "
               f"meas={r['meas_mean6_mm']:6.2f} FE_rep={r['report_FE_mm']:6.2f} "
               f"meas/pred={r['meas_over_pred']:.3f} FE/pred={r['FE_over_pred']:.3f}")
    pr("\n=== meas/pred range over all variable-EI variants (primary sensors) ===")
    primary = ["CM N8 0.4L (22 m from T8)", "CM N7 mid-span", "TB N12 mid-span",
               "TB N13 mid-span", "TB N14 mid-span"]
    lsum = []
    for lab in primary:
        v = [r for r in lt_rows if r["sensor"] == lab and r["model"].startswith("varEI")
             and r["pier"] in ("pinned", "fixed", "kFE")]
        mp = np.array([r["meas_over_pred"] for r in v])
        fp = np.array([r["FE_over_pred"] for r in v])
        bp = [r for r in v if r["model"] == BASE[r["bridge"]] and r["pier"] == "pinned"][0]
        bf = [r for r in v if r["model"] == BASE[r["bridge"]] and r["pier"] == "fixed"][0]
        bk = [r for r in v if r["model"] == BASE[r["bridge"]] and r["pier"] == "kFE"][0]
        mk = models[(bk["bridge"], BASE[bk["bridge"]], "kFE")]
        vk = [r for r in v if r["pier"] == "kFE"]
        mpk = np.array([r["meas_over_pred"] for r in vk])
        pr(f"{lab:28s} kFE: pred {bk['pred_mm']:.2f} mm, FE/pred {bk['FE_over_pred']:.3f}, meas/pred {bk['meas_over_pred']:.3f} (variants [{mpk.min():.3f},{mpk.max():.3f}]); alpha(EIeff/EIdesign at k_FE) {mk['alpha_at_kFE']:.3f}")
        pr(f"{lab:28s} meas/pred base pinned {bp['meas_over_pred']:.3f}, fixed "
           f"{bf['meas_over_pred']:.3f}; range [{mp.min():.3f},{mp.max():.3f}]; "
           f"FE/pred range [{fp.min():.3f},{fp.max():.3f}]; meas/FE_report "
           f"{bp['meas_over_reportFE']:.3f}")
        lsum.append(dict(sensor=lab, n_trucks=bp["n_trucks"], W_total_t=bp["W_total_t"],
                         meas_mean_mm=bp["meas_mean6_mm"], report_FE_mm=bp["report_FE_mm"],
                         k_FE_kNm_per_rad=mk["k"], pred_base_kFE_mm=bk["pred_mm"],
                         FE_over_pred_kFE=bk["FE_over_pred"],
                         meas_over_pred_kFE=bk["meas_over_pred"],
                         meas_over_pred_kFE_variants_min=mpk.min(),
                         meas_over_pred_kFE_variants_max=mpk.max(),
                         alpha_EIeff_over_EIdesign_at_kFE=mk["alpha_at_kFE"],
                         pred_base_pinned_mm=bp["pred_mm"], pred_base_fixed_mm=bf["pred_mm"],
                         pred_lo_mm=min(r["pred_lo_mm"] for r in v),
                         pred_hi_mm=max(r["pred_hi_mm"] for r in v),
                         meas_over_pred_pinned=bp["meas_over_pred"],
                         meas_over_pred_fixed=bf["meas_over_pred"],
                         meas_over_pred_min=mp.min(), meas_over_pred_max=mp.max(),
                         meas_over_reportFE=bp["meas_over_reportFE"],
                         EIeff_over_EIreportFE=1 / bp["meas_over_reportFE"],
                         meas_per_tonne_mm=bp["meas_mean6_mm"] / bp["W_total_t"]))
    with open(os.path.join(RES, "wp3_loadtest_summary.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, list(lsum[0].keys()))
        w.writeheader()
        for r in lsum:
            w.writerow({k: (f"{v:.4g}" if isinstance(v, float) else v) for k, v in r.items()})

    # linearity / proportionality (different spans: only a per-span C_eff check)
    pr("\n=== Load proportionality: deflection per tonne and per unit of sum(P*eta) ===")
    for r in lsum:
        pr(f"{r['sensor']:28s} n={r['n_trucks']:2d} W={r['W_total_t']:6.1f} t "
           f"meas/W={r['meas_per_tonne_mm']:.4f} mm/t  meas/FE_report={r['meas_over_reportFE']:.3f}")

    figures(models, schemes)
    with open(os.path.join(ROOT, "code", "analysis", "logs", "wp3_run.log"), "w") as f:
        f.write("\n".join(log) + "\n")


def figures(models, schemes):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    plt.rcParams.update({"font.size": 9})
    panels = [("CM", CM_SENS[0]), ("CM", CM_SENS[2]),
              ("TB", TB_SENS[0]), ("TB", TB_SENS[2]), ("TB", TB_SENS[3])]
    fig, axs = plt.subplots(len(panels), 1, figsize=(7.0, 10.0), constrained_layout=True)
    for ax, (br, (lab, xm, key, note)) in zip(axs, panels):
        mk = models[(br, BASE[br], "kFE")]
        EIr = E_C45 * mk["I_mid"]
        b = mk["b"]
        i, L = b.span_of(xm)
        c, pos, neg, eta = b.Cm(xm)
        e = eta * EIr / L ** 3
        ax.fill_between(b.x, 0, e, where=e >= 0, color="#3b6fb6", alpha=0.45, lw=0,
                        label="positive area")
        ax.fill_between(b.x, 0, e, where=e < 0, color="#d0563b", alpha=0.6, lw=0,
                        label="negative area")
        ax.plot(b.x, e, color="#1d3557", lw=1.2, label="pier k = k$_{FE}$ (calibrated)")
        out = [f"{192 * EIr * c / L ** 4:.3f} (k$_{{FE}}$)"]
        for sup, ls, col in (("pinned", ":", "0.35"), ("fixed", "--", "k")):
            mm = models[(br, BASE[br], sup)]
            cc, pp, nn, ee = mm["b"].Cm(xm)
            ax.plot(mm["b"].x, ee * EIr / L ** 3, color=col, lw=0.9, ls=ls,
                    label=f"pier {sup}")
            out.append(f"{192 * EIr * cc / L ** 4:.3f} ({sup})")
        for sx in b.sup:
            ax.axvline(sx, color="0.6", lw=0.6)
        ax.axvline(xm, color="#2a9d8f", lw=1.0, ls="-.")
        ax.axhline(0, color="k", lw=0.5)
        ax.set_title(f"{lab}: 192EI$_{{ref}}$C$_m$/L$^4$ = " + ", ".join(out)
                     + f"; C$_m$/A$^+$ = {c/pos:.2f}", fontsize=8)
        ax.set_ylabel(r"$\eta\,EI_{ref}/L^3$")
        ax.set_xlim(b.sup[0], b.sup[-1])
    axs[0].legend(fontsize=7, ncol=3, loc="lower left")
    axs[-1].set_xlabel("x along the continuous unit (m); dash-dot = sensor")
    fig.savefig(os.path.join(FIG, "wp3_influence_lines.png"), dpi=200)
    plt.close(fig)

    rows = list(csv.DictReader(open(os.path.join(RES, "wp3_Cm_summary.csv"))))
    labs = [r["sensor"] for r in rows]
    f_ = lambda k: np.array([float(r[k]) for r in rows])
    vk, vp, vf, lo, hi, ce = (f_("norm_base_kFE"), f_("norm_base_pinned"),
                              f_("norm_base_fixed"), f_("norm_min"), f_("norm_max"),
                              f_("norm_constEI_pinned"))
    y = np.arange(len(labs))
    fig, ax = plt.subplots(figsize=(7.0, 5.0), constrained_layout=True)
    ax.barh(y, vk, 0.55, color="#3b6fb6", label="variable EI, pier k$_{FE}$ (best estimate)")
    ax.errorbar((lo + hi) / 2, y, xerr=(hi - lo) / 2, fmt="none", ecolor="k", capsize=3,
                lw=0.8, label="range: pinned...fixed, all geometry variants")
    ax.plot(ce, y, "D", color="#d0563b", ms=4, label="constant EI, pinned (WP2 style)")
    ax.axvline(0.2, color="#d0563b", ls="--", lw=1)
    ax.axvline(0.0, color="k", lw=0.5)
    ax.text(0.205, len(labs) - 0.45, "near-blind threshold 0.2", color="#d0563b", fontsize=7.5)
    ax.set_yticks(y)
    ax.set_yticklabels(labs)
    ax.invert_yaxis()
    ax.set_xlabel(r"$192\,EI_{ref}\,C_m/L^4$  (EI$_{ref}$ = mid-span section, L = sensor span)")
    ax.legend(fontsize=7, loc="upper center", bbox_to_anchor=(0.45, -0.13), ncol=2)
    fig.savefig(os.path.join(FIG, "wp3_Cm_normalised_bar.png"), dpi=200)
    plt.close(fig)

    fig, axs = plt.subplots(1, 2, figsize=(7.0, 2.6), constrained_layout=True)
    for ax, br in zip(axs, ("CM", "TB")):
        m = models[(br, BASE[br], "pinned")]
        b = m["b"]
        ax.plot(b.x, m["EI"](b.x) / (E_C45 * m["I_mid"]), "k")
        ax.set_title(f"{'Cau May' if br == 'CM' else 'Thai Binh'}: EI(x)/EI$_{{mid}}$ "
                     f"(n={m['n']:.2f}, Lv={m['Lv']:g} m)", fontsize=8.5)
        ax.set_xlabel("x (m)")
        for sx in b.sup:
            ax.axvline(sx, color="0.6", lw=0.6)
    fig.savefig(os.path.join(FIG, "wp3_EI_profiles.png"), dpi=200)
    plt.close(fig)


if __name__ == "__main__":
    main()
