# Package 1C: identifiability of girder rigidity and pier stiffness for Cầu Mây, and what the measured frequencies add

Every number in this note comes from one of the scripts in `code/theory2/`; the log that holds it is named in brackets. Run the scripts in this order (about 2 minutes in total):

```
python3 code/theory2/ident_theory.py   # -> logs/ident_theory.log, figures/ident_theory_closedform.png
python3 code/theory2/ident_static.py   # -> logs/ident_static.log, figures/ident_static_kappa_scan.png
python3 code/theory2/ident_freq.py     # -> logs/ident_freq.log, figures/ident_alpha_k_map.png, ident_freq_vs_kappa.png
python3 code/theory2/ident_fisher.py   # -> logs/ident_fisher.log
```

`ident_core.py` re-assembles the WP3 model. It uses the same mesh (10 elements per metre), the same EI(x) law (`wp3_fe.haunch_EI`), the same truck positions (`wp3_run.cm_schemes`) and the same measured values (`wp3_run.MEAS`). The girder stiffness, the pier-spring pattern and a consistent mass matrix are kept separate. Its static predictions match `wp3_fe.Bridge` (5.686 / 17.324 mm at k_FE, C_m = 4.376 × 10⁻⁵ m²/kN). No existing file was modified.

---

## 1. Summary of findings

1. **Structure of the problem.** The stiffness is K(α, k) = αK_g + kK_p. Every static quantity therefore depends on α and k only as (1/α)·g(κ), with κ = k/α, and every frequency as √(α e_d/γ)·f̂(κ). Here γ is the mass scale and e_d = E_dyn/E_stat. The two log-sensitivities obey S_α + S_k = −1 exactly (checked to 10⁻⁶) [ident_theory.log].
2. **Möbius law.** For any mirror-symmetric girder, C_m depends on κ through a single girder constant: C_m(κ) = C_∞ + (C_0 − C_∞)/(1 + κ/k_g). For the Cầu Mây model k_g = 4.36 × 10⁷ kN m/rad. The law holds to a relative error of 5 × 10⁻⁶ over k = 10⁵–10¹² [ident_theory.log].
   - At gauge N8, C_∞/C_0 = 14.0. The N8 constant therefore changes by a factor of 14 between pinned and fixed piers.
   - At gauge N7 the ratio is 0.59.
   - The design calibration k_FE = 2.75 × 10⁷ sits at κ/k_g = 0.63, close to where C_m changes fastest.
3. **Closed form (prismatic, rotational springs at the piers).** Here μ(K) = 1 + β(2β²−3)/(3β + 2ρ + βK), with K = kL_s/EI_s. It is inserted into Eq. (4)/(8) of the manuscript. It reproduces the FE results to 4.4 × 10⁻⁷. |dN/d ln K| peaks at K* = 3 + 2ρ/β = 4.22, which is k_g in this case.
4. **Static data only.** Two readings fix α for each κ, but leave κ unbounded above.
   - The ratio misfit has a minimum of 1.0580 at κ = 1.68 × 10⁸, which is calibration B.
   - At exactly that point the 2 × 2 Fisher matrix is singular, because S_y8 = S_y7 there.
   - With the tolerance τ = 5.27 % (2σ; σ combines the measurement SEM 1.97 % and the model-form spread 1.75 %), the admissible set is κ ≥ 1.78 × 10⁷.
   - Over that set the N8 index (design EI_ref) ranges from 0.124 to 0.822, R_8 from 0.133 to 1.000, and the N7 index from 0.190 to 0.286 [ident_static.log].
5. **Frequencies.** The main-bridge values 3.43, 3.64 and 3.63 Hz cannot be the first vertical mode: matching them would need α ≥ 1.91. They also cannot be mode 2, which is antisymmetric with a node at mid-N7, because the joint set for mode 2 is empty. They are compatible only with mode 3, the first symmetric mode dominated by the side spans (3.26–3.79 Hz over κ at α = 1).
   - **Under the mode-3 interpretation**, calibration B is excluded: f3 = 2.89 Hz with base mass, and at most 3.28 Hz even with the lowest mass and e_d = 1.2.
   - The joint admissible set (with the wide mass and e_d brackets) shrinks to κ = 1.78 × 10⁷ … 1.12 × 10⁸ and α = 0.80 … 1.15.
   - Over it the **N8 index is 0.124–0.390** (R_8 0.133–0.458) and the **N7 index is 0.190–0.222**.
   - With the base mass alone, N8 is 0.124–0.159, close to calibration A′ [ident_freq.log].
   - The selection is conditional, because the report does not identify the mode. The 3.0–3.6 Hz peaks could also be the truck's own bounce.
6. **What would identify κ.** A tiltmeter on pier T7 under the side-span convoy would. At κ = k_FE it cuts the CRB on ln C_8 from 0.865 (two static readings) to 0.177. A properly identified f1 would cut it to 0.237 even with the wide mass prior. A rotation reading at the end bearing T8 adds almost nothing, because its sensitivity copies that of N8 [ident_fisher.log].
7. **Table 5.** The N7 entry of the bound column must read 0.263 … 0.145 (pinned … fixed). Calibration B's N8 value, 0.476, lies outside the bound because the bound uses design EI; normalised by αEI_mid it is 0.341 [ident_static.log].

---

## 2. Theory

### 2.1 Sensitivities of C_m

Let G = K⁻¹ with K = αK_g + kK_p, where K_p has a 1 on each inner-pier rotational degree of freedom. Write C_m = e_mᵀGq, with q the consistent unit uniform load. Then dG/dk = −GK_pG and dG/dα = −GK_gG, so

- dC_m/dk = −Σ_piers θ_{m,i} θ_{q,i}, where θ_{m,i} is the pier rotation under a unit load at the gauge (by Maxwell–Betti, the slope of the gauge's influence line at the pier) and θ_{q,i} is the pier rotation under the uniform load;
- dC_m/dα = −(C_m − kΣθ_mθ_q)/α;
- S_α + S_k = −1, where S_p = ∂ln C_m/∂ln p. This follows from Euler's theorem, because C_m is homogeneous of degree −1 in (α, k).

**Adjoint check against central differences** [ident_theory.log]:

| Gauge | S_k at k_FE: adjoint | S_k at k_FE: FD | S_k at κ = 1.675 × 10⁸ |
|---|---|---|---|
| N8, 0.4L | +0.5115 | +0.5108 | +0.1882 |
| N8, mid | +0.9161 | +0.9148 | +0.2461 |
| N7, mid | −0.1150 | −0.1145 | −0.0990 |

**Boundary-conditioning indicator.** B_m = |∂ln C_m/∂ln κ| is the relative error in C_m caused by a unit relative error in κ = k/α. B_m ≈ 0.5 means that a factor-2 uncertainty in pier stiffness becomes about a 40 % uncertainty in C_m.

### 2.2 Möbius law for a symmetric girder

Write G_0 for the flexibility at k = 0 and split the pier rotations into a symmetric pattern s = (1, 1)/√2 and an antisymmetric pattern a = (1, −1)/√2.

- Mirror symmetry decouples the two patterns: aᵀG_0s = −2.8 × 10⁻¹⁶.
- The symmetric uniform load excites only a.
- The Sherman–Morrison formula then gives C_m(κ) = C_∞ + (C_0 − C_∞)/(1 + κ g_a), with g_a = aᵀG_0a = 1/k_g.
- The log-sensitivity is S_κ = −κg_a(C_0 − C_∞)/[(1 + κg_a)² C_m].

Values from the Cầu Mây model [ident_theory.log]:

| Gauge | C_0 (m²/kN) | C_∞ (m²/kN) | C_∞/C_0 |
|---|---|---|---|
| N8, 0.4L | 7.27 × 10⁻⁶ | 1.016 × 10⁻⁴ | 13.99 |
| N8, mid | −1.25 × 10⁻⁵ | 8.53 × 10⁻⁵ | −6.82 (sign change: the blind state is crossed) |
| N7, mid | 4.29 × 10⁻⁴ | 2.54 × 10⁻⁴ | 0.592 |

The ratio C_∞/C_0 is a second, global conditioning measure. It is the full range that pier fixity can produce.

### 2.3 Closed form: symmetric prismatic three-span beam with rotational springs

Slope-deflection at pier B, using symmetry (θ_C = −θ_B) and joint equilibrium M_BA + M_BC + kθ_B = 0, gives

θ_B = qL_s³(2β² − 3) / [24EI_s(3 + 2ρ/β + K)],

μ = 1 + β(2β² − 3)/(3β + 2ρ + βK) (side-span hogging moment, −μqL_s²/8),

N_side(ξ) = 8F(ξ, μ(K)) (Eq. 4 unchanged),

ν = (2/3)[1 − ρ(2β² − 3)/(β²(3β + 2ρ + βK))], N_main(½) = 2.5 − 3ν (normalised with EI_m, L_m).

Limits: K = 0 recovers Eq. (8); K → ∞ gives μ = 1 (propped cantilever) and ν = 2/3 (fixed–fixed).

At β = 1.636 and ρ = 1 [ident_theory.log]:

- N_side(0.4) rises from 0.287 at K = 0 to 1.037 at K → ∞.
- N_side(0.5) rises from 0.163 to 1.000.
- N_main falls from 0.7546 to 0.500.
- The blind spring stiffness K_crit = [β(2β² − 3)/(μ_crit − 1) − 3β − 2ρ]/β is negative for both side-span positions. Rotational restraint therefore always moves this layout away from the blind locus.
- Because N_side is a Möbius function of K, |dN/d ln K| peaks at K* = 3 + 2ρ/β = 4.222. There ∂ln C/∂ln K = 0.283 (ξ = 0.4) and 0.360 (ξ = 0.5).

FE agreement over K = 0 … 10⁴ is within 4.4 × 10⁻⁷ (figure `ident_theory_closedform.png`).

### 2.4 Fisher information

Parameters: θ = (ln α, ln κ, ln γ′), with γ′ = γ/e_d.

Log-observation rows:

| Observation | Row |
|---|---|
| static gauge | [−1, S_j, 0] |
| frequency | [½, S_f, −½] |
| rotation | [−1, S_r, 0] |

- **(a) Two static readings.** The 2 × 2 Fisher matrix has det ∝ (S_y8 − S_y7)², so sd(ln κ) = √2σ/|S_y8 − S_y7|.
- **(b) Static readings plus a frequency.** This adds a row, but a frequency carries the nuisance γ′, so it informs κ only through a prior on γ′. The frequency ratios f_i/f_j depend on κ alone, so two identified modes would remove γ′.
- **(c) Static readings plus a rotation.** This adds a row with no nuisance.

---

## 3. Assumptions and sources

| # | Item | Value used (bracket) | Source / status |
|---|---|---|---|
| S1 | E_c | 36 057 MPa | LRFR pdf p.4 (`section_properties.csv`) |
| S2 | I_mid, I_pier (vertical) | 5.482, 59.612 m⁴ | LRFR pdf p.5 |
| S3 | Depth law, haunch length | parabolic, L_v = 44 m (40, 45) | **[NEED VALUE]**, WP3 assumption |
| S4 | I ∝ hⁿ | n = 2.943 (2.5, 3.2 tested) | fitted to S2; variants test editor concern 4 |
| S5 | Pier rigid zone | none (±1.5 m rigid tested) | **[NEED VALUE]** diaphragm width |
| S6 | Truck loads, positions | nominal 5 + 10 + 10 t, `wp3_run.cm_schemes` | report; weighed mean changes ratios ≤ 0.003 (manuscript §4.2) |
| S7 | Measured deflections | mean of 6: 5.5533 / 15.4250 mm; rel. SEM 1.90 / 2.04 % | `cau-may_main_static_deflection.csv` |
| S8 | Model-form σ per gauge | 1.75 % (half-range of ln(pred8/pred7) over S3–S5 variants, 4.95 %, divided by 2√2) | this work [ident_static.log] |
| M1 | A_mid, A_pier, A_on-pier, A_over-T5/T8 | 7.233, 14.437, 29.945, 16.127 m² | LRFR pdf p.5 |
| M2 | A(h) between sections | linear in h (low case: power law, p = 0.852) | assumption |
| M3 | Concrete density incl. steel | 2.50 t/m³ (2.40–2.55) | AASHTO LRFD/TCVN 11823-3 Tab. 3.5.1-1 normal-weight concrete ≈ 2.35 t/m³ at f′c = 45 MPa plus a reinforcement/tendon allowance; 2.50 is the customary design value. **[NEED VALUE]** from the design calculation |
| M4 | Wearing surface | 2.25 t/m³ × 0.07 m (0.05–0.10) × 11.0 m | density AASHTO Tab. 3.5.1-1 (bituminous); thickness **[NEED VALUE]**; width INVENTORY §1 (12 m − 2 × 0.5 m kerbs) |
| M5 | Kerb + railing/barrier | 0.5 t/m per side (0.3–1.0) | **[NEED VALUE]** |
| M6 | Pier / end diaphragms | 3.0 m / 2.0 m at A_on-pier / A_over-T5/T8 (omitted in low case) | **[NEED VALUE]** lengths; negligible effect (vertical dof fixed there) |
| M7 | Resulting mass | low 4878 t (24.39 t/m), base 5484 t (27.42 t/m), high 5932 t (29.66 t/m); γ = 0.889 / 1 / 1.082 | [ident_freq.log] |
| D1 | Measured vertical f | N6 3.43, N7 3.64, N8 3.63 Hz (mean 3.567, sd 3.3 %); approaches 3.03–3.11 Hz | PDF Bảng 2.15 (`cau-may_span_dynamic_properties.csv`); mode not identified in report; sampling rate **[NEED VALUE]** |
| D2 | E_dyn/E_stat | 1.0–1.2 | assumption (typical literature range for concrete); **[NEED VALUE]** citable source |
| D3 | Neglected | shear deformation, rotary inertia, pier mass, vertical pier/bearing flexibility, shear lag | as in WP3 |
| F1 | σ static (CRB) | 2.64 % per gauge (= τ_rec/2) | S7 + S8 |
| F2 | σ frequency | 3.3 % | spread of D1 |
| F3 | σ rotation | 3 % of ≈ 100–380 µrad | **[NEED VALUE]** instrument |
| P1 | Pier k (illustrative) | 5.8 × 10⁶ – 1.8 × 10⁸ kN m/rad from cE_p bt³/(12H), E_p 30 GPa, b 6–9 m, t 1.8–2.5 m, H 8–15 m, c 1–4 | **[NEED VALUE]** pier drawings; illustration only, does not discriminate A from B |

The mesh check at k_FE gives identical f1–f4 for 5 and 10 elements per metre (1.4271, 2.5409, 3.2876, 4.9457 Hz).

---

## 4. Results

### 4.1 Static data: ratio misfit and admissible set

All values from [ident_static.log] and `ident_static_kappa_scan.png`. Here α* is the best-fit α for each κ.

| κ (kN m/rad) | ρ = (m/p)_N8 / (m/p)_N7 | α* | Residual ± | N8 index (αEI_mid) | R_8 | N7 index | R_7 |
|---|---|---|---|---|---|---|---|
| 1.0 × 10⁷ | 1.1255 | 1.238 | 5.91 % | 0.103 | 0.088 | 0.229 | 0.540 |
| 2.82 × 10⁷ (≈ A) | 1.0960 | 1.067 | 4.59 % | 0.184 | 0.187 | 0.208 | 0.588 |
| 1.68 × 10⁸ (B, minimum) | 1.0580 | 0.716 | 2.82 % | 0.341 | 0.556 | 0.168 | 0.772 |
| 1.0 × 10⁹ | 1.0767 | 0.559 | 3.69 % | 0.405 | 0.880 | 0.151 | 0.938 |
| 10¹² (fixed) | 1.0913 | 0.517 | 4.37 % | 0.422 | 1.000 | 0.147 | 1.000 |

This reproduces the editor's numbers: 1.126, 1.097, 1.058 and 1.09. The three calibrations re-computed:

| Calibration | Misfit N8 / N7 | N8 (design ref) | N8 mid | N7 | R_8 | R_7 | C_8 (m²/kN) | C_7 (m²/kN) |
|---|---|---|---|---|---|---|---|---|
| A (design EI, k_FE) | +2.4 / +12.3 % | 0.181 | 0.105 | 0.209 | 0.183 | 0.586 | 4.376 × 10⁻⁵ | 3.610 × 10⁻⁴ |
| A′ (α = 1.088, k_FE) | −4.6 / +5.0 % | 0.160 | 0.089 | 0.194 | 0.172 | 0.581 | 3.850 × 10⁻⁵ | 3.350 × 10⁻⁴ |
| B (α = 0.716, k = 1.199 × 10⁸) | −2.8 / +2.9 % | 0.476 | 0.377 | 0.234 | 0.556 | 0.772 | 1.147 × 10⁻⁴ | 4.047 × 10⁻⁴ |

**Model-form variants** (ρ_min and its κ):

| Variant | ρ_min | at κ |
|---|---|---|
| L_v 40 | 1.0442 | 1.33 × 10⁸ |
| L_v 44 | 1.0580 | 1.68 × 10⁸ |
| L_v 45 | 1.0617 | 1.78 × 10⁸ |
| n = 2.5 | 1.0916 | 2.00 × 10⁸ |
| n = 3.2 | 1.0391 | 1.58 × 10⁸ |
| rigid zone ±1.5 m | 1.0539 | 1.33 × 10⁸ |

No variant reaches ρ = 1. The residual gauge-ratio error of 4–9 % is therefore a model-form error and not a calibration choice.

**Admissible sets**, base model. The criterion is max_j |ln(meas/pred)| ≤ τ, with α and κ free.

| τ | κ | α | N8 (design ref) | N8 (αEI_mid) | R_8 | N7 (design ref) | R_7 |
|---|---|---|---|---|---|---|---|
| 3 % | 1.00 × 10⁸ – 2.99 × 10⁸ | 0.642–0.804 | 0.376–0.579 | 0.303–0.372 | 0.430–0.689 | 0.221–0.249 | 0.709–0.839 |
| 4 % | 4.22 × 10⁷ – 2.0 × 10⁹ | 0.539–0.984 | 0.226–0.767 | 0.223–0.413 | 0.249–0.936 | 0.201–0.276 | 0.619–0.967 |
| 5 % | ≥ 2.24 × 10⁷ | 0.514–1.113 | 0.146–0.820 | 0.163–0.422 | 0.158–1.000 | 0.192–0.285 | 0.574–1.000 |
| **5.27 % (= 2σ, recommended)** | **≥ 1.78 × 10⁷** | **0.513–1.153** | **0.124–0.822** | **0.144–0.422** | **0.133–1.000** | **0.190–0.286** | **0.562–1.000** |
| 6 % | ≥ 9.44 × 10⁶ | 0.509–1.245 | 0.080–0.828 | 0.100–0.422 | 0.084–1.000 | 0.185–0.288 | 0.538–1.000 |
| 8 % | whole range | 0.499–1.385 | 0.028–0.845 | 0.039–0.422 | 0.029–1.000 | 0.177–0.294 | 0.511–1.000 |

Across the model-form variants at τ = 5.27 %, the ranges widen to N8 (design ref) 0.052–0.833, R_8 0.053–1.000 and N7 0.173–0.291.

Because ρ(∞) = 1.091 lies inside 2τ, the static data bound κ only from below. Two quantities set the upper end of the N8 range:

- the pier-fixity limit;
- the implausible α ≈ 0.51 needed to fit there. That is why the design-referenced index reaches 0.82.

With a physical prior α ∈ [0.9, 1.3] (editor concern 3), the admissible set is κ = 1.78 × 10⁷ … 6.68 × 10⁷. Over it N8 = 0.124–0.297, R_8 = 0.133–0.339 and N7 = 0.190–0.211 [ident_freq.log].

### 4.2 Frequencies

All values from [ident_freq.log], `ident_freq_vs_kappa.png` and `ident_alpha_k_map.png`.

**Model modes** at α = 1 with base mass, over κ = 10⁶ … 10¹²:

| Mode | Type | Frequency range |
|---|---|---|
| f1 | symmetric (S), centre-span dominated | 1.19–2.48 Hz |
| f2 | antisymmetric (A) | 2.33–3.79 Hz |
| f3 | symmetric (S), side spans | 3.26–3.79 Hz |

At k_FE the normalised amplitudes at mid-N6 / mid-N7 / mid-N8 are:

| Mode | N6 | N7 | N8 |
|---|---|---|---|
| 1 | 0.41 | 1.00 | 0.41 |
| 2 | 0.95 | 0.00 | 0.95 |
| 3 | 0.88 | 0.77 | 0.88 |

Mode 3 is the only mode in the 3–4 Hz range that the three mid-span vibration points would all record at a common frequency.

**α required for the mean measured value of 3.567 Hz**, over κ and the mass brackets:

| Mode | α required | Verdict |
|---|---|---|
| 1 | 1.91–9.78 | impossible |
| 2 | 0.82–2.56 | needs high κ, where the static valley requires α ≈ 0.5–0.6; joint set empty |
| 3 | 0.82–1.31 | compatible |

**Joint sets** at τ = 5.27 %:

| Information used | κ | α | N8 (design ref) | N8 (αEI_mid) | R_8 | N7 | R_7 | C_8 (m²/kN) |
|---|---|---|---|---|---|---|---|---|
| static only | ≥ 1.78 × 10⁷ | 0.513–1.153 | 0.124–0.822 | 0.144–0.422 | 0.133–1.000 | 0.190–0.286 | 0.562–1.000 | 3.0 × 10⁻⁵ – 1.98 × 10⁻⁴ |
| + prior α ∈ [0.9, 1.3] | 1.78 × 10⁷ – 6.68 × 10⁷ | 0.900–1.153 | 0.124–0.297 | 0.144–0.267 | 0.133–0.339 | 0.190–0.211 | 0.562–0.663 | 3.0 × 10⁻⁵ – 7.15 × 10⁻⁵ |
| + f3 ∈ [3.43, 3.64], mass low…high, e_d 1.0–1.2 | 1.78 × 10⁷ – 1.12 × 10⁸ | 0.801–1.153 | **0.124–0.390** | 0.144–0.312 | **0.133–0.458** | **0.190–0.222** | 0.562–0.723 | 3.0 × 10⁻⁵ – 9.39 × 10⁻⁵ |
| + f3, base mass, e_d = 1 | 1.78 × 10⁷ – 2.51 × 10⁷ | 1.090–1.153 | 0.124–0.159 | 0.144–0.173 | 0.133–0.171 | 0.190–0.194 | 0.562–0.581 | 3.0 × 10⁻⁵ – 3.83 × 10⁻⁵ |
| + f1 or f2 hypothesis | empty | | | | | | | |

**Along the static valley α*(κ), with base mass:**

| κ | f3 (base) | f3 (low mass) | f3 (high mass) |
|---|---|---|---|
| 1 × 10⁷ | 3.636 Hz | | |
| 2.8 × 10⁷ | 3.397 Hz | | |
| 1 × 10⁸ | 3.013 Hz | | |
| 1.68 × 10⁸ (B) | 2.888 Hz | 2.998 Hz | 2.760 Hz |

At B, even e_d = 1.2 lifts the low-mass value only to 3.28 Hz, which is below 3.43 Hz.

**Honest reading of the frequency result:**

1. **Mass uncertainty does not prevent the selection.** The mass bracket is −11/+8 % and enters f only as a square root. Most of the selective power comes instead from the fact that the static valley trades α against κ: high κ needs α ≈ 0.6–0.7, which pushes f3 down to 2.7–3.0 Hz.
2. **The weak link is mode identification.** The report tabulates one frequency per span without mode shapes. All seven spans, including the 38 m simply supported approaches, give 3.0–3.6 Hz, and that also fits a truck-bounce response. If the peaks are not structural, the frequency row must be dropped. The admissible range then falls back to the static set: with the α-prior, 0.124–0.297; without it, 0.124–0.822.
3. **The selected region sits at the edge of the static tolerance.** The static residual there is 4.6–5.3 %, against 2.8 % at B. The frequencies and the two static readings are therefore only marginally consistent within the stated model.

### 4.3 Local identifiability (CRB, 1σ in log units)

All values from [ident_fisher.log].

| Information | κ = 2.75 × 10⁷ (A): sd ln κ | sd ln C_8 | sd ln C_7 | κ = 1.68 × 10⁸ (B): sd ln κ | sd ln C_8 |
|---|---|---|---|---|---|
| (a) y8, y7 | 1.241 | 0.865 | 0.090 | singular | — |
| (b) + f3, wide γ′ prior (sd 0.109) | 0.657 | 0.456 | 0.048 | 0.925 | 0.367 |
| (b) + f3, γ′ known to 3 % | 0.422 | 0.291 | 0.031 | 0.537 | 0.210 |
| (b′) + f1 + f3 (if f1 identified), wide prior | 0.339 | 0.237 | 0.030 | 0.362 | 0.145 |
| (c) + rotation at T8 bearing | 0.829 | 0.571 | 0.054 | 1.216 | 0.476 |
| (c) + rotation at pier T7 | 0.239 | 0.177 | 0.031 | 0.068 | 0.040 |

**Log-sensitivities** (∂ln/∂ln κ at k_FE): y8 −0.171, y7 −0.201, C_8 +0.511, C_7 −0.115, f1 +0.141, f3 +0.009, rotation at T8 −0.154, rotation at T7 −0.330.

- f3 is almost insensitive to κ. It informs κ only through α and the absolute static level, which is why its value depends on the mass prior.
- The T7 rotation is about 167 µrad under scheme III at A.

**Shape factor for BPM.** C_8 divided by the modelled N8 deflection varies by a factor of 6.49 over the static admissible set, 3.04 with f3 (wide brackets) and 1.27 with f3 (base mass). For N7 the factors are 1.51, 1.20 and 1.03. Calibrating a model to the N8 reading therefore does not fix the N8 constant.

### 4.4 Table 5 bound column (corrected)

All values from [ident_static.log]: design EI, L_v 40/44/45.

| Gauge | Pinned (range over L_v) | Fixed (range over L_v) | Column should read (pinned … fixed) |
|---|---|---|---|
| N8, 0.4L | 0.023 – 0.032 | 0.415 – 0.446 | 0.023 … 0.446 |
| N8, mid | −0.066 – −0.049 | 0.349 – 0.375 | −0.066 … 0.375 |
| N7, mid | 0.244 – 0.263 | 0.145 – 0.155 | **0.263 … 0.145** (manuscript prints 0.145 … 0.263) |

The caption should add the following. The bound uses design EI. Calibration B's N8 = 0.476 lies outside the bound because α = 0.716 reduces EI_eff but not EI_ref; with EI_ref = αEI_mid, B gives 0.341, inside the bound.

---

## 5. Draft replacement for manuscript §4.3–4.4 (English, about 990 words)

> **4.3. Observability of the installed gauges and its identifiability**
>
> The prismatic closed form already places this layout near the blind locus: with uniform rigidity, Eq. (8) gives $N_m = 0.163$ at mid side span and 0.287 at the installed position $\xi = 0.4$. Monolithic piers add a rotational restraint $k$. Slope-deflection at the pier then replaces $\mu$ of Eq. (8) by $\mu(K) = 1 + \beta(2\beta^2-3)/(3\beta+2\rho_{EI}+\beta K)$, $K = kL_s/EI_s$, which reproduces FE values to $4\times10^{-7}$. For $\beta = 1.636$ the side-span index rises from 0.287 (pinned) to 1.037 (fixed) at $\xi = 0.4$, while the mid main-span index falls from 0.755 to 0.500. Restraint moves the side-span gauge away from blindness but makes its constant strongly $k$-dependent.
>
> For the haunched girder the same structure holds exactly. The stiffness is $\alpha K_g + kK_p$, where $\alpha = EI_\mathrm{eff}/EI_\mathrm{design}$, so every static response scales as $\alpha^{-1}g(\kappa)$ with $\kappa = k/\alpha$. Mirror symmetry leaves one pier-rotation pattern active under a uniform load. Hence $C_m(\kappa) = C_\infty + (C_0-C_\infty)/(1+\kappa/k_g)$, where $k_g = 4.36\times10^7$ kN m/rad is the girder's own antisymmetric pier stiffness. At the installed side-span gauge N8, $C_\infty/C_0 = 14.0$; at the centre-span gauge N7 it is 0.59. We use $B_m = |\partial\ln C_m/\partial\ln\kappa| = \kappa|\sum\theta_{m,i}\theta_{q,i}|/|C_m|$ as a boundary-conditioning indicator. Here $\theta_{m,i}$ and $\theta_{q,i}$ are the pier rotations under a unit load at the gauge and under the uniform load. At the design-model stiffness $k_\mathrm{FE} = 2.75\times10^7$ kN m/rad, $B_m$ is 0.51 at N8 and 0.12 at N7.
>
> For any $\kappa$ the two acceptance readings fix $\alpha$; they constrain $\kappa$ only through the ratio $\rho(\kappa)$ of the measured-to-model ratios at N8 and N7. That ratio never reaches 1. It falls from 1.126 at $\kappa = 10^7$ to a minimum of 1.058 at $\kappa = 1.68\times10^8$ and returns to 1.091 for fixed piers. The minimum is the joint least-squares fit (calibration B: $\alpha = 0.716$, $k = 1.2\times10^8$ kN m/rad). Because $\rho$ is stationary there, the Fisher information of the two readings is singular at exactly that point. Variants of the haunch length, the depth–inertia exponent and a rigid pier zone move the minimum between 1.039 and 1.092 but never to 1. The 4–9 % gauge-ratio residual is therefore model-form error, not a calibration choice.
>
> We therefore report the admissible range instead of two calibrations. The relative standard error of each mean reading is 1.9–2.0 %, and the model-form spread adds 1.75 % per gauge. A 2σ tolerance of 5.3 % on both gauges admits every $\kappa \ge 1.8\times10^7$ kN m/rad. Over this set the N8 index (design $EI_\mathrm{mid}$) lies between 0.12 and 0.82 and $R_m$ between 0.13 and 1.00. The upper part of this range requires $\alpha \approx 0.5$–0.7, a 30–50 % loss of rigidity in a young, uncracked prestressed girder, which we consider implausible. Restricting $\alpha$ to 0.9–1.3 leaves $\kappa = 1.8$–$6.7\times10^7$, with an N8 index of 0.12–0.30 and $R_m$ of 0.13–0.34. The N7 index stays between 0.19 and 0.29 over the whole static set, and between 0.19 and 0.21 under the prior.
>
> The vertical frequencies measured at mid-span (3.43, 3.64 and 3.63 Hz in N6, N7 and N8) add an independent constraint once a mass model is assumed. We used box self-weight, surfacing and barriers (24.4–29.7 t/m) and a dynamic-to-static modulus ratio of 1.0–1.2. These values cannot be the first vertical mode, which lies at 1.2–2.5 Hz in the model and would need $\alpha > 1.9$. Nor can they be the antisymmetric mode, which has a node at mid-N7 and is inconsistent with the static set. They match the first symmetric side-span mode (3.26–3.79 Hz at $\alpha = 1$). Under this interpretation calibration B is excluded: it predicts 2.89 Hz, and at most 3.28 Hz at the lightest mass and stiffest dynamic modulus. The joint admissible set becomes $\kappa = 1.8\times10^7$–$1.1\times10^8$ kN m/rad and $\alpha = 0.80$–1.15. The N8 index then lies between 0.12 and 0.39 ($R_m$ 0.13–0.46) and the N7 index between 0.19 and 0.22; with the central mass estimate alone the N8 range narrows to 0.12–0.16. Mass uncertainty does not limit this result (±10 % mass moves the frequency by ±5 %); mode identification does. The test report gives one frequency per span without mode shapes, and the approach spans show similar values (3.0–3.1 Hz), so a vehicle-dominated response cannot be ruled out. The frequency-based narrowing is therefore conditional.
>
> **Table 5** keeps the pinned … fixed bounds (N8: 0.023 … 0.446; mid side span: −0.066 … 0.375; N7: 0.263 … 0.145) and adds the admissible ranges above. Calibration B's N8 value of 0.476 lies outside the bound because the bound uses design $EI$; normalised by $\alpha EI_\mathrm{mid}$ it is 0.341.
>
> **4.4. Implications for BPM and SLM**
>
> The side-span constant cannot be taken from a design model, and calibrating the model to the side-span reading does not fix it either. Over the static admissible set, the ratio of $C_m$ to the modelled N8 deflection varies by a factor of 6.5. With the frequency constraint the factor is still 3.0. The centre-span constant is robust: the same ratio varies by 1.51 and 1.20, and the N7 index by less than ±10 % under the prior. In the joint set the absolute N7 constant spans $3.3$–$3.8\times10^{-4}$ m²/kN. SLM removes the dependence on $\alpha$ and $k$ altogether, provided that the response is linear, but it does not remove the residual-offset term, which remains large at N8 (Section 6.2).
>
> If a model-based constant is wanted, the most effective additional measurement is a tiltmeter on the monolithic pier T7. Under the side-span convoy it would read about 170 µrad. Added to the two deflections, it would reduce the Cramér–Rao standard deviation of $\ln C_m$ at N8 from 0.87 to 0.18. An identified first vertical frequency would reduce it to 0.24, whereas a rotation reading at the end bearing adds little, because its sensitivity duplicates that of N8. The criterion is most useful before installation: on this bridge a gauge in the centre span would have avoided the problem.

Word count of the quoted draft: about 990 words.

---

## 6. Limits of this analysis

- **Linear model.** The analysis uses a 2D Euler–Bernoulli model. Shear lag, transverse distribution and shear deformation are absorbed in α and κ, and the model-form variants cover only L_v, n and a rigid zone.
- **Pier springs.** The two pier springs are assumed equal, so symmetry is imposed. Unequal T6/T7 stiffness would bring in the symmetric pier mode, which the Möbius result does not cover. Its effect on C_m is zero under the uniform load only if the piers are equal.
- **Mode identification.** The frequency conclusion depends on the mode-3 interpretation (§4.2). Re-analysing the raw SDA-830C records, if they can be obtained, to find a peak at 1.4–1.7 Hz at mid-N7 would test the interpretation. Such a peak would also supply the f1 that the CRB analysis shows to be valuable.
- **CRB bounds.** These are local. The valley is curved and long, so the admissible-set ranges in §4.1–4.2 are the primary result.
- **Inputs still needed.** All quantities marked [NEED VALUE] in §3 remain open: pier drawings, diaphragm lengths, surfacing and barrier weights, sampling rate, and a citable E_dyn/E_stat ratio.
