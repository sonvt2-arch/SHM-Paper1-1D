"""Package 1C, part 2 - static identifiability of (alpha, k) for Cau May and
the admissible range of the gauge indices over kappa = k/alpha.

Because K = alpha*K_g + k*K_p, every static prediction is
    y_j(alpha, k) = y_j(1, kappa) / alpha .
With alpha free, the best log-LS alpha for given kappa is
    ln alpha*(kappa) = mean_j ln(y_j(1,kappa)/y_j,meas)
and the residuals are +-ln(rho(kappa))/2, rho = (meas8/pred8)/(meas7/pred7).
A tolerance tau on max_j |ln(y_meas/y_pred)| therefore admits the kappa set
|ln rho(kappa)| <= 2 tau and, for each such kappa, the alpha interval
|ln alpha - ln alpha*| <= tau - |ln rho|/2.
Run: python3 code/theory2/ident_static.py
"""
import os
import numpy as np
from ident_core import (Model, EI_law, SPANS, X_N8, X_N7, X_N8MID, E, CM, EI_MID,
                        Logger, FIGD, LOGD, norm_index, static_pred, schemes,
                        MEAS_ALL, MEAS_MEAN, FE_REPORT)

KAPPA = np.logspace(6, 12, 241)
K_FE = 2.748e7                   # wp3_run.log, Lv = 44
TAUS = (0.03, 0.04, 0.05, 0.06, 0.08)


def variants():
    out = {}
    for Lv in (40.0, 44.0, 45.0):
        out[f"Lv{Lv:g}"] = EI_law(Lv)[0]
    for n in (2.5, 3.2):
        out[f"Lv44_n{n}"] = EI_law(44.0, n_override=n)[0]
    EI44 = EI_law(44.0)[0]
    sup = np.concatenate([[0.0], np.cumsum(SPANS)])

    def EIrz(x, half=1.5):
        x = np.asarray(x, float)
        d = np.minimum(abs(x - sup[1]), abs(x - sup[2]))
        return np.where(d < half, 100.0 * EI44(x), EI44(x))
    out["Lv44_rigid1.5"] = EIrz
    return out


def scan(model, kappas=KAPPA):
    sch = schemes()
    r = {k: [] for k in ("p8", "p7", "C8", "C7", "C8mid", "A8p", "A7p", "A8mp")}
    for k in kappas:
        p = static_pred(model, k, 1.0, sch)
        r["p8"].append(p["N8"]); r["p7"].append(p["N7"])
        for key, xm, ak in (("C8", X_N8, "A8p"), ("C7", X_N7, "A7p"), ("C8mid", X_N8MID, "A8mp")):
            c, pos, neg, eta, u = model.Cm_parts(xm, k)
            r[key].append(model.Cm(xm, k)); r[ak].append(pos)
    r = {k: np.array(v) for k, v in r.items()}
    m8, m7 = MEAS_MEAN["N8"], MEAS_MEAN["N7"]
    r["rho"] = (m8 / r["p8"]) / (m7 / r["p7"])
    r["lnalpha"] = 0.5 * (np.log(r["p8"] / m8) + np.log(r["p7"] / m7))
    r["res"] = 0.5 * abs(np.log(r["rho"]))
    r["R8"] = r["C8"] / r["A8p"]; r["R7"] = r["C7"] / r["A7p"]; r["R8mid"] = r["C8mid"] / r["A8mp"]
    r["kappa"] = kappas
    return r


def admissible(r, tau):
    ok = r["res"] <= tau
    if not ok.any():
        return None
    out = dict(kappa=(r["kappa"][ok].min(), r["kappa"][ok].max()))
    da = tau - r["res"][ok]
    amin = np.exp(r["lnalpha"][ok] - da)
    amax = np.exp(r["lnalpha"][ok] + da)
    out["alpha"] = (amin.min(), amax.max())
    out["k"] = ((r["kappa"][ok] * amin).min(), (r["kappa"][ok] * amax).max())
    for g, L in (("8", 55.0), ("7", 90.0), ("8mid", 55.0)):
        C1 = r["C" + g][ok]
        Nd = np.r_[norm_index(C1 / amin, L), norm_index(C1 / amax, L)]
        out["Ndesign" + g] = (Nd.min(), Nd.max())
        out["Nalpha" + g] = (norm_index(C1, L).min(), norm_index(C1, L).max())   # EI_ref = alpha EI_mid
        out["R" + g] = (r["R" + g][ok].min(), r["R" + g][ok].max())
        Ca = np.r_[C1 / amin, C1 / amax]
        out["C" + g] = (Ca.min(), Ca.max())
    out["n_ok"] = int(ok.sum())
    return out


def main():
    log = Logger("ident_static.log")
    m8, m7 = MEAS_MEAN["N8"], MEAS_MEAN["N7"]
    sem8 = MEAS_ALL["N8"].std(ddof=1) / np.sqrt(6) / m8
    sem7 = MEAS_ALL["N7"].std(ddof=1) / np.sqrt(6) / m7
    log("=== Measured static data (mean of 3 lines x 2 transverse cases) ===")
    log(f"N8: mean {m8:.4f} mm, sd {MEAS_ALL['N8'].std(ddof=1):.3f}, rel. SEM {100*sem8:.2f} %;  "
        f"N7: mean {m7:.4f} mm, sd {MEAS_ALL['N7'].std(ddof=1):.3f}, rel. SEM {100*sem7:.2f} %")
    sig_rho = np.hypot(sem8, sem7)
    log(f"rel. SEM of the ratio N8/N7: {100*sig_rho:.2f} %  (2 sigma = {200*sig_rho:.2f} %)")

    V = variants()
    scans = {}
    for name, EI in V.items():
        scans[name] = scan(Model(EI, None, ne=10))
    r = scans["Lv44"]
    # values quoted in the text
    log("\n=== Base model (Lv = 44 m): ratio misfit rho(kappa) = (meas/pred)_N8 / (meas/pred)_N7 ===")
    for kk in (1e7, K_FE, 1.199e8 / 0.716, 1e9, 1e12):
        i = int(np.argmin(abs(np.log(KAPPA / kk))))
        log(f"kappa={KAPPA[i]:.3e}: rho={r['rho'][i]:.4f}  alpha*={np.exp(r['lnalpha'][i]):.4f}  "
            f"residual +-{100*r['res'][i]:.2f} %  N8 index (EI_ref=alpha* EI_mid)={norm_index(r['C8'][i],55):.3f}"
            f"  N7 {norm_index(r['C7'][i],90):.3f}  R8={r['R8'][i]:.3f} R7={r['R7'][i]:.3f}")
    i0 = int(np.argmin(r["rho"]))
    from scipy.optimize import minimize_scalar
    mod44 = Model(V["Lv44"], None)
    sch = schemes()

    def rho_of(lk):
        p = static_pred(mod44, 10 ** lk, 1.0, sch)
        return (m8 / p["N8"]) / (m7 / p["N7"])
    opt = minimize_scalar(rho_of, bounds=(np.log10(KAPPA[i0 - 3]), np.log10(KAPPA[i0 + 3])), method="bounded")
    kmin, rmin = 10 ** opt.x, opt.fun
    p = static_pred(mod44, kmin, 1.0, sch)
    amin_ = np.sqrt(p["N8"] * p["N7"] / (m8 * m7))
    log(f"minimum ratio misfit rho_min = {rmin:.4f} at kappa = {kmin:.3e} kNm/rad (alpha* = {amin_:.3f}, "
        f"k = {kmin*amin_:.3e}); irreducible residual +-{50*np.log(rmin)*100/100:.2f} % per gauge")
    log(f"rho at fixed piers (kappa=1e12) = {r['rho'][-1]:.4f}; at kappa=1e6 = {r['rho'][0]:.4f}")
    # calibrations
    for lab, a, k in (("A (design EI, k_FE)", 1.0, K_FE), ("A' (alpha=1.088, k_FE)", 1.088, K_FE),
                      ("B (alpha=0.716, k=1.199e8)", 0.716, 1.199e8)):
        p = static_pred(mod44, k, a, sch)
        C8, C7, C8m = mod44.Cm(X_N8, k, a), mod44.Cm(X_N7, k, a), mod44.Cm(X_N8MID, k, a)
        c8 = mod44.Cm_parts(X_N8, k, a); c7 = mod44.Cm_parts(X_N7, k, a)
        log(f"calib {lab:28s}: pred N8 {p['N8']:.3f} N7 {p['N7']:.3f} mm; misfit (pred/meas-1) "
            f"{100*(p['N8']/m8-1):+.1f} / {100*(p['N7']/m7-1):+.1f} %; N8 index {norm_index(C8,55):.3f} "
            f"(EI_ref design), N8mid {norm_index(C8m,55):.3f}, N7 {norm_index(C7,90):.3f}; R8 {C8/c8[1]:.3f} "
            f"R7 {C7/c7[1]:.3f}; C8 {C8:.3e} C7 {C7:.3e} m2/kN")

    # model-form spread of the predicted ratio at fixed kappa
    lr = np.array([np.log(s["p8"] / s["p7"]) for s in scans.values()])
    spread = lr.max(0) - lr.min(0)
    log("\n=== Model-form variants (Lv 40/44/45, n 2.5/3.2, rigid pier zone +-1.5 m) ===")
    for name, s in scans.items():
        j = int(np.argmin(s["rho"]))
        log(f"{name:15s}: rho_min={s['rho'][j]:.4f} at kappa={KAPPA[j]:.2e}; N8 index range over kappa "
            f"[{norm_index(s['C8'],55).min():.3f}, {norm_index(s['C8'],55).max():.3f}] (EI_ref = alpha EI_mid)")
    jk = int(np.argmin(abs(np.log(KAPPA / K_FE)))); jb = int(np.argmin(abs(np.log(KAPPA / kmin))))
    log(f"spread of ln(pred8/pred7) across variants: at kappa=k_FE {100*spread[jk]:.2f} %, at kappa_min "
        f"{100*spread[jb]:.2f} %, max over kappa {100*spread.max():.2f} %")
    sig_model = spread[jb] / 2 / np.sqrt(2)     # half-range of ratio -> per-gauge 1 sigma (uniform-ish)
    sig_tot = np.hypot(np.hypot(sem8, sem7) / np.sqrt(2), sig_model)
    log(f"per-gauge sigma: measurement {100*np.hypot(sem8,sem7)/np.sqrt(2):.2f} %, model-form {100*sig_model:.2f} % "
        f"-> total {100*sig_tot:.2f} %;  recommended tolerance tau = 2 sigma = {200*sig_tot:.2f} %")
    tau_rec = 2 * sig_tot

    # admissible sets
    log("\n=== Admissible sets: max_j |ln(meas_j/pred_j)| <= tau, alpha and kappa free ===")
    log("columns: kappa range | alpha range | k range | N8 index (EI_ref design EI_mid) | N8 index (EI_ref alpha EI_mid) | R8 | N7 (design) | R7 | C8 | C7 (m2/kN)")
    adm = {}
    for tau in list(TAUS) + [tau_rec]:
        for name, s in scans.items():
            a = admissible(s, tau)
            if name == "Lv44" or tau in (0.05, tau_rec):
                if a is None:
                    log(f"tau={100*tau:.2f}% {name:15s}: EMPTY (rho_min not reached)")
                    continue
                log(f"tau={100*tau:.2f}% {name:15s}: kappa [{a['kappa'][0]:.2e},{a['kappa'][1]:.2e}] | alpha "
                    f"[{a['alpha'][0]:.3f},{a['alpha'][1]:.3f}] | k [{a['k'][0]:.2e},{a['k'][1]:.2e}] | N8d "
                    f"[{a['Ndesign8'][0]:.3f},{a['Ndesign8'][1]:.3f}] | N8a [{a['Nalpha8'][0]:.3f},{a['Nalpha8'][1]:.3f}]"
                    f" | R8 [{a['R8'][0]:.3f},{a['R8'][1]:.3f}] | N7d [{a['Ndesign7'][0]:.3f},{a['Ndesign7'][1]:.3f}]"
                    f" | R7 [{a['R7'][0]:.3f},{a['R7'][1]:.3f}] | C8 [{a['C8'][0]:.2e},{a['C8'][1]:.2e}] | C7 [{a['C7'][0]:.2e},{a['C7'][1]:.2e}]")
            adm[(tau, name)] = a
    # union over variants at tau_rec
    for tau in (0.05, tau_rec):
        al = [adm[(tau, n)] for n in scans if adm[(tau, n)] is not None]
        if al:
            u = lambda key: (min(a[key][0] for a in al), max(a[key][1] for a in al))
            log(f"UNION over variants, tau={100*tau:.2f}%: N8 design-ref [{u('Ndesign8')[0]:.3f},{u('Ndesign8')[1]:.3f}], "
                f"N8 alpha-ref [{u('Nalpha8')[0]:.3f},{u('Nalpha8')[1]:.3f}], R8 [{u('R8')[0]:.3f},{u('R8')[1]:.3f}], "
                f"N7 design-ref [{u('Ndesign7')[0]:.3f},{u('Ndesign7')[1]:.3f}], R7 [{u('R7')[0]:.3f},{u('R7')[1]:.3f}], "
                f"N8mid design-ref [{u('Ndesign8mid')[0]:.3f},{u('Ndesign8mid')[1]:.3f}], "
                f"alpha [{u('alpha')[0]:.3f},{u('alpha')[1]:.3f}], kappa [{u('kappa')[0]:.2e},{u('kappa')[1]:.2e}]")

    # Table 5 bound ordering
    log("\n=== Table 5 last column, re-ordered as pinned ... fixed (design EI, Lv 40/44/45) ===")
    for lab, xm, L in (("N8 0.4L", X_N8, 55.0), ("N8 mid", X_N8MID, 55.0), ("N7 mid", X_N7, 90.0)):
        pin = [norm_index(Model(V[f"Lv{Lv:g}"], None).Cm(xm, 0.0), L) for Lv in (40.0, 44.0, 45.0)]
        fix = [norm_index(Model(V[f"Lv{Lv:g}"], None).Cm(xm, 1e15), L) for Lv in (40.0, 44.0, 45.0)]
        log(f"{lab:8s}: pinned {min(pin):.3f}..{max(pin):.3f} (Lv44 {pin[1]:.3f}); fixed {min(fix):.3f}..{max(fix):.3f} "
            f"(Lv44 {fix[1]:.3f})")

    np.savez(os.path.join(LOGD, "ident_static_scan.npz"), kappa=KAPPA, tau_rec=tau_rec,
             **{f"{n}__{k}": v for n, s in scans.items() for k, v in s.items() if k != "kappa"})

    # ------------------------------------------------ figure
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    plt.rcParams.update({"font.size": 8.5})
    fig, axs = plt.subplots(2, 1, figsize=(6.6, 5.6), sharex=True, constrained_layout=True)
    ax = axs[0]
    for name, s in scans.items():
        ax.semilogx(KAPPA, s["rho"], color="k" if name == "Lv44" else "0.65", lw=1.4 if name == "Lv44" else 0.7)
    ax.axhline(1.0, color="k", lw=0.5)
    ax.axhspan(np.exp(-2 * tau_rec), np.exp(2 * tau_rec), color="#2a9d8f", alpha=0.15, lw=0,
               label=f"admissible band |ln $r_{{87}}$| $\\leq$ 2$\\tau$, $\\tau$ = {100*tau_rec:.1f} %")
    ax.axvline(K_FE, color="#d0563b", ls=":", lw=1); ax.text(K_FE, 1.13, " A", color="#d0563b")
    ax.axvline(1.199e8 / 0.716, color="#3b6fb6", ls=":", lw=1); ax.text(1.68e8, 1.13, " B", color="#3b6fb6")
    ax.set_ylabel("$r_{87}$ = (meas/pred)$_{N8}$ / (meas/pred)$_{N7}$")
    ax.set_ylim(0.98, 1.16)
    ax.plot([], [], color="0.65", lw=0.7, label="model-form variants")
    ax.legend(fontsize=7, loc="upper right")
    ax.set_title("(a) misfit ratio", fontsize=8, loc="left")
    ax = axs[1]
    ax.semilogx(KAPPA, norm_index(r["C8"], 55), "k", label="N8 $N_w$, $EI_\\mathrm{ref} = \\alpha EI_\\mathrm{mid}$")
    ax.semilogx(KAPPA, norm_index(r["C8"], 55) / np.exp(r["lnalpha"]), "k--", lw=0.9,
                label="N8 $N_w$, $EI_\\mathrm{ref}$ = design $EI_\\mathrm{mid}$, $\\alpha=\\alpha^*$")
    ax.semilogx(KAPPA, r["R8"], color="#d0563b", label="N8 $R$")
    ax.semilogx(KAPPA, norm_index(r["C7"], 90), color="#3b6fb6", label="N7 $N_w$, $EI_\\mathrm{ref} = \\alpha EI_\\mathrm{mid}$")
    ax.semilogx(KAPPA, r["R7"], color="#3b6fb6", ls="--", label="N7 $R$")
    ok = r["res"] <= tau_rec
    if ok.any():
        ax.axvspan(KAPPA[ok].min(), KAPPA[ok].max(), color="#2a9d8f", alpha=0.15, lw=0)
    ax.axhline(0.2, color="0.5", ls=":", lw=0.8)
    ax.set_xlabel("$\\kappa = k/\\alpha$ (kN m/rad)")
    ax.set_ylabel("indicator")
    ax.legend(fontsize=6, loc="center right", bbox_to_anchor=(1.0, 0.585), labelspacing=0.3,
              handlelength=1.6, borderpad=0.3)
    ax.set_title("(b) indicators along the best static fit $\\alpha^*(\\kappa)$", fontsize=8, loc="left")
    fig.savefig(os.path.join(FIGD, "ident_static_kappa_scan.png"), dpi=300)
    fig.savefig(os.path.join(FIGD, "ident_static_kappa_scan.pdf"))
    plt.close(fig)
    log.save()


if __name__ == "__main__":
    main()
