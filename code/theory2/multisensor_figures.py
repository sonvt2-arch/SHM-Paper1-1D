"""Package 1B - figures (PNG 300 dpi + PDF) from the theory/placement/MC outputs.
Run after multisensor_theory.py, multisensor_placement.py, multisensor_mc.py.
"""
import csv
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker
import multisensor_core as mc

plt.rcParams.update({"font.size": 8, "axes.titlesize": 8, "axes.labelsize": 8,
                     "legend.fontsize": 7, "xtick.labelsize": 7, "ytick.labelsize": 7,
                     "axes.spines.top": False, "axes.spines.right": False})
COL = {"single": "#7f7f7f", "gls": "#1f5fa8", "immune": "#c8502a", "aux": "#2a9d55"}


def save(fig, name):
    fig.savefig(f"{mc.FIGS}/{name}.png", dpi=300, bbox_inches="tight")
    fig.savefig(f"{mc.FIGS}/{name}.pdf", bbox_inches="tight")
    plt.close(fig)


# ---------------------------------------------------------------- Fig 1: C(x)
PM = mc.prismatic_models()
CM = mc.caumay_models()
fig, axs = plt.subplots(2, 3, figsize=(7.2, 4.0))
items = [("2S-eq", PM), ("2S-r2", PM), ("3S-b1.4", PM), ("3S-b2.0", PM), ("CM-A", CM), ("CM-B", CM)]
for ax, (key, d) in zip(axs.ravel(), items):
    m = d[key]
    ax.axhline(0, color="k", lw=0.5)
    ax.plot(m.x, m.Cd, color=COL["gls"], lw=1.2)
    for s in m.supports:
        ax.plot(s, 0, marker="^", color="k", ms=4, clip_on=False)
    i1, i0 = int(np.argmax(m.Cd)), int(np.argmin(m.Cd))
    ax.plot(m.x[i1], m.Cd[i1], "o", color=COL["gls"], ms=5)
    ax.plot(m.x[i0], m.Cd[i0], "s", color=COL["immune"], ms=5)
    ax.annotate(f"max {m.x[i1]:.1f} m", (m.x[i1], m.Cd[i1]), xytext=(3, -10),
                textcoords="offset points", fontsize=6.5)
    ax.annotate(f"min {m.x[i0]:.1f} m", (m.x[i0], m.Cd[i0]), xytext=(3, 4),
                textcoords="offset points", fontsize=6.5, color=COL["immune"])
    ax.set_title(m.name, loc="left")
    ax.set_xlabel("sensor position x (m)")
    ax.set_ylabel(r"$C(x)$ (mm m/kN)")
fig.tight_layout()
save(fig, "ms_fig1_Cx_extremes")

# ---------------------------------------------------------------- Fig 2: placement gains
rows = list(csv.DictReader(open(f"{mc.RES}/placement_vertex.csv")))
fig, axs = plt.subplots(1, 3, figsize=(7.2, 3.6))
ax = axs[0]
mk = {"2S-eq": "o", "3S-b2.0": "s", "CM-A": "^", "CM-B": "v"}
for key in mk:
    for k, ls in ((2, "-"), (3, "--")):
        r = [x for x in rows if x["model"] == key and x["types"] == "d" and float(x["sig"]) == 0.01
             and float(x["eps"]) == 0.1 and int(x["k"]) == k and x["est"] == "gls"]
        rh = [float(x["rho"]) for x in r]
        ax.semilogy(rh, [float(x["ratio"]) for x in r], ls, marker=mk[key], ms=3.5, lw=1,
                    label=f"{key}, k = {k}")
ax.set_xlabel(r"common-mode fraction $\rho$")
ax.set_ylabel(r"Var$_k$/Var$_1$ (GLS)")
ax.set_title("(a) gain over the best single sensor", loc="left")
ax.legend(ncol=2, fontsize=5.5, frameon=False, loc="lower left")
ax = axs[1]
for key, c in (("CM-A", COL["gls"]), ("2S-eq", COL["aux"])):
    for rho, ls in ((0.0, ":"), (0.9, "-"), (1.0, "--")):
        for est, lab in (("gls", "GLS-3"),):
            r = [x for x in rows if x["model"] == key and x["types"] == "d" and
                 float(x["sig"]) == 0.01 and float(x["rho"]) == rho and int(x["k"]) == 3
                 and x["est"] == est]
            ax.loglog([float(x["eps"]) for x in r], [float(x["std_pct"]) for x in r], ls,
                      color=c, lw=1, label=f"{key}, k = 3, $\\rho$ = {rho}")
    r = [x for x in rows if x["model"] == key and x["types"] == "d" and float(x["sig"]) == 0.01
         and float(x["rho"]) == 0.0 and int(x["k"]) == 1]
    ax.loglog([float(x["eps"]) for x in r], [float(x["std_pct"]) for x in r], "-", color=c,
              lw=2.2, alpha=0.35, label=f"{key}, single sensor")
ax.set_xlabel(r"offset std $\delta_0$ (mm)")
ax.set_xticks([0.02, 0.05, 0.1, 0.2, 0.5])
ax.set_xticklabels(["0.02", "0.05", "0.1", "0.2", "0.5"])
ax.xaxis.set_minor_formatter(matplotlib.ticker.NullFormatter())
ax.set_ylabel(r"std of $\hat P$ (% of P)")
ax.set_title(r"(b) $\sigma$ = 0.01 mm", loc="left")
ax.legend(fontsize=5.6, frameon=False, ncol=2, loc="upper center", bbox_to_anchor=(0.5, -0.28))
ax = axs[2]
t3 = list(csv.DictReader(open(f"{mc.RES}/T3_immune.csv")))
for key, c in (("2S-eq", COL["aux"]), ("3S-b2.0", COL["immune"]), ("CM-A", COL["gls"])):
    r = [x for x in t3 if x["model"] == key and float(x["eps_mm"]) == 0.1 and float(x["rho"]) == 1.0]
    ax.plot([float(x["sig_mm"]) for x in r], [float(x["std_immune2_pct"]) for x in r], "-o",
            color=c, ms=3, lw=1, label=f"{key} zero-sum pair")
ax.set_xlabel(r"white noise $\sigma$ (mm)")
ax.set_ylabel(r"std of $\hat P$ (% of P)")
ax.set_title(r"(c) $\rho$ = 1: zero-sum pair", loc="left")
ax.legend(fontsize=5.6, frameon=False, loc="upper center", bbox_to_anchor=(0.5, -0.28))
fig.tight_layout()
save(fig, "ms_fig2_placement_gain")

# ---------------------------------------------------------------- Fig 3: MC
E = np.load(f"{mc.RES}/mc_errors.npz")
summ = list(csv.reader(open(f"{mc.RES}/mc_summary.csv")))[1:]
th = {(r[0], r[1]): float(r[6]) for r in summ if r[6] not in ("",)}
fig, axs = plt.subplots(1, 3, figsize=(7.2, 2.5))
for ax, case in zip(axs[:2], ("A", "B")):
    for e, c in (("single (Cmax)", COL["single"]), ("GLS-3", COL["gls"]), ("immune-3", COL["immune"])):
        x = E[f"{case}_{e}"]
        sd = th[(case, e)]
        lim = 4 * th[(case, "single (Cmax)")]
        bins = np.linspace(-lim, lim, 121)
        ax.hist(x, bins=bins, density=True, histtype="step", color=c, lw=1, label=e.replace("immune", "zero-sum"))
        xx = np.linspace(-lim, lim, 400)
        ax.plot(xx, np.exp(-xx**2 / (2 * sd**2)) / (sd * np.sqrt(2 * np.pi)), ":", color=c, lw=1)
    ax.set_xlabel(r"$\hat P - P$ (kN)")
    ax.set_ylabel("density")
    ax.set_title({"A": "(a) 30+60+30 m", "B": "(b) Mây Bridge, calibration A"}[case], loc="left")
axs[0].legend(fontsize=6, frameon=False)
ax = axs[2]
for case, mkr in (("A", "o"), ("B", "s")):
    for e, c in (("single (Cmax)", COL["single"]), ("GLS-3", COL["gls"]), ("immune-3", COL["immune"])):
        x = E[f"{case}_{e}"]
        n = E[f"{case}_nax"]
        sd = [x[n == k].std(ddof=1) / th[(case, e)] for k in range(1, 7)]
        ax.plot(range(1, 7), sd, marker=mkr, color=c, lw=0.8, ms=3.5,
                label=f"{case}: {e}".replace("immune", "zero-sum") if case == "A" else None)
ax.axhline(1, color="k", lw=0.5)
ax.set_ylim(0.9, 1.1)
ax.set_xlabel("number of axles")
ax.set_ylabel("MC std / theory")
ax.set_title("(c) invariance of the scatter (o: A, s: B)", loc="left")
ax.legend(fontsize=5.5, frameon=False)
fig.tight_layout()
save(fig, "ms_fig3_montecarlo")

# ---------------------------------------------------------------- Fig 4: structure-aware
W = np.load(f"{mc.RES}/T4_weights.npz")
t4 = list(csv.DictReader(open(f"{mc.RES}/T4_structure_aware.csv")))
fig, axs = plt.subplots(1, 3, figsize=(7.2, 2.5))
ax = axs[0]
C0 = PM["2S-eq"].C("d", 12.6)
x = W["S20_x"]
ax.plot(x, W["S20_wu"] * C0 / mc.DX, color=COL["single"], lw=1.2, label="uniform (structure-agnostic)")
ax.plot(x, W["S20_g"] * C0 / mc.DX, color=COL["gls"], lw=0.9, label="min-variance invariant")
ax.plot(x, W["S20_gc"] * C0 / mc.DX, color=COL["immune"], lw=0.9, label=r"invariant, $\sum g$ = 0")
ax.set_xlabel("record coordinate x (m)")
ax.set_ylabel(r"weight $g(x)\,C/\Delta x$")
ax.set_title("(a) weights, S = 20 m, 2S-eq, x = 12.6 m", loc="left")
ax.legend(fontsize=5.5, frameon=False)
ax = axs[1]
S = [float(r["S_m"]) for r in t4]
ax.semilogy(S, [float(r["var_opt_over_unif_white"]) for r in t4], "-o", ms=3, color=COL["gls"],
            label="min-variance invariant")
ax.semilogy(S, [float(r["var_immune_over_unif_white"]) for r in t4], "-s", ms=3,
            color=COL["immune"], label=r"invariant, $\sum g$ = 0")
ax.semilogy(S, [float(r["CS_lower_bound"]) for r in t4], ":", color="k", label="Cauchy-Schwarz bound")
ax.semilogy(S, [float(r["var_MF_over_unif"]) for r in t4], "--", color=COL["single"],
            label="matched filter (not invariant)")
ax.axhline(1, color="k", lw=0.5)
ax.set_xlabel("entry-shift range S (m)")
ax.set_ylabel("Var / Var(uniform), white noise")
ax.set_title("(b) price of structure-agnosticism", loc="left")
ax.legend(fontsize=5.5, frameon=False)
ax = axs[2]
for nm, c in (("sensor +0.5 m", COL["aux"]), ("span-2 EI x1.2", COL["immune"])):
    ax.semilogy(S[1:], [float(r[f"defect_opt_{nm}"]) for r in t4][1:], "-o", ms=3, color=c,
                label=f"min-var., {nm}")
    ax.semilogy(S[1:], [float(r[f"defect_immune_{nm}"]) for r in t4][1:], "--s", ms=3, color=c,
                label=rf"$\sum g$=0, {nm}")
ax.semilogy(S[1:], [float(r["defect_unif_span-2 EI x1.2"]) for r in t4][1:], "-", color=COL["single"],
            label="uniform (any error)")
ax.set_xlabel("entry-shift range S (m)")
ax.set_ylabel("invariance defect (max-min)/mean")
ax.set_title("(c) fragility to model error", loc="left")
ax.legend(fontsize=5.2, frameon=False)
fig.tight_layout()
save(fig, "ms_fig4_structure_aware")
print("figures written to", mc.FIGS)

# ---------------------------------------------------------------- invariance-of-scatter check
lg = mc.Logger("multisensor_figures.log")
lg("By-axle-count std relative to pooled std (structure-agnostic estimators, cases A and B):")
worst = 0.0
for case, ests in (("A", ("single (Cmax)", "GLS-3", "immune-3")),
                   ("B", ("single (Cmax)", "GLS-3", "immune-3"))):
    n = E[f"{case}_nax"]
    for e in ests:
        x = E[f"{case}_{e}"]
        x = x.astype(float)
        dev = [x[n == k].std(ddof=1) / x.std(ddof=1) - 1 for k in range(1, 7)]
        cnt = [int((n == k).sum()) for k in range(1, 7)]
        worst = max(worst, max(abs(d) for d in dev))
        lg(f"  {case} {e:15s} deviations % {np.round(100*np.array(dev), 2).tolist()} (n per bin {cnt})")
lg(f"  max |deviation| = {100*worst:.2f} %; SE of one bin std ~ 1/sqrt(2*16700) = "
   f"{100/np.sqrt(2*16700):.2f} %")
