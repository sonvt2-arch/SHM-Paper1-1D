# Hostile audit v2, role 3: tables and figures

Scope: every main figure (Figs 1–7, graphical abstract), every Supplementary figure (Figs S1–S17), all main tables (1–4) and Supplementary tables (S1–S18). Each image was opened. Values read from the figures were checked against the text, the tables and the logs/CSVs named in `code/supplementary/README.md`. Captions were checked against the plotting scripts. I also checked citation order and numbering, and confirmed that the built PDFs contain all 7 + 17 figures and 4 + 18 tables.

## Blocking

### B1. Fig. 6 caption: the newly added note "in (c) L is the main span" is false
- Location: manuscript.md, Fig. 6 caption, last sentence. It reads: "(c) strain indicator including the gain, $N_\varepsilon = N_M\,(c/EI)/(c/EI)_\mathrm{mid}$, that is, the strain constant $C_\varepsilon$ in units of $(c/EI)_\mathrm{mid}L^2/8$ … In (a) and (b) each indicator is normalized by the span containing the sensor, so steps at the piers are changes of scale; in (c) $L$ is the main span."
- Evidence: `code/theory2/gc_figures.py` lines 152–164 compute
  `Lx = np.where((X < 55) | (X > 145), 55.0, 90.0); NM = 8*M/Lx**2` and plot `ax[2].plot(X, NM * sens)`. Panel (c) is therefore $N_M$ (normalized by the span that contains the point: 55 m in the side spans, 90 m in the main span) times the gain ratio. It is not normalized by the main span. The published PNG is byte-identical to the script output (md5 03fd6cd1…), and it shows the steps this produces at both piers in (c): haunched curves jump from about −0.35/−0.39 to about −0.17, and the prismatic curve from about −1.56 (clipped at −1) to −0.58. If $L$ were the main span everywhere, (c) would be continuous at the piers.
- Why it matters: the caption tells the reader that (c) is $C_\varepsilon$ on one common scale, so that side-span and main-span values can be compared directly. That is how Section 5.3 uses it ("their gain c/EI is about one quarter to one third of that at mid-span (Fig. 6c)", and the placement rule ranks by $C_\varepsilon$). As plotted, side-span values are inflated by $(90/55)^2 = 2.68$ relative to main-span values. A haunched side-span value 5–10 m from the pier looks larger in magnitude (about 0.3–0.39) than mid main span (about 0.18–0.20). In true $C_\varepsilon$ units it is smaller (for example 0.39/2.68 ≈ 0.15).
- Fix, one of two:
  - (preferred) In `gc_figures.py`, use `Lx = 90.0` for panel (c) only, regenerate Fig. 6, and keep the caption.
  - Or change the caption to "in (c) also $L$ is the span containing the sensor, so (c) gives $C_\varepsilon$ only within a span; side-span values are $(L_\mathrm{main}/L_\mathrm{side})^2 = 2.68$ times too large relative to the main span". Then recheck the Section 5.3 sentence that relies on Fig. 6c.

## Should-fix

### S1. Fig. 3 caption: "steps at the piers are changes of scale, not discontinuities" is false for the shear indicator, and is wrong for panel (a) as a whole
- Location: manuscript.md, Fig. 3 caption, last sentence. It reads: "Each indicator is normalized by the span containing the sensor, so steps at the piers are changes of scale, not discontinuities."
- Evidence: `gc_figures.py` lines 116–127 normalize each span by its own $L$, so the note is correct for $N_w$, $N_\theta$ and $N_M$. In (b), $N_M$ goes from −1.558 to −0.582, a ratio of $\beta^2$. $N_\theta$ goes from 0.57 to 0.13, a ratio of $\beta^3$. In (a), however, the two spans are equal, so there is no change of scale at all. The only step in (a) is $N_V$ jumping from −1.25 to +1.25, and that is a real discontinuity: the shear jumps by the interior reaction. In (b), the $N_V$ step (−1.39 to +1.00) is mostly the same real jump.
- Fix: "… so steps of $N_\theta$ and $N_M$ at the piers in (b) are changes of scale; the step of $N_V$ is the real jump of shear at a support."

### S2. Fig. 4 caption misdescribes the traces
- Location: manuscript.md, Fig. 4 caption. It reads: "Thin traces: other channels of the same run, unfiltered."
- Evidence: `code/norbwim/nb_fig1.py` lines 28–33. For each gauge in the legend, the script plots the raw re-zeroed record (`lw=0.4, alpha=0.6`) and then `ev.lowpass(yb, fs, 0.5)` (`lw=1.0`, labelled). The thin traces are therefore the same legend gauges unfiltered, not other channels. The labelled traces are low-pass filtered at 0.5 Hz, which the caption never says. The default colour cycle gives each thin trace a different colour from its filtered counterpart, so the reader cannot pair them. The two vertical black lines (first-axle entry and last-axle exit, from `axvline(0)` and `axvline(t_exit - t_entry)`) are not defined either.
- Fix: "Thick lines: the four gauges, low-pass filtered at 0.5 Hz (legend values are the integrals of the unfiltered records); thin lines: the same records unfiltered; vertical lines: entry of the first and exit of the last axle." Ideally also give each thin trace its gauge's colour.

### S3. Main text cites Table S14 (frequencies) for the deflection readings
- Location: manuscript.md, Section 5.1, paragraph 1. It reads: "with means of 5.55 mm at N8 and 15.43 mm at N7 (Supplementary Tables S11, S12 and S14; axle positions in Table S16)".
- Why it is wrong: Table S14 lists the vertical natural frequencies. It does not support the deflection means; Table S12 alone does (I checked that 5.553 and 15.425 are its six-reading means). The citation also makes S14 the first-cited of S13–S15 in the main text.
- Fix: "(Supplementary Tables S11 and S12; axle positions in Table S16)". If frequencies should be mentioned in 5.1, cite S14 in that sentence.

### S4. Table S9 says the day-1 window-length and crossing-residual correlations were "not computed", yet they were computed and one of them is plotted
- Location: supplementary_material.md, Table S9, rows "vehicle-free noise, window length of each crossing" and "crossing residuals", Day 1 column: "–", with the note "–: not computed".
- Evidence: Fig. S11a is exactly the day-1 matrix at T = 58 s. `code/norbwim/logs/v4.log` gives "Day 1 … window T = 58 s … mean off-diagonal r = 0.430" and "day1 12ch … mean off-diag correlation: crossing residuals 0.301 (range −0.51 to 0.99) vs quiet noise 0.418". `results/v4_noise_corr_day1.csv` also has a mean off-diagonal value of 0.430.
- Fix: enter 0.43 and 0.30 in the day-1 column (or 0.30 with the range −0.51 to 0.99), and delete "not computed" where it no longer applies.

### S5. Tables 3 and S15: the "haunched, pinned/fixed" rows report one end of a range without saying which, so they contradict the ratios given in the text
- Location: Table 3 caption ("haunched pinned-pier and fixed-pier rows give the extremes over the haunch-length variants ($L_\mathrm{v}$ = 40–45 m)") and the matching rows in Table S15. Values: N8 pinned 0.023, fixed 0.446; N7 pinned 0.263, fixed 0.145.
- Evidence: `code/theory2/logs/ident_static.log` lines 48–51 give "N8 0.4L: pinned 0.023..0.032 (Lv44 0.030); fixed 0.415..0.446 (Lv44 0.422); N7 mid: pinned 0.244..0.263 (Lv44 0.248); fixed 0.145..0.155 (Lv44 0.147)". The tables show the low end for N8 pinned, the high end for N8 fixed, the high end for N7 pinned and the low end for N7 fixed. Every other haunched row is the $L_\mathrm{v}$ = 44 m base model (not stated either). Supplementary Section S8 then says "going from pinned to fixed piers multiplies the N8 constant by 14.0 but reduces the N7 constant to 0.59". That is correct for $L_\mathrm{v}$ = 44 m (0.422/0.030 and 0.147/0.248), but a reader computing from the table gets 0.446/0.023 = 19.4 and 0.145/0.263 = 0.55.
- Fix: give ranges ("0.023–0.032", "0.415–0.446", "0.244–0.263", "0.145–0.155"), or give the $L_\mathrm{v}$ = 44 m values with the range in a note. State in both captions that the other haunched rows are the base model, $L_\mathrm{v}$ = 44 m.

### S6. Main text cites Fig. 7b for Cramér–Rao bounds that the figure does not show
- Location: manuscript.md, Section 5.3, paragraph 4. It reads: "at the design pier stiffness (Fig. 7b), the Cramér–Rao bound on the standard deviation of $\ln C_8$ falls from 0.87 … to 0.18". Supplementary Section S8 also cites "(Fig. 7b)" for $\alpha^* = 1.07$.
- Why it is wrong: Fig. 7b shows indicators and cancellation ratios along $\alpha^*(\kappa)$. It shows no CRB, no tiltmeter, and no marker for the design stiffness (the A line is drawn only in (a); `ident_static.py` line 212 adds `axvline(K_FE)` only to axis (a)).
- Fix: move "(Fig. 7b)" to a statement the panel supports, or cite `logs/ident_fisher.log` / Supplementary Section S8 for the CRB values. Optionally also draw the A line in (b).

## Minor

- **m1. Fig. S6 / Section S4.** The text says "Eqs. (11) and (12) hold to within 0.6 %". That is true of the pooled ratios in `results/mc_summary.csv` (max 1.0062). Fig. S6c, however, plots the per-axle-count ratios, which reach about 1.007 for GLS (Mây Bridge, 1 axle: 24.105/23.943) and about 1.011 for the single sensor (61.61/60.947). Say "pooled over axle configurations, within 0.6 %; per axle count within about 1 %".
- **m2. Fig. S3 vs Section S3.** "a 20 % rigidity error in the adjacent span then produces configuration-dependent errors of −1.1 % to +2.0 %" does not say which entry-shift range S, or which weighting. Fig. S3c shows defects up to 5.0 % (minimum variance) and 16 % (Σg = 0) at S = 160 m (`logs/multisensor_theory.log`). The 3.1 % spread matches only Σg = 0 at S = 20 m. State "at S = 20 m (Fig. S3a)" and "up to 5–16 % for larger S".
- **m3. Fig. S9.** Truck labels T1–T4 are not defined in the caption, so the reader cannot tell which day-2 truck is 3-axle and which is 5-axle. Add "T1, T2: day-1 3-axle trucks; T3: 3-axle, T4: 5-axle" (check the mapping in `nb_v4.py`).
- **m4. Fig. S13b.** The y axis has no unit (µε m/t, as in (a)). **Fig. S17.** The y label "s (mm)" uses a symbol defined nowhere (the text uses $w$), and (b) has no y label or unit (mm).
- **m5. Fig. S7a.** The pink band (|N_w| < 0.2) is not explained in the caption.
- **m6. Fig. 6c.** The prismatic curve is clipped at −1.0 (`ax[2].set_ylim(-1.0, 1.1)`), and the caption does not say so. Note it in the caption, or widen the limits once B1 is fixed.
- **m7. Table S5.** The caption gives the single load (40.64 N) but neither the totals of the two- and three-load groups (66.99 N, 125.08 N) nor what $x$ means for them (position of the leading load). It also does not say that the two- and three-load columns are measured. Add these.
- **m8. Table 1.** "band" is used in the cells but defined only in the text (|N| < 0.2). Add "band: near-blind band, |N| < 0.2" to the caption.
- **m9. Fig. 7a / Supplementary S8.** S8 lists "rigid pier zone ±1.5 m", which suggests two variants, but Fig. 7a shows five gray curves and `ident_static.log` has a single `Lv44_rigid1.5` variant. Write "rigid pier zone of 1.5 m".
- **m10. Graphical abstract.** The middle panel keeps the sub-panel label "(a) symmetric beam, uniform EI", and the left panel keeps "(a)/(b)". The right panel is headed "pier stiffness controls the side-span constant" but plots the misfit ratio, not the constant. Consider removing the leftover panel letters.

## Checked and found consistent (no finding)

- **Numbering and citation order.** Figs 1–7 and Tables 1–4 are cited in order. Figs S1–S17 and Tables S1–S18 are each cited, numbered without gaps, and first cited in order within the Supplementary Material. The built PDFs contain all 17 Supplementary figures and 18 tables, and 7 + 4 in the main text.
- **Fig. 2.** Blind ratios in (b) at L3/L2 = 1.0 and 1.2 read 0.53 and 0.46, matching the Section S2 values (I recomputed them independently: 0.5258, 0.4614). The blind locus in (a) reaches ξ = 0 at β ≈ 1.88 and ξ = 1 at β = √1.5. The open circle (N_w = 0.163) sits on the edge of the band, inside it.
- **Fig. 3 values.** N_w peak 1.04 at ξ* = 0.42; N_M = 0.5 / −1 / 0 at 0.75; three-span N_M −1.558 / −0.582; N_w(0.4) = 0.287; mid main span 0.755; zero at 0.61.
- **Fig. 6a–b against Table 3, Table S15 and `gc_results.log`.** N8 0.181/0.476/0.287; mid side span 0.105/0.377/0.163; N7 0.209/0.234/0.755; zero-moment points and N_M at N7 agree.
- **Figs 4 and 5 against Tables S6 and S7.** Integration window (±5 s); speeds; ratios and colour classes.
- **Fig. 7 against `ident_static.log`.** Band 1.111; minimum 1.058 at κ = 1.68 × 10⁸; 1.126 at 10⁷; 1.091 at fixity; variant minima 1.039–1.092; admissible κ ≥ 1.78 × 10⁷; indicator ranges.
- **Figs S10 and S11 against Tables S8 and S9** (every value read from the figures matched the tables).
- **Fig. S12.** Zeros at 121.6 m and 190.8 m; gauge constant 0.69 (0.56–0.93).
- **Figs S14 and S15.** Labels A, A′ and B, and the colours for low, base and high mass.
- **Table 4 against `fieldplan_compute.log`.** 0.121, 0.284, −58, −29.
- **Table S12.** Means and standard deviations (4.7 %, 5.0 %).
- **Table S11.** Mean 25.06 t.
- **Table S13 against `ident_static.log`.** All rows.
- **Table S16.** Spacings and distances.
- **Table S17.** I recomputed every entry.
- **Fig. 3 normalization note against the script.** Correct for N_w, N_θ and N_M (see S1 for N_V).

## Count

- Blocking: 1 (B1)
- Should-fix: 6 (S1–S6)
- Minor: 10 (m1–m10)
