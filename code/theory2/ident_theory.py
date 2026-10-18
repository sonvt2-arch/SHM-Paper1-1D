"""Package 1C, part 1 - sensitivity / identifiability theory.

(1) Adjoint sensitivities of C_m to pier rotational stiffness k and girder
    scale alpha, K = alpha*K_g + k*K_p:
        dC_m/dk     = - sum_piers theta_m,i * theta_q,i
        dC_m/dalpha = - (C_m - k sum theta_m,i theta_q,i) / alpha
    theta_m,i = pier rotation under a unit point load at the gauge (= slope
    of the gauge's influence line... by Maxwell-Betti), theta_q,i = pier
    rotation under the unit uniform load.  Euler: S_alpha + S_k = -1 with
    S_p = dlnC_m/dlnp, because C_m(alpha,k) = C_m(1,k/alpha)/alpha.
(2) Moebius law for any mirror-symmetric girder:
        C_m(kappa) = C_inf + (C_0 - C_inf) / (1 + kappa/k_g),
    kappa = k/alpha, k_g = 1/(a^T G_0 a): girder's own antisymmetric
    rotational stiffness at the piers (only the antisymmetric pier-rotation
    pattern is excited by the symmetric uniform load).
(3) Closed form for the symmetric prismatic three-span beam with springs:
        mu(K) = 1 + beta(2 beta^2-3) / (3 beta + 2 rho + beta K),  K = k L_s/EI_s
        N_side(xi) = 8 F(xi, mu)           (Eq. 4 / Eq. 8 of the manuscript)
        nu(K) = (2/3)[1 - rho(2beta^2-3)/(beta^2(3beta+2rho+beta K))]
        N_main(1/2) = 2.5 - 3 nu           (normalised with EI_m, L_m)
    verified against the FE model.
Run: python3 code/theory2/ident_theory.py
"""
import numpy as np
from ident_core import (Model, EI_law, SPANS, X_N8, X_N7, X_N8MID, E, CM,
                        EI_MID, Logger, FIGD, norm_index)
import os

log = Logger("ident_theory.log")


# ------------------------------------------------ closed form (prismatic)
def F(xi, mu):
    return xi * (1 - 2 * xi**2 + xi**3) - 0.5 * mu * xi * (1 - xi**2)


def mu_spring(K, beta, rho=1.0):
    return 1 + beta * (2 * beta**2 - 3) / (3 * beta + 2 * rho + beta * K)


def nu_spring(K, beta, rho=1.0):
    return (2 / 3) * (1 - rho * (2 * beta**2 - 3) / (beta**2 * (3 * beta + 2 * rho + beta * K)))


def N_side(xi, K, beta, rho=1.0):
    return 8 * F(xi, mu_spring(K, beta, rho))


def N_main(K, beta, rho=1.0):
    return 2.5 - 3 * nu_spring(K, beta, rho)


def S_side(xi, K, beta, rho=1.0):
    """d N_side / d ln K  and log-sensitivity d ln C / d ln K."""
    c = 3 * beta + 2 * rho
    dmu = -beta * (2 * beta**2 - 3) * beta * K / (c + beta * K) ** 2
    dN = -4 * xi * (1 - xi**2) * dmu
    return dN, dN / N_side(xi, K, beta, rho)


def mu_crit(xi):
    return 2 * (1 + xi - xi**2) / (1 + xi)


def K_blind(xi, beta, rho=1.0):
    m = mu_crit(xi)
    return (beta * (2 * beta**2 - 3) / (m - 1) - (3 * beta + 2 * rho)) / beta


def main():
    beta = 90 / 55
    Ls = 55.0
    log("=== (3) Closed form, symmetric prismatic 3-span beam with pier springs ===")
    log(f"beta = {beta:.6f}, rho_EI = 1, K = k L_s / EI_s")
    EIc = lambda x: EI_MID + 0 * x
    mprism = Model(EIc, None, ne=10)
    rows = []
    maxerr = 0
    for K in [0.0, 0.3, 1.0, 3.0, 10.0, 30.0, 100.0, 1e4]:
        k = K * EI_MID / Ls
        for xi in (0.4, 0.5):
            cf = N_side(xi, K, beta)
            fe = norm_index(mprism.Cm(200 - xi * Ls, k), Ls)
            maxerr = max(maxerr, abs(cf - fe))
            rows.append((K, xi, cf, fe))
        cfm = N_main(K, beta)
        fem = norm_index(mprism.Cm(100.0, k), 90.0)
        maxerr = max(maxerr, abs(cfm - fem))
        log(f"K={K:8.1f}  mu={mu_spring(K,beta):.6f}  N_side(0.4) CF={rows[-2][2]:+.6f} FE={rows[-2][3]:+.6f} | "
            f"N_side(0.5) CF={rows[-1][2]:+.6f} FE={rows[-1][3]:+.6f} | N_main(0.5) CF={cfm:+.6f} FE={fem:+.6f}")
    log(f"max |closed form - FE| = {maxerr:.2e}")
    c = 3 + 2 / beta
    log(f"N_side is a Moebius function of K; |dN/dlnK| peaks at K* = 3 + 2rho/beta = {c:.4f} "
        f"(k* = {c*EI_MID/Ls:.3e} kNm/rad for EI_s = EI_mid)")
    for xi in (0.4, 0.5):
        Kb = K_blind(xi, beta)
        log(f"xi={xi}: N(K=0)={N_side(xi,0,beta):.4f}, N(K->inf)={N_side(xi,1e12,beta):.4f}, "
            f"mu_crit={mu_crit(xi):.6f}, blind spring K_crit={Kb:.4f}"
            f" ({'exists' if Kb > 0 else 'none for K>0: already past blind at K=0' if N_side(xi,0,beta) < 0 else 'none: N>0 for all K>=0'})")
        dN, S = S_side(xi, c, beta)
        log(f"   at K*: N={N_side(xi,c,beta):.4f}, dN/dlnK={dN:.4f}, dlnC/dlnK={S:.3f}")
    log(f"main span (mid): N(K=0)={N_main(0,beta):.6f}, N(K->inf)={N_main(1e12,beta):.6f} (fixed-fixed 0.5)")
    # what K reproduces kFE on a prismatic beam?  (illustration only)

    # ------------------------------------------- (1) adjoint sensitivities
    log("\n=== (1) Adjoint sensitivity, haunched model (Lv = 44 m), alpha = 1 ===")
    EI, h, n = EI_law(44.0)
    m = Model(EI, None, ne=10)
    piers = [int(np.where(m.free == d)[0][0]) for d in [2 * i + 1 for i in m.node[1:3]]]
    for k in (2.748e7, 1.675e8):
        uq = m.solve(m.uniform_load(), k)
        for lab, xm, L in (("N8 0.4L", X_N8, 55.0), ("N8 mid", X_N8MID, 55.0), ("N7 mid", X_N7, 90.0)):
            um = m.solve(m.point_load(xm), k)
            C = m.Cm(xm, k)
            dCdk = -sum(um[p] * uq[p] for p in piers)
            S_k = k * dCdk / C
            S_a = -(C - k * sum(um[p] * uq[p] for p in piers)) / C
            eps = 1e-4
            Cp, Cm_ = m.Cm(xm, k * (1 + eps)), m.Cm(xm, k * (1 - eps))
            S_fd = (np.log(Cp) - np.log(Cm_)) / (np.log(1 + eps) - np.log(1 - eps))
            Ap, Am_ = m.Cm(xm, k, 1 + eps), m.Cm(xm, k, 1 - eps)
            Sa_fd = (np.log(Ap) - np.log(Am_)) / (np.log(1 + eps) - np.log(1 - eps))
            log(f"k={k:.3e} {lab:8s}: C_m={C:.4e}  S_k adjoint={S_k:+.4f} FD={S_fd:+.4f} | "
                f"S_alpha adjoint={S_a:+.4f} FD={Sa_fd:+.4f} | S_alpha+S_k={S_a+S_k:+.6f}")

    # ------------------------------------------- (2) Moebius law
    log("\n=== (2) Moebius law C_m(kappa) = C_inf + (C_0-C_inf)/(1+kappa/k_g) ===")
    N = m.N
    a = np.zeros(m.Kg.shape[0])
    a[piers[0]], a[piers[1]] = 1 / np.sqrt(2), -1 / np.sqrt(2)
    s_ = np.zeros_like(a)
    s_[piers[0]], s_[piers[1]] = 1 / np.sqrt(2), 1 / np.sqrt(2)
    G0a = m.solve(a, 0.0)
    G0s = m.solve(s_, 0.0)
    ga = a @ G0a
    gs = s_ @ G0s
    log(f"girder pier flexibility: antisymmetric g_a = {ga:.4e} rad/kNm -> k_g = 1/g_a = {1/ga:.4e} kNm/rad;"
        f" symmetric g_s = {gs:.4e} -> {1/gs:.4e}; cross term a^T G0 s = {a @ G0s:.2e}")
    kgrid = np.logspace(5, 12, 29)
    for lab, xm in (("N8 0.4L", X_N8), ("N8 mid", X_N8MID), ("N7 mid", X_N7)):
        C0 = m.Cm(xm, 0.0)
        Cinf = m.Cm(xm, 1e15)
        err = max(abs(m.Cm(xm, k) - (Cinf + (C0 - Cinf) / (1 + k * ga))) / abs(C0) for k in kgrid)
        log(f"{lab:8s}: C_0={C0:.4e}  C_inf={Cinf:.4e}  C_inf/C_0={Cinf/C0:+.3f}  "
            f"max rel. error of Moebius law over k=1e5..1e12: {err:.1e}")
        for k in (2.748e7, 1.675e8):
            C = m.Cm(xm, k)
            S = -(k * ga) * (C0 - Cinf) / ((1 + k * ga) ** 2 * C)
            log(f"    kappa={k:.3e} (kappa/k_g={k*ga:.3f}): S_kappa from Moebius law = {S:+.4f}")
    log("Log-sensitivity S_kappa = dlnC_m/dln kappa = -(kappa g_a)(C_0-C_inf) / [(1+kappa g_a)^2 C_m(kappa)]; "
        "|dC_m/dln kappa| is largest at kappa = k_g (prismatic case: k_g L_s/EI_s = 3 + 2rho/beta)")
    log("Boundary-conditioning indicator B_m = |S_kappa|: relative error in C_m per relative error in kappa = k/alpha.")

    # figure
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    plt.rcParams.update({"font.size": 8.5})
    fig, axs = plt.subplots(1, 2, figsize=(7.2, 2.9), constrained_layout=True)
    Ks = np.logspace(-2, 3, 200)
    for xi, ls in ((0.4, "-"), (0.5, "--")):
        axs[0].semilogx(Ks, N_side(xi, Ks, beta), "k", ls=ls, label=f"side span, $\\xi$={xi} (closed form)")
        axs[1].semilogx(Ks, abs(S_side(xi, Ks, beta)[1]), "k", ls=ls, label=f"side, $\\xi$={xi}")
    axs[0].semilogx(Ks, N_main(Ks, beta), color="#3b6fb6", label="main span, mid (closed form)")
    num = lambda K: (N_main(K * 1.0001, beta) - N_main(K / 1.0001, beta)) / (2 * np.log(1.0001)) / N_main(K, beta)
    axs[1].semilogx(Ks, abs(num(Ks)), color="#3b6fb6", label="main, mid")
    fe = np.array(rows)
    for xi, mk in ((0.4, "o"), (0.5, "s")):
        sel = (fe[:, 1] == xi) & (fe[:, 0] > 0) & (fe[:, 0] < 1e3)
        axs[0].plot(fe[sel, 0], fe[sel, 3], mk, mfc="none", color="#d0563b", ms=4)
    axs[0].plot([], [], "o", mfc="none", color="#d0563b", label="FE check")
    axs[0].axhspan(-0.2, 0.2, color="#d0563b", alpha=0.12, lw=0)
    axs[0].axhline(0, color="k", lw=0.4)
    axs[0].set_xlabel("$K = kL_s/EI_s$")
    axs[0].set_ylabel("$N_m = 192EI\\,C_m/L^4$")
    axs[0].set_title(f"prismatic, $\\beta$ = {beta:.3f}", fontsize=8.5)
    axs[0].legend(fontsize=6.5)
    axs[1].axvline(c, color="0.5", lw=0.6, ls=":")
    axs[1].set_xlabel("$K = kL_s/EI_s$")
    axs[1].set_ylabel("$|\\partial \\ln C_m/\\partial \\ln K|$")
    axs[1].set_yscale("log")
    axs[1].set_title("boundary-conditioning indicator $B_m$", fontsize=8.5)
    axs[1].legend(fontsize=6.5)
    fig.savefig(os.path.join(FIGD, "ident_theory_closedform.png"), dpi=200)
    plt.close(fig)
    log.save()


if __name__ == "__main__":
    main()
