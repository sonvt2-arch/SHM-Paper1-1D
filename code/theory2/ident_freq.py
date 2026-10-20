"""Package 1C, part 3 - mass model, vertical natural frequencies over the
(alpha, k) plane, overlay on the static misfit map, and what the measured
frequencies (N6 3.43, N7 3.64, N8 3.63 Hz; cau-may_span_dynamic_properties.csv)
can select.

Homogeneity: K = alpha K_g + k K_p, M = gamma M_base  =>
    f_i(alpha, k; gamma) = sqrt(alpha e_d / gamma) * f_i(1, kappa; 1),
with e_d = E_dynamic/E_static.  So frequencies are computed once along kappa.
Run after ident_static.py:  python3 code/theory2/ident_freq.py
"""
import os
import csv
import numpy as np
from ident_core import (Model, EI_law, mass_fn, MASS_CASES, SPANS, X_N8, X_N7,
                        X_N8MID, EI_MID, Logger, FIGD, LOGD, norm_index,
                        classify_mode, MEAS_MEAN, RHO_AS, W_CARR,
                        L_DIAPH_PIER, L_DIAPH_END, CM)
from ident_static import KAPPA, K_FE, admissible

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
F_MEAS = {}
with open(os.path.join(ROOT, "data", "bridges", "cau-may", "cau-may_span_dynamic_properties.csv")) as f:
    for row in csv.DictReader(l for l in f if not l.startswith("#")):
        F_MEAS[row["span"].split()[0]] = float(row["vertical_f_Hz"])
F_MAIN = np.array([F_MEAS["N6"], F_MEAS["N7"], F_MEAS["N8"]])
ED = (1.0, 1.2)            # E_dyn/E_static bracket (see doc, assumption D2)


def main():
    log = Logger("ident_freq.log")
    log("=== Measured vertical frequencies (CSV, acceptance-test report, Table 2.15) ===")
    log(", ".join(f"{k} {v:.2f} Hz" for k, v in F_MEAS.items()))
    log(f"main bridge N6/N7/N8: mean {F_MAIN.mean():.3f} Hz, sd {F_MAIN.std(ddof=1):.3f} Hz "
        f"({100*F_MAIN.std(ddof=1)/F_MAIN.mean():.1f} %), band [{F_MAIN.min():.2f}, {F_MAIN.max():.2f}]")

    EI = EI_law(44.0)[0]
    models, fh, kinds = {}, {}, {}
    log("\n=== Mass model (per metre; see doc table) ===")
    for case in MASS_CASES:
        mf, sdl = mass_fn(case)
        mod = Model(EI, mf, ne=5)
        models[case] = mod
        log(f"{case:5s}: {MASS_CASES[case]}; SDL {sdl:.3f} t/m; m(mid-span) {mf(np.array([100.0]))[0]:.2f} t/m, "
            f"m(pier face, h=5.4) {mf(np.array([55.0 + 1.6]))[0]:.2f} t/m; total {mod.mass_total:.0f} t "
            f"(mean {mod.mass_total/200:.2f} t/m)")
    gam = {c: models[c].mass_total / models["base"].mass_total for c in models}
    log("mass scale relative to base: " + ", ".join(f"{c} {v:.3f}" for c, v in gam.items()))
    # check ne=5 vs ne=10 for base
    m10 = Model(EI, mass_fn("base")[0], ne=10)
    f5, _ = models["base"].modes(K_FE, 1.0, 4)
    f10, _ = m10.modes(K_FE, 1.0, 4)
    log(f"mesh check (base, k_FE): ne=5 {np.round(f5,4).tolist()} ne=10 {np.round(f10,4).tolist()}")

    kap = KAPPA[::4]
    for case, mod in models.items():
        F, Kd = [], []
        for k in kap:
            f, V = mod.modes(k, 1.0, 5)
            F.append(f[:5])
            Kd.append([classify_mode(mod, V[:, i], k)[:2] for i in range(5)])
        fh[case] = np.array(F)
        kinds[case] = Kd
    log("\n=== f_i(alpha=1, kappa), base mass; mode type (S/A, span of max amplitude 0=N6,1=N7,2=N8) ===")
    for j in range(0, len(kap), 6):
        log(f"kappa={kap[j]:.2e}: " + "  ".join(f"f{i+1}={fh['base'][j,i]:.3f}{kinds['base'][j][i][0]}" for i in range(4)))
    # mode shapes and visibility at the three mid-span vibration points
    log("\n=== Mode-shape amplitude at the vibration points (mid N6 x=27.5, mid N7 x=100, mid N8 x=172.5), base, k_FE ===")
    f, V = models["base"].modes(K_FE, 1.0, 5)
    for i in range(5):
        t, sp_, w, amp = classify_mode(models["base"], V[:, i], K_FE)
        x = models["base"].x
        a = [np.interp(p, x, w) for p in (27.5, 100.0, 172.5)]
        mx = np.max(abs(w))
        log(f"mode {i+1}: f={f[i]:.3f} Hz {t}, |w|/max at N6/N7/N8 mid = "
            + "/".join(f"{abs(v)/mx:.2f}" for v in a))

    # which mode can be 3.4-3.6 Hz?
    log("\n=== Alpha needed for f_i = measured mean, sqrt(alpha e_d/gamma) f_i(1,kappa) = f_meas ===")
    fm = F_MAIN.mean()
    for i in range(3):
        for case in models:
            req = (fm / fh[case][:, i]) ** 2
            log(f"mode {i+1}, mass {case:4s}: alpha*e_d/gamma... alpha (e_d=1) needed over kappa range: "
                f"[{req.min():.3f}, {req.max():.3f}] (pinned->fixed: {req[0]:.3f} -> {req[-1]:.3f})")

    # ------------------------------------------- intersection with statics
    S = np.load(os.path.join(LOGD, "ident_static_scan.npz"))
    tau_rec = float(S["tau_rec"])
    r = {k.split("__")[1]: S[k] for k in S.files if k.startswith("Lv44__")}
    r["kappa"] = KAPPA
    lnf3 = {c: np.interp(np.log(KAPPA), np.log(kap), np.log(fh[c][:, 2])) for c in fh}
    lnf1 = {c: np.interp(np.log(KAPPA), np.log(kap), np.log(fh[c][:, 0])) for c in fh}
    lnf2 = {c: np.interp(np.log(KAPPA), np.log(kap), np.log(fh[c][:, 1])) for c in fh}

    def joint(tau, fband, ed_rng, cases, mode_ln, alpha_prior=None, nalpha=401):
        """Admissible (kappa, alpha) points: static max residual <= tau, and
        some (case, e_d) puts f_mode inside fband; optional prior on alpha."""
        pts = []
        for i, k in enumerate(KAPPA):
            da = tau - r["res"][i]
            if da < 0:
                continue
            for a in np.exp(np.linspace(r["lnalpha"][i] - da, r["lnalpha"][i] + da, nalpha)):
                if alpha_prior and not (alpha_prior[0] <= a <= alpha_prior[1]):
                    continue
                okf = False
                for c in cases:
                    for ed in np.linspace(ed_rng[0], ed_rng[1], 5):
                        fv = np.sqrt(a * ed) * np.exp(mode_ln[c][i])
                        if fband[0] <= fv <= fband[1]:
                            okf = True
                            break
                    if okf:
                        break
                if okf:
                    pts.append((i, a))
        return pts

    def summarize(pts, label):
        if not pts:
            log(f"{label}: EMPTY")
            return None
        ii = np.array([p[0] for p in pts]); aa = np.array([p[1] for p in pts])
        kk = KAPPA[ii]
        N8d = norm_index(r["C8"][ii] / aa, 55); N7d = norm_index(r["C7"][ii] / aa, 90)
        N8a = norm_index(r["C8"][ii], 55)
        out = dict(kappa=(kk.min(), kk.max()), alpha=(aa.min(), aa.max()), k=((kk * aa).min(), (kk * aa).max()),
                   N8d=(N8d.min(), N8d.max()), N7d=(N7d.min(), N7d.max()), N8a=(N8a.min(), N8a.max()),
                   R8=(r["R8"][ii].min(), r["R8"][ii].max()), R7=(r["R7"][ii].min(), r["R7"][ii].max()),
                   C8=((r["C8"][ii] / aa).min(), (r["C8"][ii] / aa).max()),
                   C7=((r["C7"][ii] / aa).min(), (r["C7"][ii] / aa).max()))
        log(f"{label}: kappa [{out['kappa'][0]:.2e},{out['kappa'][1]:.2e}] alpha [{out['alpha'][0]:.3f},{out['alpha'][1]:.3f}] "
            f"k [{out['k'][0]:.2e},{out['k'][1]:.2e}] | N8 design-ref [{out['N8d'][0]:.3f},{out['N8d'][1]:.3f}] "
            f"alpha-ref [{out['N8a'][0]:.3f},{out['N8a'][1]:.3f}] R8 [{out['R8'][0]:.3f},{out['R8'][1]:.3f}] | "
            f"N7 design-ref [{out['N7d'][0]:.3f},{out['N7d'][1]:.3f}] R7 [{out['R7'][0]:.3f},{out['R7'][1]:.3f}] | "
            f"C8 [{out['C8'][0]:.2e},{out['C8'][1]:.2e}] C7 [{out['C7'][0]:.2e},{out['C7'][1]:.2e}] m2/kN")
        return out

    log("\n=== Joint admissible sets (static tau and frequency) ===")
    fb = (F_MAIN.min(), F_MAIN.max())
    res = {}
    for tau in (0.05, tau_rec):
        T = f"tau={100*tau:.2f}%"
        res[(tau, "static")] = summarize(joint(tau, (0, 99), (1, 1), ["base"], lnf3), f"{T} static only")
        res[(tau, "prior")] = summarize(joint(tau, (0, 99), (1, 1), ["base"], lnf3, alpha_prior=(0.9, 1.3)),
                                        f"{T} static + prior alpha in [0.9,1.3]")
        res[(tau, "f3base")] = summarize(joint(tau, fb, (1, 1), ["base"], lnf3),
                                         f"{T} static + f3 in [{fb[0]},{fb[1]}] Hz, base mass, e_d=1")
        res[(tau, "f3wide")] = summarize(joint(tau, fb, ED, list(models), lnf3),
                                         f"{T} static + f3 in band, mass low..high, e_d 1.0..1.2")
        res[(tau, "f1wide")] = summarize(joint(tau, fb, ED, list(models), lnf1),
                                         f"{T} static + f1 in band (mode-1 hypothesis), mass low..high, e_d 1.0..1.2")
        res[(tau, "f2wide")] = summarize(joint(tau, (F_MEAS["N6"], F_MEAS["N8"]), ED, list(models), lnf2),
                                         f"{T} static + f2 in N6..N8 band (mode-2 hypothesis), mass low..high, e_d 1.0..1.2")
    # alpha implied by f3 at the static best fit along kappa
    log("\n=== Along the static valley alpha*(kappa): predicted f3 and f1 (base mass, e_d=1) ===")
    for kk in (1e7, K_FE, 5e7, 1e8, 1.679e8, 1e9):
        i = int(np.argmin(abs(np.log(KAPPA / kk))))
        a = np.exp(r["lnalpha"][i])
        log(f"kappa={KAPPA[i]:.2e}: alpha*={a:.3f}, static residual +-{100*r['res'][i]:.2f} %, "
            f"f1={np.sqrt(a)*np.exp(lnf1['base'][i]):.3f} f3={np.sqrt(a)*np.exp(lnf3['base'][i]):.3f} Hz "
            f"(low mass {np.sqrt(a)*np.exp(lnf3['low'][i]):.3f}, high {np.sqrt(a)*np.exp(lnf3['high'][i]):.3f})")
    np.savez(os.path.join(LOGD, "ident_freq_curves.npz"), kap=kap,
             **{f"f_{c}": fh[c] for c in fh}, gam=np.array([gam[c] for c in ("low", "base", "high")]))

    # ------------------------------------------- map figure
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    plt.rcParams.update({"font.size": 8.5})
    al = np.linspace(0.4, 1.6, 241)
    lk = np.linspace(6, 11, 251)
    A, LK = np.meshgrid(al, lk, indexing="xy")
    LKAP = LK - np.log10(A)
    m8, m7 = MEAS_MEAN["N8"], MEAS_MEAN["N7"]
    lp8 = np.interp(LKAP * np.log(10), np.log(KAPPA), np.log(r["p8"])) - np.log(A)
    lp7 = np.interp(LKAP * np.log(10), np.log(KAPPA), np.log(r["p7"])) - np.log(A)
    mis = np.maximum(abs(np.log(m8) - lp8), abs(np.log(m7) - lp7)) * 100
    fig, ax = plt.subplots(figsize=(6.8, 4.8), constrained_layout=True)
    cs = ax.contourf(A, LK, mis, levels=[0, 3, 4, 5, tau_rec * 100, 6, 8, 12, 20, 40], cmap="Greys_r", extend="max")
    cb = fig.colorbar(cs, ax=ax, format=matplotlib.ticker.FuncFormatter(
        lambda v, _: f"{v:.0f}" if abs(v - round(v)) < 1e-9 else f"{v:.2f}"))
    cb.set_label("static misfit max$_j$|ln(meas/pred)| (%)")
    cols = {"low": "#2a9d8f", "base": "#d0563b", "high": "#3b6fb6"}
    for c in ("low", "base", "high"):
        F3 = np.sqrt(A) * np.exp(np.interp(LKAP * np.log(10), np.log(KAPPA), lnf3[c]))
        cc = ax.contour(A, LK, F3, levels=list(fb), colors=cols[c], linewidths=1.1,
                        linestyles=["--", "-"])
        ax.clabel(cc, fmt=lambda v: f"f3={v:.2f}", fontsize=6)
        F1 = np.sqrt(A) * np.exp(np.interp(LKAP * np.log(10), np.log(KAPPA), lnf1[c]))
        if c == "base":
            c1 = ax.contour(A, LK, F1, levels=[1.4, 1.6, 1.8, 2.0], colors="#e9c46a", linewidths=0.7)
            ax.clabel(c1, fmt=lambda v: f"f1={v:.1f}", fontsize=6)
    ax.plot([1.0], [np.log10(K_FE)], "o", color="#d0563b", mfc="none", ms=6)
    ax.text(0.955, np.log10(K_FE) - 0.3, "A", color="#d0563b")
    ax.plot([1.088], [np.log10(K_FE)], "o", color="#d0563b", ms=4)
    ax.text(1.1, np.log10(K_FE) + 0.08, "A'", color="#d0563b")
    ax.plot([0.716], [np.log10(1.199e8)], "s", color="#3b6fb6", ms=5)
    ax.text(0.665, np.log10(1.199e8) - 0.3, "B", color="#3b6fb6")
    ax.plot(np.exp(r["lnalpha"]), np.log10(KAPPA * np.exp(r["lnalpha"])), color="w", lw=0.8, ls=":")
    ax.set_ylim(6, 11)
    ax.set_xlabel("$\\alpha = EI_{eff}/EI_{design}$")
    ax.set_ylabel("log$_{10}$ k (kN m/rad)")
    fig.savefig(os.path.join(FIGD, "ident_alpha_k_map.png"), dpi=200)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(6.4, 3.4), constrained_layout=True)
    for c, ls in (("low", ":"), ("base", "-"), ("high", "--")):
        for i, col in zip(range(3), ("k", "#3b6fb6", "#d0563b")):
            ax.semilogx(kap, fh[c][:, i], color=col, ls=ls, lw=1.0,
                        label=f"f{i+1}" if c == "base" else None)
    ax.axhspan(fb[0], fb[1], color="#2a9d8f", alpha=0.2, lw=0, label="measured band")
    ax.set_xlabel("$\\kappa = k/\\alpha$ (kN m/rad)")
    ax.set_ylabel("f (Hz) at $\\alpha$ = 1")
    for lab, ls in (("base mass", "-"), ("low mass", ":"), ("high mass", "--")):
        ax.plot([], [], color="0.4", ls=ls, lw=1.0, label=lab)
    ax.legend(fontsize=7, ncol=2, loc="lower right")
    fig.savefig(os.path.join(FIGD, "ident_freq_vs_kappa.png"), dpi=200)
    plt.close(fig)
    log.save()


if __name__ == "__main__":
    main()
