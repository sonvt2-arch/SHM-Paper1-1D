"""Package 1A figures (300 dpi PNG + PDF) in code/theory2/figures/:
  fig_gc_strain_map_2span   strain (moment) observability map, two-span beam
  fig_gc_strain_map_3span   strain observability map, symmetric three-span beam
  fig_gc_channels_prismatic all channels along prismatic two- and three-span girders
  fig_gc_caumay_channels    Cau May: deflection vs strain indicators along the girder

Run:  python code/theory2/gc_figures.py
"""
import os
import sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import gc_theory as th          # noqa: E402
from gc_fe import Girder        # noqa: E402
import gc_bridge as br          # noqa: E402

FIG = os.path.join(HERE, "figures")
os.makedirs(FIG, exist_ok=True)
plt.rcParams.update({"font.size": 9, "axes.titlesize": 9.5, "savefig.dpi": 300})
C_W, C_M, C_TH, C_V = "#1f5fa8", "#c2410c", "#4d7c0f", "#7c3aed"
LEV = np.linspace(-1.5, 1.5, 31)


def save(fig, name):
    for ext in ("png", "pdf"):
        fig.savefig(os.path.join(FIG, f"{name}.{ext}"), bbox_inches="tight")
    plt.close(fig)
    print("wrote", name)


def map_panel(ax, X, Y, Z, Zw, xlabel, ylabel, title):
    cs = ax.contourf(X, Y, np.clip(Z, -1.5, 1.5), levels=LEV, cmap="RdBu", extend="both")
    ax.contourf(X, Y, np.abs(Z), levels=[0, 0.2], colors="none", hatches=["////"])
    ax.contour(X, Y, Z, levels=[0.0], colors="k", linewidths=1.8)
    ax.contour(X, Y, Zw, levels=[0.0], colors="k", linewidths=1.0, linestyles="--")
    ax.set_xlabel(xlabel); ax.set_ylabel(ylabel); ax.set_title(title)
    return cs


# ------------------------------------------------------------- two-span map
xi = np.linspace(0.0, 1.0, 301)
rL = np.linspace(0.5, 2.5, 301)
XX, RR = np.meshgrid(xi, rL)
MU = th.mu_two(RR, 1.0)
Z = th.N_M(XX, 0, MU)
Zw = th.N_w(XX, 0, MU)
fig, ax = plt.subplots(1, 2, figsize=(10.5, 4.2), constrained_layout=True)
cs = map_panel(ax[0], XX, RR, Z, Zw, r"sensor position $\xi = x/L_1$ (span 1)",
               r"span ratio $\lambda = L_2/L_1$",
               r"(a) strain indicator $N_M = 8M_q(x_m)/(q_0L_1^2)$, $\gamma=1$")
ax[0].plot([], [], "k-", lw=1.8, label=r"strain blind: $\xi_0 = 1-\mu/4$")
ax[0].plot([], [], "k--", lw=1.0, label="deflection blind (Eq. 6)")
ax[0].fill_between([], [], [], facecolor="none", hatch="////", label=r"$|N_M|<0.2$")
ax[0].legend(loc="upper right", fontsize=7.5, framealpha=0.9)
fig.colorbar(cs, ax=ax[0], label=r"$N_M$", ticks=[-1.5, -1, -0.5, 0, 0.5, 1, 1.5])
for rE, ls in [(0.5, ":"), (1.0, "-"), (2.0, "--"), (4.0, "-.")]:
    mu = th.mu_two(rL, rE)
    x0 = 1 - mu / 4
    ax[1].plot(rL, np.where(x0 > 0, x0, np.nan), color=C_M, ls=ls,
               label=rf"$\gamma={rE:g}$")
    # deflection blind position at this rho_EI (root of F in (0,1)) for comparison
    # deflection blind position: F/[xi(1-xi)] = 0 -> xi^2 - (1-mu/2) xi - (1-mu/2) = 0
    xb = []
    for m in mu:
        a_ = 1 - m / 2
        rr = [z for z in np.roots([1.0, -a_, -a_]).real if 0 < z < 1]
        xb.append(min(rr) if rr else np.nan)
    ax[1].plot(rL, xb, color=C_W, ls=ls, lw=1.0)
ax[1].plot([], [], color=C_M, label="strain blind point")
ax[1].plot([], [], color=C_W, lw=1.0, label="deflection blind point")
ax[1].set_xlabel(r"span ratio $\lambda = L_2/L_1$")
ax[1].set_ylabel(r"blind position $\xi$ in span 1")
ax[1].set_ylim(0, 1); ax[1].grid(alpha=0.3)
ax[1].set_title(r"(b) blind positions: strain for every $\mu<4$, deflection only for $1<\mu<2$")
ax[1].legend(fontsize=7.5, ncol=2, loc="lower left")
save(fig, "fig_gc_strain_map_2span")

# ------------------------------------------------------------- three-span map
B = np.linspace(0.8, 2.5, 301)
XS = np.linspace(0.0, 1.0, 301)
XE = np.linspace(0.0, 0.5, 201)
BB, XX = np.meshgrid(B, XS)
MU = th.mu_three(BB)
Zs, Zsw = th.N_M(XX, 0, MU), th.N_w(XX, 0, MU)
BB2, EE = np.meshgrid(B, XE)
M2 = th.mu_three(BB2) / BB2**2
Zm, Zmw = th.N_M(EE, M2, M2), th.N_w(EE, M2, M2)
fig, ax = plt.subplots(1, 2, figsize=(10.5, 4.2), constrained_layout=True)
map_panel(ax[0], BB, XX, Zs, Zsw, r"$\beta = L_\mathrm{main}/L_\mathrm{side}$", r"side-span position $\xi = x/L_\mathrm{side}$",
          r"(a) side span, $N_M = 8M_q/(q_0L_s^2)$, uniform $EI$")
cs = map_panel(ax[1], BB2, EE, Zm, Zmw, r"$\beta = L_\mathrm{main}/L_\mathrm{side}$",
               r"main-span position $\zeta$ from the pier",
               r"(b) main span, $N_M = 8M_q/(q_0L_m^2)$")
for a_, ys in ((ax[0], [0.4, 0.5]), (ax[1], [0.5])):
    a_.axvline(90 / 55, color="0.2", lw=0.8, ls=":")
    for y in ys:
        a_.plot(90 / 55, y, "ko", ms=4)
ax[0].annotate("Mây Bridge gauges\n(N8 at 0.4L, 0.5L)", (90 / 55, 0.45), (1.9, 0.86),
               fontsize=7.5, arrowprops=dict(arrowstyle="-", lw=0.6))
ax[1].annotate("N7", (90 / 55, 0.5), (1.75, 0.44), fontsize=7.5,
               arrowprops=dict(arrowstyle="-", lw=0.6))
ax[0].plot([], [], "k-", lw=1.8, label="strain blind")
ax[0].plot([], [], "k--", lw=1.0, label="deflection blind")
ax[0].legend(loc="lower left", fontsize=7.5, framealpha=0.9)
fig.colorbar(cs, ax=ax, label=r"$N_M$ (hatched: $|N_M|<0.2$)", shrink=0.9)
save(fig, "fig_gc_strain_map_3span")

# ------------------------------------------------------------- prismatic channels
fig, ax = plt.subplots(1, 2, figsize=(10.5, 3.8), constrained_layout=True)
for a_, spl, title in ((ax[0], th.two_span(1.0), "(a) equal two-span beam"),
                       (ax[1], th.three_span_sym(90 / 55),
                        r"(b) symmetric three-span, $\beta=1.636$ (Mây Bridge, prismatic)")):
    x0 = 0.0
    for j, (L, EI, ml, mr) in enumerate(spl):
        s = np.linspace(0, 1, 201)
        X = (x0 + s * L) / spl[0][0]
        a_.plot(X, th.N_w(s, ml, mr), color=C_W, label=r"$N_w$ deflection" if j == 0 else None)
        a_.plot(X, th.N_th(s, ml, mr), color=C_TH, label=r"$N_\theta$ rotation" if j == 0 else None)
        a_.plot(X, th.N_M(s, ml, mr), color=C_M, lw=2, label=r"$N_M$ strain/moment" if j == 0 else None)
        a_.plot(X, th.N_V(s, ml, mr), color=C_V, lw=0.9, ls="--",
                label=r"$N_V$ shear" if j == 0 else None)
        x0 += L
    a_.axhspan(-0.2, 0.2, color="0.85", zorder=0)
    a_.axhline(0, color="k", lw=0.6)
    for xs in np.cumsum([0] + [s_[0] for s_ in spl]):
        a_.axvline(xs / spl[0][0], color="0.4", lw=0.6)
    a_.set_xlabel(r"$x/L_1$" if len(spl) == 2 else r"$x/L_\mathrm{side}$")
    a_.set_ylabel("normalized constant (1 = simply supported reference)")
    a_.set_title(title); a_.set_ylim(-2.2, 1.6); a_.grid(alpha=0.25)
ax[0].legend(fontsize=7.5, loc="lower left")
save(fig, "fig_gc_channels_prismatic")

# ------------------------------------------------------------- Cau May
cs_ = br.cases()
h = br.depth()
show = ["prismatic, pinned", "haunched, A (k_FE)", "haunched, B (alpha 0.716, k 1.2e8)"]
cols = {"prismatic, pinned": "0.45", "haunched, A (k_FE)": "#c2410c",
        "haunched, B (alpha 0.716, k 1.2e8)": "#1f5fa8"}
labs = {"prismatic, pinned": "prismatic, pinned piers",
        "haunched, A (k_FE)": "haunched, calibration A",
        "haunched, B (alpha 0.716, k 1.2e8)": "haunched, calibration B"}
fig, ax = plt.subplots(3, 1, figsize=(8.0, 8.4), sharex=True, constrained_layout=True)
for name in show:
    c = cs_[name]
    g = Girder(br.SPANS, EI=c["EI"], ne_per_span=0, h_max=0.5, kind="flex", ngauss=8,
               k_rot=c["k"])
    X, M, V, u = g.moment_diagram(nsub=2)
    Lx = np.where((X < 55) | (X > 145), 55.0, 90.0)
    NM = 8 * M / Lx**2
    Lw = np.where((g.x < 55) | (g.x > 145), 55.0, 90.0)
    Nw = 192 * br.EI_MID * u[0::2] / Lw**4
    if name.startswith("haunched"):
        sens = np.array([br.EI_MID * c["alpha"] / c["EI"](xx) * h(xx) / br.H_MID for xx in X])
    else:
        sens = np.ones_like(X)
    ax[0].plot(g.x, Nw, color=cols[name], label=labs[name])
    ax[1].plot(X, NM, color=cols[name], label=labs[name])
    ax[2].plot(X, NM * sens, color=cols[name], label=labs[name])
    for z in g.moment_zeros():
        ax[1].plot(z, 0, "o", color=cols[name], ms=4)
for a_ in ax:
    a_.axhspan(-0.2, 0.2, color="0.88", zorder=0)
    a_.axhline(0, color="k", lw=0.6)
    for xs in (0, 55, 145, 200):
        a_.axvline(xs, color="0.4", lw=0.6)
    for gl, xg in br.GAUGES.items():
        a_.axvline(xg, color="k", lw=0.6, ls=":")
    a_.grid(alpha=0.25)
ax[0].set_ylabel(r"$N_w = 192EI_\mathrm{mid}C_m/L^4$")
ax[1].set_ylabel(r"$N_M = 8M_q/(q_0L^2)$")
ax[2].set_ylabel(r"$N_{\varepsilon}$ (mid-span section units)")
ax[0].set_title(r"(a) deflection channel, $N_w$")
ax[1].set_title("(b) strain channel: uniform-load moment; dots = strain blind points")
ax[2].set_title(r"(c) strain channel incl. section sensitivity $c/EI$ (assumption $c\propto h$)")
ax[1].set_ylim(-2.3, 1.1); ax[2].set_ylim(-1.0, 1.1)
ax[2].set_xlabel("x from end support T5 (m)")
ax[0].set_ylim(-0.65, 0.85)
for gl, xg, ha in (("N8 0.4L", 178.0, "left"), ("N8 mid", 172.5, "right"), ("N7", 100.0, "center")):
    ax[0].text(xg + (0.8 if ha == "left" else -0.8 if ha == "right" else 0), 0.78, gl,
               fontsize=7, ha=ha, bbox=dict(fc="white", ec="none", pad=0.5))
ax[0].legend(fontsize=7.5, loc="lower center", ncol=3, bbox_to_anchor=(0.5, -0.02))
save(fig, "fig_gc_caumay_channels")
