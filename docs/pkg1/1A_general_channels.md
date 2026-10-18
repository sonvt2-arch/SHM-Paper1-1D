# Package 1A: Observability of arbitrary linear response channels

Author role: structural theorist (package 1A). Status: draft for the corresponding author. Nothing in `manuscript/` has been edited.

**Scripts** (all new, in `code/theory2/`; the existing `code/analysis/*.py` files are imported but not modified):

| File | Content |
|---|---|
| `gc_theory.py` | closed forms for every channel (span-level building block, two-span, symmetric three-span, n-span three-moment solver, exact blind roots) |
| `gc_fe.py` | FE for all channels (reuses `cm_multispan.element`), rotational pier springs, exact influence-line integrals, exact convoy-record integrals |
| `gc_force_method.py` | independent force-method solution for three spans with arbitrary $EI(x)$ and pier springs (adaptive quadrature) |
| `gc_bridge.py` | Cầu Mây model inputs (reuses `wp3_fe.haunch_EI`; WP3 calibrations A and B) |
| `verify_general.py` | verification; log in `logs/verify_general.log` |
| `gc_results.py` | all tables of this note; log in `logs/gc_results.log`, CSV files in `results/gc_T*.csv` |
| `gc_figures.py` | figures in `figures/fig_gc_*.png/.pdf` (300 dpi) |

Every number below is copied from `logs/verify_general.log` or `logs/gc_results.log`. Assumptions are marked **[A#]**.

---

## 1. Generalised invariance theorem

**Setting.** A structure carries vertical loads along a fixed path $x\in[0,L]$. A *response channel* at a fixed point $m$ is any fixed linear functional $r_m$ of the displacement field, measured relative to the unloaded state. Examples are the deflection $w(x_m)$, the rotation $\theta(x_m)=w'(x_m)$, the bending moment $M(x_m)$, the fibre strain $\varepsilon(x_m)=c\,M(x_m)/EI(x_m)$, the curvature $\kappa = M/EI$, the shear force $V(x_m)$ and a support reaction $R_j$. Let $r_m(x)$ be its influence line, i.e. the response to a unit force at $x$.

**Hypotheses.**
- (H1) Linear-elastic, small-displacement structure whose properties do not change during the crossing. $EI(x)$, the degree of indeterminacy and linear elastic supports (springs) are arbitrary. Excluded: cracking, bearing uplift or friction, temperature change during the crossing.
- (H2) Quasi-static response: inertia and damping are negligible, so the record is $y_m(x)=\sum_i P_i\,r_m(x-a_i)$ (manuscript Sec. 6.5 gives the limits).
- (H3) Constant axle forces $P_i$ at fixed offsets $a_i$ that travel along the same path on which $r_m$ is defined. In the 1-D model this path is the girder axis; for a 2-D deck it is the lane, and $C_r$ is then the response to a uniform load on that lane.
- (H4) $r_m$ is integrable and vanishes outside $[0,L]$. Jumps are allowed (shear at $m$) and so are kinks (moment and strain at $m$).
- (H5) A complete crossing: the integration runs from the entry of the first axle to the exit of the last, $[0,L+a_\max]$, and the record is re-zeroed to the unloaded state.

**Theorem.** Under (H1)–(H5),
$$
I_r=\int_0^{L+a_\max} y_m\,\mathrm dx = P_\mathrm{tot}\,C_r,\qquad
C_r=\int_0^L r_m(u)\,\mathrm du=\frac{r_m\big[q_0\ \text{on}\ [0,L]\big]}{q_0}.
\tag{G1}
$$

*Proof.* Substituting $u=x-a_i$ term by term gives the first equality, exactly as in manuscript Eq. (2). For the second, a uniform load $q_0$ is the continuous superposition of point loads $q_0\,\mathrm du$, so linearity (H1) and Fubini give $r_m[q_0]=q_0\int r_m(u)\,\mathrm du$. ∎

The identification needs **superposition only**. Maxwell–Betti is not required for (G1). It enters only through Müller-Breslau: $r_m(x)$ is the deflected shape $w^{(r)}(x)$ caused by the generalised force dual to $r$ (a unit force for $w$, a unit couple for $\theta$, a unit relative rotation for $M$, a unit relative transverse slip for $V$, a unit support settlement for $R$). Hence $C_r=\int w^{(r)}\,\mathrm dx$, which is the manuscript's Eq. (3) when $r=w$. At constant speed, $I_t=I_r/v$.

**Strain channel.** $\varepsilon_m = c_m M(x_m)/EI_m$ with *local* section constants $c_m$ and $EI_m$, so
$$
C_\varepsilon=\frac{c_m\,M_q(x_m)}{EI_m\,q_0}.\tag{G2}
$$
The local section enters only as a gain. **The blind loci of a strain (or curvature or moment) channel are the zeros of the uniform-load bending-moment diagram**, for any $EI(x)$ and any elastic support conditions. $EI(x)$ affects the blind loci only through the redundant moments.

---

## 2. Closed forms for prismatic spans

### 2.1 Span-level building block

Take a span of length $L$ and rigidity $EI$ under $q_0$, with sagging end moments $M_l$ and $M_r$. Write them through the hogging parameters $m_l=-8M_l/(q_0L^2)$ and $m_r=-8M_r/(q_0L^2)$, and let $\xi=s/L$. Each indicator below equals 1 for the simply supported reference: mid-span $w$ and $M$, end rotation, end shear, end reaction.

$$
\begin{aligned}
N_w&=\frac{192EI\,C_w}{L^4}=8\Phi,\qquad \Phi=\xi(1-2\xi^2+\xi^3)-\tfrac{m_l}{2}(2\xi-3\xi^2+\xi^3)-\tfrac{m_r}{2}(\xi-\xi^3),\\
N_\theta&=\frac{24EI\,C_\theta}{L^3}=\Phi'(\xi),\\
N_M&=\frac{8\,C_M}{L^2}=\frac{8M_q(x_m)}{q_0L^2}=4\xi(1-\xi)-m_l(1-\xi)-m_r\xi,\qquad C_\varepsilon=\frac{c\,L^2}{8EI}N_M,\\
N_V&=\frac{2\,C_V}{L}=1-2\xi+\tfrac{m_l-m_r}{4},\\
R_\text{left}&=\tfrac{q_0L}{8}(4+m_l-m_r),\quad R_\text{right}=\tfrac{q_0L}{8}(4-m_l+m_r)\ \ (\text{span contributions}),\quad N_R=\frac{R}{q_0L_\text{trib}}.
\end{aligned}\tag{G3}
$$

For the two-span beam, $(m_l,m_r)=(0,\mu)$ in span 1, with $\mu$ from manuscript Eq. (5), and $(\mu/\rho_L^2,0)$ in span 2. For the symmetric three-span beam, $(0,\mu)$ in the side span, with $\mu$ from Eq. (8), and $(m,m)$ in the main span, where $m=\mu/\beta^2=2\nu/3$. With these substitutions $N_w$ reproduces manuscript Eqs. (4), (8) and App. D. Strain zeros solve
$$4\xi^2-(4+m_l-m_r)\xi+m_l=0.\tag{G4}$$

### 2.2 Blind loci by channel

| Channel | Blind locus (uniform-load zero) | Two-span (span 1) | Symmetric three-span |
|---|---|---|---|
| Strain / moment / curvature | zeros of $M_q$ | $\xi_0=1-\mu/4$; span 2: $\mu/(4\rho_L^2)$ of $L_2$ from B | side $\xi_0=1-\mu/4$; main $\eta_0=\tfrac12(1-\sqrt{1-m})$ from the pier |
| Deflection | zeros of $w_q$ | $\mu=\mu_\mathrm{crit}(\xi)$, Eq. (6); exists only for $1<\mu<2$ | Eq. (9) |
| Rotation | extrema of $w_q$ (zeros of $\Phi'$) | end A: $\mu=2$ ($\rho_L=(1+\sqrt5)/2=1.618034$ for $\rho_{EI}=1$); pier B: $\mu=1\Leftrightarrow\rho_L=1$ for **any** $\rho_{EI}$ | end: $\mu=2$, $\beta^3-3\beta-1=0$, $\beta=2\cos(\pi/9)=1.879385$; pier: $\mu=1\Leftrightarrow\beta=\sqrt{3/2}=1.224745$ for **any** $\rho$; mid main span: always blind (symmetry) |
| Shear | maxima of $M_q$ | $\xi=(4-\mu)/8=\xi_0/2$ | side $\xi_0/2$; mid main span: always blind (symmetry) |
| End reaction | $M_q$ has no sagging zone in the end span | $\mu=4$: $\rho_L=(1+\sqrt{13})/2=2.302776$ | $\mu=4$: $\beta^3-6\beta-3=0$, $\beta=2.669079$ |
| Interior reaction | never blind under a full UDL (two-span and symmetric three-span: $R_B=\tfrac{q_0}{2}(L_1+L_2)+|M_B|(1/L_1+1/L_2)>0$) | – | – |

Three identities follow directly from (G3).

1. **End-reaction indicator = contraflexure abscissa.** Statics of the end segment gives $M_q(x)=R_Ax-q_0x^2/2$, hence $N_{R_A}=2R_A/(q_0L_1)=\xi_0$. This holds for **any** $EI(x)$ and any pier springs. The FE confirms it for the haunched Cầu Mây girder: $N_{R_A}=0.4724$ against $\xi_0=25.984/55=0.4724$ (pinned piers).
2. **Antisymmetric channels on an axis of symmetry are identically blind.** Rotation and shear at the centre of a symmetric girder are blind whatever the spans and stiffnesses.
3. **The deflection blind locus ends where the end rotation vanishes.** The manuscript's limit $\beta=2\cos(\pi/9)$ (end of the side-span deflection blind locus) is exactly the root of $N_\theta(\text{end})=1-\mu/2=0$.

The blind configurations of the rotation, shear, reaction and mid-main-span strain channels are reproduced by the FE to $\le 2.3\times10^{-12}$ (log section E).

### 2.3 Strain channel: positions of the zero-moment points

**Two-span** (T1; $\rho_{EI}=1$ unless stated). Band = $|N_M|<0.2$ around $\xi_0$.

| $\rho_L$ | $\mu$ | $\xi_0$ (span 1) | distance from B | band in span 1 | $N_M$ mid span 1 | $N_M$ at B | zero in span 2 (from C, $/L_2$) |
|---|---|---|---|---|---|---|---|
| 0.5 | 0.75 | 0.8125 | 0.1875 $L_1$ | 0.7454–0.8700 | 0.625 | −0.75 | 0.2500 |
| 0.8 | 0.84 | 0.7900 | 0.2100 | 0.7206–0.8489 | 0.580 | −0.84 | 0.6719 |
| 1.0 | 1.00 | 0.7500 | 0.2500 | 0.6760–0.8116 | 0.500 | −1.00 | 0.7500 |
| 1.2 | 1.24 | 0.6900 | 0.3100 | 0.6077–0.7561 | 0.380 | −1.24 | 0.7847 |
| 1.45743 | 1.667 | 0.5833 | 0.4167 | 0.4789–0.6592 | 0.167 | −1.67 | 0.8038 |
| 1.618 | 2.00 | 0.5000 | 0.5000 | 0.3618–0.5854 | 0.000 | −2.00 | 0.8090 |
| 2.0 | 3.00 | 0.2500 | 0.7500 | 0–0.3812 | −0.500 | −3.00 | 0.8125 |
| 2.303 | 4.00 | – (no sagging zone) | – | – | −1.000 | −4.00 | 0.8114 |

For equal spans, $\mu=1$ for every $\rho_{EI}$. The stiffness ratio moves the strain zero only for unequal spans: at $\rho_L=1.6$, $\rho_{EI}=2.14$, $\xi_0=0.5832$.

At the blind configuration of the mid-span deflection channel ($\rho_L=1.45743$), the mid-span strain indicator is 0.167, also inside its band, because $\mu=5/3$ gives $N_M(1/2)=1-\mu/2=1/6$. At $\rho_L=1.618$ both the mid-span strain and the end rotation are exactly blind.

**Symmetric three-span, uniform $EI$** (T2). $\eta$ is measured from the pier; main-span indicators are normalised by $L_m$.

| $\beta$ | $\mu$ | side $\xi_0$ | side band | main $\eta_0$ | main band | $N_M$ mid side | $N_M$ mid main | $N_{R}$ end | $N_\theta$ at pier |
|---|---|---|---|---|---|---|---|---|---|
| 1.0 | 0.800 | 0.8000 | 0.7317–0.8583 | 0.2764 | 0.1838–0.5000 | 0.600 | **0.200** | 0.800 | −0.200 |
| 1.2 | 0.974 | 0.7564 | 0.6832–0.8176 | 0.2157 | 0.1383–0.3243 | 0.513 | 0.323 | 0.756 | −0.026 |
| 1.2247 | 1.000 | 0.7500 | 0.6760–0.8116 | 0.2113 | 0.1349–0.3174 | 0.500 | 0.333 | 0.750 | 0 |
| 1.4 | 1.208 | 0.6981 | 0.6170–0.7635 | 0.1902 | 0.1180–0.2856 | 0.396 | 0.384 | 0.698 | 0.208 |
| 1.5 | 1.346 | 0.6635 | 0.5768–0.7318 | 0.1831 | 0.1122–0.2754 | 0.327 | 0.402 | 0.664 | 0.346 |
| 1.636 | 1.558 | 0.6105 | 0.5131–0.6837 | 0.1767 | 0.1069–0.2664 | 0.221 | 0.418 | 0.611 | 0.558 |
| 1.7006 | 1.667 | 0.5833 | 0.4789–0.6592 | 0.1745 | 0.1051–0.2635 | 0.167 | 0.424 | 0.583 | 0.667 |
| 2.0 | 2.250 | 0.4375 | 0–0.5316 | 0.1693 | 0.1008–0.2563 | −0.125 | 0.438 | 0.438 | 1.250 |
| 2.5 | 3.500 | 0.1250 | 0–0.2947 | 0.1683 | 0.1000–0.2551 | −0.750 | 0.440 | 0.125 | 2.500 |

The mid-main-span strain channel is exactly blind only for $\beta^3+2\beta^2-2=0$, $\beta=0.839287$ (main span shorter than the side spans). For three equal spans it sits **exactly on the band edge**, $N_M=0.2$: the main-span band covers $0.1838\le\eta\le0.5$, i.e. the whole central 63 % of the span.

### 2.4 Strain gauges near interior supports

**The premise needs qualifying.** A gauge *at* the support section is strongly observable: $|N_M|=\mu$ (side normalisation), 0.8–1.6 for practical layouts. Blindness starts when the gauge section is set back from the pier, for example to clear the diaphragm or anchorage zone, or when it is placed at a "quarter-point" section.

T3 gives $N_M$ at distance $d$ from the interior support (prismatic):

| case | 0 | 0.05L | 0.10L | 0.15L | 0.20L | 0.25L | 0.30L | 0.35L | 0.40L |
|---|---|---|---|---|---|---|---|---|---|
| 2-span equal, span 1 | −1.000 | −0.760 | −0.540 | −0.340 | **−0.160** | **0.000** | **0.140** | 0.260 | 0.360 |
| 3-span equal, side | −0.800 | −0.570 | −0.360 | **−0.170** | **0.000** | **0.150** | 0.280 | 0.390 | 0.480 |
| 3-span equal, main | −0.800 | −0.610 | −0.440 | −0.290 | **−0.160** | **−0.050** | **0.040** | **0.110** | **0.160** |
| 3-span β=1.636, side | −1.558 | −1.290 | −1.042 | −0.814 | −0.606 | −0.418 | −0.250 | **−0.103** | **0.025** |
| 3-span β=1.636, main | −0.582 | −0.392 | −0.222 | **−0.072** | **0.058** | **0.168** | 0.258 | 0.328 | 0.378 |

(Bold: inside $|N_M|<0.2$.) The prismatic near-blind ring lies at $d\approx0.14$–$0.32L$ for equal spans and moves away from the pier in the side span of a long-main-span layout ($d=0.32$–$0.49L_s$ at β = 1.636). In the main span it sits at $d\approx0.11$–$0.27L_m$.

**Cancellation ratio of the strain channel** (prismatic, FE influence line):

| location | $R_\varepsilon$ | $R_w$ (deflection) |
|---|---|---|
| 2-span equal, mid span | 0.667 | 0.571 |
| 3-span equal, mid side / mid main | 0.750 / 0.333 | 0.684 / 0.077 |
| β = 1.636: 0.4 side / mid side / mid main | 0.399 / 0.259 / 0.795 | 0.144 / 0.079 / 0.699 |

At every location listed the strain channel cancels less than the deflection channel. The strain influence line is more local (a kink at $m$, with negative lobes only in the adjacent spans).

---

## 3. Haunched girder: Cầu Mây 55 + 90 + 55 m

Model **[A1]**: WP3 inputs. The depth is parabolic over $L_v=44$ m, $I\propto h^n$ with $n=2.9428$, $E=36\,057$ MPa, and the pier rotational springs follow calibrations A ($k=2.748\times10^7$ kN m/rad) and B ($\alpha=0.716$, $k=1.199\times10^8$), as printed in `wp3_run.log`. FE flex elements, $h=0.5$ m. The deflection indicators reproduce manuscript Table 5 (A: 0.1815 / 0.1051 / 0.2088; prismatic: 0.2870 / 0.1632 / 0.7546).

**[A2]** For the absolute strain sensitivity only, $c\propto h$: the neutral axis is assumed to stay at a fixed fraction of the depth, so $(c/EI)(x)/(c/EI)_\text{mid}=(h/h_\text{mid})^{1-n}$, which is 0.207 at the pier face. The blind loci do not depend on [A2].

**Strain blind points** (zeros of $M_q$; x from T5; symmetric):

| model | side-span zero (from abutment) | main-span zero (from pier) | band $\lvert N_M\rvert<0.2$, $x\le100$ m |
|---|---|---|---|
| prismatic, pinned | 33.580 m = 0.6105 $L_s$ | 15.899 m = 0.1767 $L_m$ | 28.25–37.75; 64.75–78.75 |
| haunched, pinned | 25.984 m = 0.4724 | 24.285 m = 0.2698 | 17.25–30.75; 71.25–95.25 |
| haunched, A | 28.825 m = 0.5241 | 25.226 m = 0.2803 | 21.75–33.25; **71.75–100 (to mid-span)** |
| haunched, B | 31.814 m = 0.5784 | 26.268 m = 0.2919 | 25.75–36.25; **72.75–100** |
| haunched, fixed | 33.332 m = 0.6060 | 26.819 m = 0.2980 | 27.75–37.25; **72.75–100** |

(Band edges are on the 0.5 m output grid. A trivial band near each abutment also exists: 0–5.25 m to 0–8.75 m.)

**Gauges: strain versus deflection**

| model | gauge | $N_M$ | $R_\varepsilon$ | $N_w$ ($EI_\mathrm{mid}$) | $R_w$ | $N_{\varepsilon,\text{abs}}$ [A2] |
|---|---|---|---|---|---|---|
| prismatic | N8 0.4L / N8 mid / N7 | 0.337 / 0.221 / 0.418 | 0.40 / 0.26 / 0.79 | 0.287 / 0.163 / 0.755 | 0.14 / 0.08 / 0.70 | = $N_M$ |
| haunched, pinned | " | 0.116 / **−0.055** / 0.212 | 0.14 / −0.07 / 0.65 | 0.030 / −0.052 / 0.248 | 0.02 / −0.04 / 0.51 | 0.100 / −0.040 / 0.212 |
| A | " | 0.199 / **0.048** / 0.193 | 0.31 / 0.08 / 0.73 | 0.182 / 0.105 / 0.209 | 0.18 / 0.11 / 0.59 | 0.172 / 0.035 / 0.193 |
| B | " | 0.286 / 0.157 / 0.173 | 0.66 / 0.46 / 0.88 | 0.476 / 0.377 / 0.234 | 0.56 / 0.49 / 0.77 | 0.247 / 0.115 / 0.173 |
| fixed | " | 0.330 / 0.212 / 0.163 | 1 / 1 / 1 | 0.422 / 0.354 / 0.147 | 1 / 1 / 1 | 0.285 / 0.155 / 0.163 |

At the pier T6 face, $N_M$ = −1.58 to −2.11 on the side face and −0.79 to −0.84 on the main face (haunched). With [A2] the strain indicator becomes −0.33 to −0.44 and −0.16 to −0.17. Measured 5–10 m from the pier, $N_M$ = −0.69 to −1.59 (side) and −0.39 to −0.63 (main). At 20 m: −0.08 to −0.42 (side) and −0.10 to −0.15 (main).

**Reading.**
1. The haunches move every zero-moment point towards mid-span: the side-span zero by up to 7.6 m, the main-span zero by 8.4–10.9 m. The pier stiffness $k$ shifts the side-span zero over 26.0–33.3 m. A strain gauge at mid side span (27.5 m) would be **blind** under calibration A ($N_M=0.048$), change sign with pinned piers (−0.055) and be weak under B (0.157). This mirrors and amplifies the deflection result for the alternative N8 position.
2. The central main span is near-blind for strain in every haunched model: $N_M=0.163$–$0.212$ at N7, and the band reaches mid-span for A, B and fixed piers. As with the deflection channel at N7, this is restraint, not cancellation: $R_\varepsilon=0.65$–$1$. The sagging free moment is largely absorbed by the haunch-attracted pier moments.
3. $N_M$ needs no reference stiffness. This removes the $EI_\mathrm{ref}$ ambiguity of the deflection indicator: the 0.2 threshold now has a fixed meaning, 20 % of the simple-span free moment. The local section enters only as the gain $c/EI$ [A2], which penalises gauges in the deep pier region by a factor of about 5.
4. For this bridge the most robust strain locations are 5–10 m from the piers: $|N_M|\ge0.39$ in all haunched models, and $\ge0.69$ on the side-span side. The end-reaction channel (bearing load cells) gives $N_R=\xi_0=0.47$–$0.61$ and cannot be blind unless the side span loses its sagging zone.

---

## 4. Verification summary (`logs/verify_general.log`)

981 checks, tolerance $10^{-8}$ on the normalised indicators (absolute error of $N$, i.e. relative to the simply supported reference). **All pass.**

| Group | Content | Max error |
|---|---|---|
| A | two-span, 8 $(\rho_L,\rho_{EI})$ pairs, 6 positions, $w,\theta,M,V$ (UDL route) + $\theta,M,V$ (exact IL integral) + 3 reactions (both routes) | 5.1e-11 |
| B | symmetric three-span, 6 $(\beta,\rho)$ pairs, side and main | 4.9e-11 |
| C | asymmetric four- and three-span (three-moment solver) | 8.1e-11 |
| D | zero-moment positions (FE quadratic roots vs Eq. G4), 7 layouts | 4.9e-12 |
| E | 10 closed-form blind configurations (rotation, shear, reaction, strain) and the $N_M=0.2$ band edge at β = 1 | 2.3e-12 |
| F | theorem: two-truck convoy, complete-crossing integral = $P_\mathrm{tot}C_r$ for $w,\theta,M,V,R$, piecewise-prismatic girders with elastic and fixed pier springs | 2.8e-9 (relative) |
| G | Cầu Mây haunched FE (5 models) vs independent force method: $N_M,N_V,N_\theta$, pier moments, reactions, zero positions | 5.4e-10 |

Group F also prints the error of truncating the record when the leader leaves the girder: up to 59 % (rotation) and 10 % (moment) on the two-span example, against at most 0.31 % on the three-span example, where the side-span sensor is far from the truncated tail. The complete-crossing requirement therefore applies to every channel.

Not done: the matched-filter index $O_m$ for the strain channel; a closed form for the haunched girder (the FE is exact up to quadrature).

---

## 5. Draft subsection for the manuscript (insert as Sec. 2.5, ≈ 800 words)

> **2.5. Observability of arbitrary response channels**
>
> Eq. (2) uses no property of the deflection other than linearity. Let $r_m$ be any linear response at a fixed point $m$, measured from the unloaded state: a deflection, a rotation, a bending moment, a fibre strain $\varepsilon=cM/EI$, a shear force or a support reaction. Let $r_m(x)$ be its influence line. For a linear-elastic, time-invariant structure crossed quasi-statically by constant axle loads, and for a complete crossing, the substitution of Eq. (2) gives
>
> $$\int_0^{L+a_\max} y_m\,\mathrm dx = P_\mathrm{tot}\,C_r,\qquad C_r=\int_0^L r_m\,\mathrm du = \frac{r_m[q_0]}{q_0}, \tag{16}$$
>
> where $r_m[q_0]$ is the response to a uniform load over the whole path. The second equality needs only superposition, because a uniform load is a continuous sum of point loads. Maxwell–Betti adds the reading of $r_m(x)$ as the deflected shape under the generalised force dual to $r$ (Müller-Breslau). The hypotheses are those of Section 2.1. Elastic supports, rotational pier springs and any $EI(x)$ are allowed. For a strain gauge, $C_\varepsilon = c_mM_q(x_m)/(EI_m q_0)$. The local section enters only as a gain, so **a strain channel is blind exactly at the zeros of the uniform-load bending-moment diagram**, for any stiffness distribution.
>
> For a prismatic span with end moments written as $m_{l,r}=-8M_{l,r}/(q_0L^2)$, the indicators normalised to the simply supported values are
>
> $$N_M=\frac{8M_q}{q_0L^2}=4\xi(1-\xi)-m_l(1-\xi)-m_r\xi,\qquad N_V=1-2\xi+\tfrac{m_l-m_r}{4},\qquad N_\theta=\frac{24EI\,C_\theta}{L^3}=\Phi'(\xi), \tag{17}$$
>
> with $N_w=8\Phi$ reproducing Eqs. (4) and (8). In the instrumented span of the two-span beam, and in the side span of the symmetric three-span beam, $(m_l,m_r)=(0,\mu)$, and the strain blind point is
>
> $$\xi_0 = 1-\mu/4. \tag{18}$$
>
> For equal two-span beams this gives the familiar $0.75L$. In the main span of the symmetric three-span beam, $m_l=m_r=\mu/\beta^2$, and the blind point lies at $\eta_0=\tfrac12\big(1-\sqrt{1-\mu/\beta^2}\big)$ from the pier: 0.276 for three equal spans and 0.177 for $\beta=1.636$. Deflection blind points exist only in the window $1<\mu<2$. Strain blind points exist in every span that has a sagging zone, i.e. for $\mu<4$. They are a property of every continuous girder, not of particular span ratios.
>
> The near-blind band $|N_M|<0.2$ is a ring around each zero. For an equal two-span beam it covers $0.676<\xi<0.812$, between 0.19 and 0.32 spans from the interior support. A gauge at the support section is well conditioned, with $|N_M|=\mu$. A gauge set back from the pier to clear the diaphragm, or placed at a quarter-point section, falls into the band. In three equal spans the mid-main-span strain lies exactly on the band edge ($N_M=0.2$), and the band covers the central 63 % of the main span. The strain influence line is more local than the deflection line, so at every location examined it cancels less: $R_\varepsilon=0.667$ against $R_m=0.571$ at the mid-span of an equal two-span beam.
>
> The other channels follow from the same diagram. A rotation channel is blind at the extrema of $w_q$. At the interior support it is blind when $\mu=1$: for $\rho_L=1$ in a two-span beam and for $\beta=\sqrt{3/2}$ in a symmetric three-span beam, independently of the stiffness ratio. At the end support it is blind when $\mu=2$, that is at $\rho_L=(1+\sqrt5)/2$ or $\beta=2\cos(\pi/9)$; the latter is the end of the side-span deflection blind locus in Section 2.3. Rotation and shear at the axis of a symmetric girder are always blind. Statics of the end segment gives the end-reaction indicator $N_{R}=2R_A/(q_0L_1)=\xi_0$ for any $EI(x)$. The end reaction is therefore blind only when the end span loses its sagging zone ($\rho_L=(1+\sqrt{13})/2$ or $\beta^3-6\beta-3=0$, $\beta=2.669$). Interior reactions are never blind under a full uniform load.
>
> On a haunched girder the zero-moment points move towards mid-span because the stiff pier regions attract moment. For the Cầu Mây model of Section 4, the side-span zero lies 26.0–33.3 m from the abutment over the range of pier fixity (28.8 m for calibration A, 33.6 m for a prismatic beam). The main-span zero lies 24.3–26.8 m from the pier, against 15.9 m. A strain gauge at mid side span would be blind under calibration A ($N_M=0.048$) and would change sign with pinned piers. At N7 the strain indicator is 0.16–0.21 in every haunched model, close to the deflection indicator of Table 5, with high cancellation ratios ($R_\varepsilon=0.65$–$1$): as for the deflection channel, the cause is restraint rather than cancellation. Unlike $N_m$, the strain indicator needs no reference stiffness. The section enters only through the gain $c/EI$, which reduces the strain signal at the pier face to about one fifth of that at mid-span (assuming $c\propto h$). For this girder the best-conditioned strain locations are 5–10 m from the piers, where $|N_M|\ge0.39$ in all haunched models. All closed forms of this section agree with FE evaluations to better than $10^{-10}$, and the haunched FE agrees with an independent force-method solution to $5\times10^{-10}$ (supplementary script `verify_general.py`).

---

## 6. Figures

- `code/theory2/figures/fig_gc_strain_map_2span.(png|pdf)`: (a) $N_M(\xi,\rho_L)$ with the strain blind locus $\xi_0=1-\mu/4$, the hatched band and the deflection blind locus; (b) strain and deflection blind positions against $\rho_L$ for $\rho_{EI}=0.5,1,2,4$.
- `fig_gc_strain_map_3span`: $N_M$ over $(\beta,\xi)$ for the side span and $(\beta,\eta)$ for the main span, with the strain and deflection blind loci and the Cầu Mây gauges.
- `fig_gc_channels_prismatic`: $N_w,N_\theta,N_M,N_V$ along an equal two-span beam and a prismatic β = 1.636 three-span beam (each span normalised by its own $L$ and $EI$, hence the jumps at the piers).
- `fig_gc_caumay_channels`: Cầu Mây, deflection vs strain indicators along the girder for the prismatic, A and B models, with strain blind points and gauge positions; panel (c) includes the section gain [A2].
