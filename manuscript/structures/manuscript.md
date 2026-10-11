# Total-load observability of continuous girder bridges from a single deflection channel: closed-form blind configurations, laboratory verification and application to an in-service box-girder bridge

Quoc-Bao Nguyen^a^, Thai-Son Vu^a,\*^, Hung-Son Nguyen^a^

^a^ Faculty of Bridge and Road Engineering, Hanoi University of Civil Engineering, 55 Giai Phong, Bach Mai ward, 11618 Ha Noi, Viet Nam

\* Corresponding author: Thai-Son Vu. Tel.: +84 971 899 888. E-mail: sonvt2@huce.edu.vn

E-mail addresses: baonq@huce.edu.vn (Q.-B. Nguyen), sonvt2@huce.edu.vn (T.-S. Vu), sonnh@huce.edu.vn (H.-S. Nguyen)

---

## Abstract

Influence-area bridge weigh-in-motion estimates gross vehicle weight from the area under a single response record. On continuous girders the influence line changes sign, and a sensor may then record no net area at all. This paper asks when one deflection channel can observe the total load. For a linear-elastic beam the deflection integral over a complete crossing equals the total load times a constant $C_m$, and by reciprocity $C_m$ is the sensor deflection under a uniformly distributed unit load. This gives closed forms for two- and three-span beams. For a two-span beam with uniform stiffness the blind span ratio is $(3+\sqrt{33})/6 = 1.45743$. For a symmetric three-span beam instrumented at mid side span it is the root of $6\beta^3-15\beta-4=0$, $\beta = 1.700594$, and beyond $\beta = 2\cos(\pi/9) = 1.879385$ no side-span position gives a positive constant. Laboratory tests on a two-span steel beam with statically positioned loads identified two- and three-load groups within 1.19 % by the beam-property method and 0.70 % by the standard-load method. The criterion was applied to the acceptance-test data of a 55 + 90 + 55 m box girder. Its side-span gauge is near-blind: the centre span cancels 82 % of the positive influence area, and $C_m$ changes about fourteenfold between pinned and fixed piers. This application is a static consistency check, not a validation of the integral on a continuous bridge. An error budget, supported by field crossing records, identifies baseline drift as the dominant error. The indicator $|C_m|$, with the cancellation ratio for haunched girders, is proposed as a pre-installation check.

**Keywords:** Bridge weigh-in-motion; Continuous girder; Deflection integral; Load observability; Sensor placement; Measurement uncertainty

---

## Nomenclature

| Symbol | Meaning |
|---|---|
| $A^+$, $A^-$ | positive and negative parts of the area under $\eta_m$ (mm²/N) |
| $C_m$ | invariance constant at sensor $m$, the signed area under $\eta_m$ (mm²/N) |
| $EI$, $EI_\mathrm{ref}$ | flexural rigidity; reference rigidity used for normalisation (N mm²) |
| $I_y$ | deflection integral over a complete crossing (mm²) |
| $L_1$, $L_2$ | instrumented and adjacent span of a two-span beam (mm) |
| $L_s$, $L_m$ | side and main span of a symmetric three-span beam (m) |
| $L_\mathrm{tot}$ | length of the integration record (mm) |
| $N_m$ | normalised indicator $192EI_\mathrm{ref}C_m/L^4$ |
| $P_\mathrm{tot}$, $P_0$, $P_t$ | total load; reference load; unknown load (N) |
| $R_m$ | cancellation ratio $C_m/A^+$ |
| $T_\mathrm{cr}$, $T_1$ | crossing time; fundamental period (s) |
| $v$ | traverse speed (mm/s) |
| $\beta$ | span ratio $L_m/L_s$ |
| $\gamma$ | relative gain error of the deflection chain |
| $\varepsilon_0$ | zero offset of the deflection signal (mm) |
| $\eta_m(x)$ | deflection influence line at $m$ (mm/N) |
| $\mu$, $\nu$ | interior-moment parameters, Eqs. (5), (8) |
| $\xi$ | sensor position as a fraction of the instrumented span |
| $\rho_L$, $\rho_{EI}$ | span ratio and stiffness ratio, adjacent span over instrumented span |
| BPM, SLM | beam-property method; standard-load method |

---

## 1. Introduction

Heavy vehicles above the design envelope shorten the life of highway bridges and, in extreme cases, contribute to collapse. A span of the Yangmingtan Bridge failed in 2012 under four overloaded trucks crossing together [1]. In other well-documented failures, heavy traffic acted together with design deficiencies or material degradation [2–4]. Knowing the loads that a bridge actually carries is therefore part of risk-informed asset management [5,6].

Pavement weigh-in-motion (WIM) is a mature technology [7,8] with codified accuracy classes [9], but stations are costly to install and maintain [10], coverage is sparse, and a pavement station weighs the vehicle rather than loading any particular bridge. Bridge weigh-in-motion (BWIM), introduced by Moses [11], instruments the structure and fits the measured response to the sum of axle loads times influence-line ordinates; it requires axle spacings and speed. The approach now includes influence lines calibrated from measurements [12], regularised solutions [13], systematic accuracy improvements [14,15], contactless variants [16] and virtual-axle methods that avoid axle detectors [17]. In parallel, moving-force identification recovers the axle-load history in the time or frequency domain [18–20], on multi-span bridges with elastic bearings [21], and with dynamic axle loads [22], steepest-descent [23], Bayesian [24], Kalman-filter [25] and physics-informed machine-learning [26] formulations. These methods aim at axle loads and need several sensors, a structural model or a regularised inversion.

A simpler family estimates only the gross weight from the area under the measured response. Ojio and Yamada, as described by Cardini and DeWolf [27], multiply the area under the strain–time record by the speed to obtain an "influence area" and calibrate it against a truck of known weight. Related strain-area and strain-integral formulations have since been proposed [28–31], simplified BWIM without axle detectors has been verified in the field [32], and the same idea has been applied to support reactions measured by load cells [33]. The integral of the displacement influence line has also been used as a damage feature, where the ratio of two sensors removes the load [34], and area-ratio features of the influence line have been applied to a two-span bridge for defect diagnosis [35]. The present authors earlier used the integral of the mid-span deflection to identify the total load on a simply supported beam [36], where the influence line has one sign and no configuration is blind. The relation between response area and gross weight is therefore established; we use it as the starting point.

What this literature does not address is the continuous girder. Over an interior support the influence line changes sign, so the positive area of the loaded span and the negative area of the adjacent span partly cancel. Distributed fibre-optic strain on a five-span continuous bridge has been used to obtain gross weight without influence lines [37], with many sensors along the bridge. Optimal sensor placement for BWIM has been addressed with an augmented Kalman filter formulation [38], and load identification from multi-point bridge deflection has been formulated as a regularised stochastic problem [39]. Field WIM from a vision-based mid-span deflection, with an accelerometer for axle detection, has also been reported [40], using an influence-line fit rather than the integral. The question asked here is narrower and comes first: for a given continuous girder and sensor position, can a single deflection channel observe the total load at all?

The question matters because continuous girders are common. Two-span overpasses are a large population of highway structures, and three-span units with a long main span are the usual form of medium-span box girders built by balanced cantilever. The two-span beam is the simplest statically indeterminate configuration in which span interaction is present, and it admits closed-form results throughout; the symmetric three-span beam is the layout of the in-service bridge studied here. On both, a sensor on one span responds negatively to load on the adjacent span, so the area-based weighing that works on simple spans can degrade, or fail, without any sign of it in the individual readings.

The contributions are as follows. First, the invariance of the deflection integral is stated for any linear-elastic beam, and the constant $C_m$ is identified by reciprocity as the sensor deflection under a uniformly distributed unit load; we did not find this characterisation stated in the BWIM literature we reviewed. This result is the foundation, not the headline. Second, closed forms of $C_m$ are derived for two-span beams with arbitrary span and stiffness ratios and for symmetric three-span beams, including the sign change of $C_m$. Third, the blind configurations, where a sensor records zero net integral for any vehicle, are located in closed form, together with the exact optimal sensor position. Fourth, $|C_m|$ and the cancellation ratio $C_m/A^+$ are proposed as pre-installation observability indicators. Fifth, an error budget specific to the integral estimator shows that zero-offset drift, not random noise, dominates. The theory is verified on a laboratory two-span beam with statically positioned loads and applied to the acceptance-test data of an in-service 55 + 90 + 55 m box girder. That application is a static consistency check of the observability criterion. It is not a validation of the integral identity on a continuous bridge, because no crossing record exists for that structure.

"Observability" is used throughout in the narrow sense of total-load observability: a non-zero $C_m$, so that the total load maps to a non-zero integral. It is not the observability of a state-space model.

Section 2 develops the theory. Section 3 reports the laboratory verification, Section 4 the application to the in-service bridge, and Section 5 a short analysis of field crossing records. Section 6 gives the error budget and the dynamic range of validity, Section 7 the recommendations and limitations, and Section 8 the conclusions.

---

## 2. Theory

This section states the invariance property, derives $C_m$ for two- and three-span beams, and defines the two estimators and the observability indicators. Only the results needed later are kept in the main text; derivations are in Appendix A.

### 2.1. Invariance of the deflection integral

Consider a linear-elastic beam of total length $L$ with time-invariant properties, and a fixed measurement point $m$. Let $\eta_m(x)$ be the deflection at $m$ due to a unit vertical force at abscissa $x$, with $\eta_m = 0$ outside $[0, L]$. A convoy of $n$ forces $P_i$ at fixed offsets $a_i$ from the leading force ($a_1 = 0$) crosses the beam quasi-statically. By superposition the deflection at $m$ when the leading force is at $x$ is

$$y_m(x)=\sum_{i=1}^{n}P_i\,\eta_m(x-a_i). \tag{1}$$

Integrating term by term and substituting $u = x - a_i$ maps every term onto the same interval, because $\eta_m$ vanishes outside $[0, L]$:

$$I_y=\int_{0}^{L+a_\mathrm{max}}y_m(x)\,\mathrm{d}x=\Big(\sum_{i=1}^{n}P_i\Big)\int_0^L\eta_m(u)\,\mathrm{d}u=C_m\,P_\mathrm{tot}. \tag{2}$$

The constant $C_m$ depends only on the structure and the sensor position. It does not depend on the number of axles, their loads or their spacings. The integration must run from the entry of the leading axle to the exit of the trailing one, $[0, L+a_\mathrm{max}]$. Truncating at $x = L$ removes the tail of every trailing axle, and on a continuous beam that tail lies where $\eta_m$ is negative, so the error does not cancel.

The constant has a second, more useful form. Let $w_m(x)$ be the deflected shape under a unit load at $m$, and $w_q(x)$ the deflection under a uniformly distributed load of intensity $q_0$ over the whole length. Maxwell's reciprocal theorem gives $\eta_m(x) = w_m(x)$. Betti's theorem applied to the unit point load at $m$ and the uniform load gives $q_0\int w_m\,\mathrm{d}x = w_q(x_m)$. Hence

$$C_m=\int_0^L\eta_m\,\mathrm{d}u=\int_0^L w_m\,\mathrm{d}x=\frac{w_q(x_m)}{q_0}. \tag{3}$$

The invariance constant is the deflection at the sensor under a uniform load over the whole structure, divided by the load intensity. It can be read from a standard table, obtained from one static analysis of an existing model, or measured with one static uniform-load test. A configuration is blind exactly when a uniformly loaded structure shows no deflection at the sensor. The invariance itself has a simple reading. Each axle produces a shifted, load-scaled copy of the same influence line; changing the spacing moves the copies along the record and changes the shape of the signal, but a translation cannot change the signed area of a function. Integration over a complete passage discards the translational information and keeps only the load scaling. By Eq. (3), $C_m$ is in turn the signed area of the deflected shape under a unit load at the sensor, a global flexibility of the structure viewed from the measurement point. For a continuous beam this flexibility is a signed sum, and its sign is what governs the results below. The property requires linearity and time-invariance: it does not survive material or geometric nonlinearity, bearing uplift or friction, or a stiffness change during the crossing.

### 2.2. Two-span continuous beam

Let the instrumented span have length $L_1$ and rigidity $EI_1$, the adjacent span $L_2 = \rho_L L_1$ and $EI_2 = \rho_{EI}EI_1$, and the sensor be at $\xi = x_m/L_1$. The interior support moment under a uniform load follows from slope continuity. Superposing the simply supported response and the end-moment response, evaluating at the sensor and dividing by $q_0$ gives (Appendix A)

$$C_m=\frac{L_1^4}{24EI_1}F(\xi,\mu),\qquad F(\xi,\mu)=\xi(1-2\xi^2+\xi^3)-\frac{\mu}{2}\,\xi(1-\xi^2), \tag{4}$$

$$\mu=\frac{1+\rho_L^3/\rho_{EI}}{1+\rho_L/\rho_{EI}}. \tag{5}$$

Geometry and stiffness enter only through the scalar $\mu$, which is unity for a symmetric beam. For equal spans and a mid-span sensor Eq. (4) gives $C_m = L^4/(192EI)$. Table 1 compares Eq. (4) with a finite element (FE) evaluation of Eq. (3); the two agree to eleven significant figures.

**Table 1.** Two-span beam: closed form, Eq. (4), against FE evaluation of Eq. (3). Values are $192EI_1C_m/L_1^4$; $\rho_{EI} = 1$.

| Case | $\rho_L$ | $\xi$ | Closed form | FE | Difference |
|---|---|---|---|---|---|
| Equal spans | 1.0 | 0.50 | 1.00000000 | 1.00000000 | 1 × 10⁻¹¹ |
| Short adjacent span | 0.5 | 0.50 | 1.37500000 | 1.37500000 | 1 × 10⁻¹¹ |
| Long adjacent span | 1.3 | 0.50 | 0.41500000 | 0.41500000 | 9 × 10⁻¹¹ |
| Blind configuration | 1.45743 | 0.50 | 0.00000000 | 0.00000000 | 7 × 10⁻¹¹ |
| Beyond blind | 2.0 | 0.50 | −2.00000000 | −2.00000000 | 8 × 10⁻¹² |
| Optimal sensor | 1.0 | 0.42154 | 1.03989535 | 1.03989535 | 9 × 10⁻¹¹ |
| Sensor near support | 1.0 | 0.70 | 0.60480000 | 0.60480000 | 1 × 10⁻¹¹ |

Because both estimators of Section 2.4 divide by $C_m$, the configurations with $C_m = 0$ carry no information about the load. Setting $F = 0$ gives a condition on $\mu$ alone, which inverts for the stiffness ratio:

$$C_m=0\;\Leftrightarrow\;\mu=\mu_\mathrm{crit}(\xi)=\frac{2(1+\xi-\xi^2)}{1+\xi},\qquad \rho_{EI,\mathrm{crit}}=\frac{\rho_L(\rho_L^2-\mu_\mathrm{crit})}{\mu_\mathrm{crit}-1}. \tag{6}$$

For a mid-span sensor $\mu_\mathrm{crit} = 5/3$. With uniform stiffness the blind condition is $3\rho_L^2-3\rho_L-2=0$, and maximising $C_m$ over $\xi$ at $\mu = 1$ gives $8\xi^2-\xi-1=0$. Both roots are exact:

$$\rho_{L,\mathrm{crit}}=\frac{3+\sqrt{33}}{6}=1.45743,\qquad \xi^*=\frac{1+\sqrt{33}}{16}=0.42154. \tag{7}$$

Beyond $\rho_{L,\mathrm{crit}}$ the constant changes sign: the integral remains formally usable, but the response is dominated by the uninstrumented span. At $\xi^*$ the constant exceeds its mid-span value by the factor 1.039895. The gain over mid-span installation is therefore small, whereas the constant falls to 10 % of its maximum at $0.9L_1$.

The blind condition has a mechanical reading. In units of $L_1^4/(192EI_1)$ and for a mid-span sensor, the positive contribution of the instrumented span, $C_m^+$, varies only between 1.50 and 2.00 for $\rho_L$ from 0.5 to 2.0, whereas the negative contribution of the adjacent span, $C_m^-$, sweeps from −0.125 to −4.00. For equal spans $C_m^+ = 1.750$ and $C_m^- = -0.750$, so the net constant is only 4/7 of the positive part. The degeneracy is driven almost entirely by the adjacent span. The same decomposition explains why the optimum lies off mid-span. Moving the sensor from $0.50L_1$ to $0.42L_1$ reduces the positive contribution only slightly, from 1.750 to 1.732, but reduces the magnitude of the negative one from 0.750 to 0.692, so the net constant rises from 1.000 to 1.040. The optimum moves towards the outer support because the adjacent span interferes less there. On a simply supported beam, mid-span is optimal by symmetry; the shift is a signature of continuity.

The effect of the stiffness ratio is directional. Since $\partial\mu/\partial\rho_{EI}\propto\rho_L(1-\rho_L^2)$, stiffening a long adjacent span raises $C_m$ and stiffening a short one lowers it. At $\rho_L = 1.6$ the constant rises from −0.78 at $\rho_{EI} = 0.5$ to +0.33 at $\rho_{EI} = 4$, crossing zero at $\rho_{EI} = 2.14$. Blindness belongs to the pair (configuration, sensor position), not to the structure: at $\rho_L = 1.45$ a mid-span sensor gives 0.021, whereas a sensor at $\xi = 0.266$ gives 0.233. Fig. 2 maps the constant over the two ratios with the blind locus of Eq. (6) and the near-blind band $|192EI_1C_m/L_1^4| < 0.2$, where the measurement sensitivity exceeds five times its equal-span value.

### 2.3. Three-span continuous beam

Medium-span box girders are mostly symmetric three-span units with a long main span. Eq. (3) extends to this layout without new ingredients; only the number of redundants increases. Let the side spans have length $L_s$ and rigidity $EI_s$, and the main span $L_m = \beta L_s$ and $EI_m = \rho_{EI}EI_s$, with $EI$ piecewise constant (Fig. 1b). For a side-span sensor, $\rho_{EI}$ is again the adjacent-to-instrumented stiffness ratio. By symmetry the two support moments are equal, and the three-moment equation gives $M_B = M_C = -q_0L_s^2\mu/8$. For a sensor at $\xi = x/L_s$ in a side span, $C_m$ has the form of Eq. (4) with

$$\frac{192EI_sC_m}{L_s^4}=8F(\xi,\mu),\qquad \mu=\frac{2(\rho_{EI}+\beta^3)}{2\rho_{EI}+3\beta}. \tag{8}$$

The far side span restrains the interior support. A symmetric beam with three equal spans therefore has $\mu = 4/5$ rather than 1, and its constant at mid side span is 1.3 times the two-span value. For a sensor at $\eta = x/L_m$ in the main span the constant is $192EI_mC_m/L_m^4 = 8[\eta(1-2\eta^2+\eta^3)-\nu\,\eta(1-\eta)]$, with $\nu = 3(\rho_{EI}+\beta^3)/[\beta^2(2\rho_{EI}+3\beta)]$. Both expressions agree with FE evaluations of Eq. (3), by the uniform-load route and by integration of the influence line, to a maximum relative error of 7.5 × 10⁻¹² over 60 comparisons (six $(\beta,\rho_{EI})$ pairs, five sensor positions, both routes).

Because $F$ is unchanged, the blind condition for a side-span sensor is again $\mu = \mu_\mathrm{crit}(\xi)$ of Eq. (6). At mid side span the blind stiffness ratio is explicit, $\rho_{EI,\mathrm{crit}} = 3\beta(2\beta^2-5)/4$. For uniform rigidity the critical main-to-side span ratio is the real root of a cubic in the irreducible case, so its exact closed form is trigonometric:

$$6\beta^3-15\beta-4=0,\qquad \beta_\mathrm{crit}=\sqrt{10/3}\,\cos\!\Big[\tfrac13\arccos\!\Big(\tfrac25\sqrt{6/5}\Big)\Big]=1.700594. \tag{9}$$

The near-blind band $|192EI_sC_m/L_s^4| < 0.2$ at mid side span begins at $\beta = 1.621399$, the root of $30\beta^3-69\beta-16=0$. For $\beta \ge 2\cos(\pi/9) = 1.879385$, no position in the side span gives a positive constant. The integral then remains formally usable, but the response at every side-span position is dominated by the main span, as beyond the two-span blind ratio. The ratio of the negative main-span contribution to the positive side-span contributions, for a mid side-span sensor and uniform rigidity, is

$$\frac{|C^-|}{C^+}=\frac{6\beta^3}{15\beta+4}. \tag{10}$$

The optimal side-span position solves $8\xi^3-(12-3\mu)\xi^2+(2-\mu)=0$. For two spans this cubic reduces to the quadratic of Eq. (7) because $\mu = 1$ makes $\xi = 1$ a root; for three spans it does not. As Table 2 shows, $\xi^*$ moves towards the abutment as the main span lengthens. A mid main-span sensor becomes blind only when $\beta < 0.964706$, that is, when the main span is shorter than the side spans. The stiffness of the main span acts in a definite direction. Since $\partial\mu/\partial\rho_{EI}\propto 3\beta-2\beta^3$, for $\beta>\sqrt{3/2}$ a stiffer main span lowers $\mu$ and improves the observability of the side span. Haunched girders, however, are stiff near the piers rather than uniformly stiffer in the main span, and Section 4 shows that their behaviour is not captured by a piecewise-constant $\rho_{EI}$.

**Table 2.** Symmetric three-span beam, uniform rigidity: optimal side-span sensor position and the indicator $192EI_sC_m/L_s^4$. The FE slope at $\xi^*$ is at most 3.6 × 10⁻⁷ in every case.

| $\beta$ | $\mu$ | $\xi^*$ | At $\xi^*$ | At $\xi = 1/2$ |
|---|---|---|---|---|
| 1.0 | 0.80000000 | 0.44603660 | 1.32176895 | 1.30000000 |
| 1.2 | 0.97428571 | 0.42508293 | 1.07563406 | 1.03857143 |
| 1.4 | 1.20774194 | 0.38747142 | 0.75849895 | 0.68838710 |
| 1.5 | 1.34615385 | 0.35820014 | 0.58065335 | 0.48076923 |
| 1.63636 | 1.55785124 | 0.29944923 | 0.33162780 | 0.16322314 |
| 1.7 | 1.66563380 | 0.26077470 | 0.22018607 | 0.00154930 |

Fig. 3a maps the indicator over $\beta$ and $\xi$, with the blind locus, the near-blind band and $\xi^*(\beta)$. Fig. 3b treats asymmetric layouts with the general closed form (Appendix D). The far side span matters little while it is short: for $L_3/L_2$ between 0.3 and 0.6, the blind ratio $L_1/L_2$ for a mid span-1 sensor stays between 0.587 and 0.592.

### 2.4. Estimators and observability indicators

If $E$, $I$ and the spans are known, Eq. (2) gives the beam-property method (BPM), $P_\mathrm{tot} = I_y/C_m$. Because $C_m \propto L^4$, a 1 % error in span length produces a 4 % error in the load. On an existing bridge $EI$ is rarely known to better than a few per cent. The standard-load method (SLM) removes this requirement: a load of known total weight $P_0$ crosses the structure, and since both crossings share $C_m$,

$$P_t=P_0\,\frac{I_{y,t}}{I_{y,0}}. \tag{11}$$

The procedure is: (i) weigh a reference load; (ii) record one or, preferably, several complete crossings of it and average the integrals; (iii) record the unknown crossing; (iv) evaluate both integrals with the same quadrature rule and sampling grid; (v) apply Eq. (11). SLM cancels the structural factor shared by the two crossings, and with it the dependence on flexural rigidity and span length. Other systematic errors cancel only to the extent that they are common to the two crossings, and independent random errors do not cancel at all (Section 6).

Records are discrete. With samples $y_i$ at $x_i = i\Delta x$ the trapezoidal and Simpson rules are

$$I_y^\mathrm{trap}=\Delta x\Big[\tfrac{y_0}{2}+\sum_{i=1}^{n-1}y_i+\tfrac{y_n}{2}\Big],\qquad I_y^\mathrm{Simp}=\frac{\Delta x}{3}\Big[y_0+4\!\sum_{i\ \mathrm{odd}}\!y_i+2\!\!\sum_{i\ \mathrm{even}\neq 0,n}\!\!y_i+y_n\Big]. \tag{12}$$

The half-weights at the ends vanish only when the record starts and ends at zero deflection, which holds in the laboratory but not on a bridge with residual deflection. The influence line of a continuous beam is piecewise cubic and twice differentiable, so Simpson quadrature is nearly exact, whereas the trapezoidal rule converges only as $\Delta x^2$ (Section 3.2).

Both estimators divide by $C_m$, so to first order the measurement sensitivity scales as $1/|C_m|$. We therefore propose $|C_m|$, in the normalised form

$$N_m=\frac{192EI_\mathrm{ref}C_m}{L^4}, \tag{13}$$

as a pre-installation observability indicator, with $L$ the span containing the sensor. It answers three questions at once: whether a span arrangement can observe the load from a given point, where to place the sensor, and how tight the baseline stability must be (Section 6.2). The threshold $|N_m| < 0.2$ marks near-blind locations for prismatic beams. Reporting $|C_m|$ for a deployment of the method serves a purpose similar to reporting the condition number of a regularised inverse problem, although $|C_m|$ is a single dimensional scalar and not a ratio of singular values.

For non-prismatic girders $N_m$ depends on the choice of $EI_\mathrm{ref}$, and Section 4 shows that this choice can dominate the result. A complementary measure that does not need a reference stiffness is the cancellation ratio

$$R_m=\frac{C_m}{A^+}=1-\frac{|A^-|}{A^+}, \tag{14}$$

the net influence area divided by its positive part. $R_m = 1$ for a simply supported beam, $R_m = 4/7$ for an equal two-span beam instrumented at mid-span, and $R_m = 0$ at a blind configuration. $N_m$ measures the signal relative to the local flexibility; $R_m$ measures how much of it the adjacent spans cancel.

A third index states what invariance costs. The integral weights the record uniformly, and only a uniform weight leaves the result unchanged under a translation of the integrand. Under white noise, with the structure and axle positions known, the optimal weight would be the influence line itself (a matched filter). By the Cauchy–Schwarz inequality the ratio of standard deviations of the two estimators is

$$O_m=\frac{|C_m|}{\sqrt{L_\mathrm{tot}\int_0^L\eta_m^2\,\mathrm{d}x}}\le 1. \tag{15}$$

For the equal two-span beam instrumented at mid-span, $O_m = 2\sqrt{44765}/1279 = 0.331$. The integral estimator keeps one third of the precision of an estimator that knows the structure and the axle positions, and in exchange needs neither. $O_m$ decreases monotonically as the sensor moves away from the outer support, whereas $|C_m|$ peaks at $\xi^*$; sensor placement should follow $|C_m|$.

The closed forms of Eqs. (4)–(10) are exact for prismatic or piecewise-prismatic beams. The next two sections test the two-span result on a laboratory beam and apply the indicators to a haunched three-span girder.

---

## 3. Laboratory verification

This section verifies the influence line, the integral and the two estimators on a laboratory two-span beam. The loads were positioned statically at successive points along the beam. The tests therefore verify the model and the algorithm, not performance at the scale of a bridge or under moving traffic.

### 3.1. Specimen and procedure

Tests were carried out at the Laboratory of Transportation Technology and Systems, Faculty of Bridge and Road Engineering, Hanoi University of Civil Engineering. The specimen (Fig. 4) was a steel beam of total length 5400 mm on three supports forming two equal spans of 2500 mm. The end supports were steel rollers and the interior support a steel knife edge that restrains vertical displacement and allows rotation. The cross-section was a hollow square tube, 25 mm × 25 mm with a wall thickness of 2.03 mm (averaged from measurements), giving $I = 16\,529.8$ mm⁴. With $E = 200$ GPa, $EI = 3.3060\times10^9$ N mm² and the theoretical constant at mid-span of the first span is $C_m = l^4/(192EI) = 61.541$ mm²/N. Shear deformation contributes 8 × 10⁻⁴ of the bending deflection (span-to-depth ratio 100), so Euler–Bernoulli theory applies.

Deflection at mid-span of the first span was measured with a linear variable differential transformer (LVDT) of range 0–50 mm and resolution 0.005 mm, connected to a TDS-303 data logger. Calibrated steel weights were suspended at positions 250 mm apart along the whole traverse, so $\Delta x = 250$ mm. Each reported deflection is the mean of three loading and unloading cycles. Three configurations were tested: a single load of 4.143 kg including its hook (40.64 N), used as the reference; two loads of 2145 g and 4684 g at 250 mm spacing; and three loads of 2550 g, 5100 g and 5100 g at spacings of 250 mm and 500 mm. Each record extends to $2l + a_\mathrm{max}$, that is 5000, 5250 and 5750 mm. The beam was modelled in Abaqus [41] with beam elements; cubic elements reproduce the exact nodal Euler–Bernoulli displacements, so agreement with the analytical influence line verifies the implementation only. The FE model was used to verify Eq. (3) and for the parametric studies.

### 3.2. Influence line and integral

Fig. 5 compares the analytical influence line (Appendix A, Eq. (A.2)) with the measurements for the single load; the values are listed in Appendix C. The largest absolute deviation is 0.0125 mm, which is 0.43 % of the maximum deflection and two and a half times the LVDT resolution. Expressed as a relative error at each point, the same data give a misleading maximum of 1.86 % at $x$ = 2250 mm, only because the deflection there is small; near the supports the absolute measure is the meaningful one. The residuals are predominantly positive on both spans, which indicates a small systematic component, plausibly slight support flexibility or a small overestimate of $EI$.

**Table 3.** Deflection integral for the single-load configuration.

| Quantity | Value (mm²) | Difference from exact |
|---|---|---|
| Exact, $P_0l^4/(192EI)$ | 2501.19 | — |
| Analytical influence line, trapezoidal rule, $\Delta x$ = 250 mm | 2488.68 | −0.500 % |
| Analytical influence line, Simpson rule, $\Delta x$ = 250 mm | 2501.85 | +0.027 % |
| Measured, trapezoidal rule, $\Delta x$ = 250 mm | 2513.43 | +0.49 % |

The trapezoidal bias of −0.500 % is a property of the quadrature, not an experimental error, and it propagates one-for-one into BPM. Simpson quadrature on the same grid reduces it to +0.027 % at no experimental cost.

### 3.3. Total-load identification

The measured records of the two- and three-load groups (Appendix C) were used to identify the total load by BPM and by SLM, with the single-load record as reference. Table 4 compares the results with direct weighing.

**Table 4.** Identified total loads against direct weighing.

| Configuration | Method | $I_y$ (mm²) | Identified load (N) | Deviation |
|---|---|---|---|---|
| Two loads | Weighing | — | 66.99 | — |
| | BPM | 4168.15 | 67.73 | +1.10 % |
| | SLM | 4168.15 | 67.40 | +0.61 % |
| Three loads | Weighing | — | 125.08 | — |
| | BPM | 7788.93 | 126.57 | +1.19 % |
| | SLM | 7788.93 | 125.95 | +0.70 % |

Both methods identify the total load within 1.2 %, and SLM is the more accurate. The ratio of the two estimates is 1.00489 for both configurations and equals the ratio of the measured reference integral to its exact value, 2513.43/2501.19. The whole difference between BPM and SLM is thus the calibration error of the reference record, which SLM absorbs and BPM does not. The BPM result also benefits from two errors of opposite sign: the trapezoidal rule underestimates the integral by 0.50 %, while the measured deflections exceed theory by about 1.6 %. Correcting the quadrature bias alone would raise the BPM deviation from +1.10 % to +1.61 %.

Fig. 6 plots the measured integral against the total load for the three configurations. A regression through the origin gives $I_y = 62.229P$ with $R^2 = 0.99998$, a slope 1.12 % above the theoretical 61.541 mm²/N, which is consistent with the residual pattern of Fig. 5. Because the three configurations differ in both total load and spacing, this line supports the invariance only indirectly; three points do not make the $R^2$ a strong test. A direct test with a fixed total load at varying spacings is recommended in Section 7.

The laboratory beam thus confirms the influence line, the integral and the common-mode cancellation of SLM on the equal two-span case. The next section asks what the criterion says about a real continuous girder whose layout lies close to the blind locus.

---

## 4. Application to an in-service three-span box girder

This section applies the observability criterion to the acceptance-test data of an in-service three-span box girder and runs a static consistency check of the model behind it. The bridge was tested only with parked convoys, one reading per gauge and load case, so the data cannot check Eq. (2) itself.

### 4.1. Bridge and test data

The Cầu Mây Bridge carries provincial road DT389 over the Kinh Mon River in Hai Duong, Viet Nam. Its main bridge is a three-span continuous prestressed concrete box girder of 55 + 90 + 55 m, built by balanced cantilever, so $\beta = 90/55 = 1.636$. The depth varies from 2.40 m at mid-span to 5.40 m at the piers. The designer's rating calculation gives $I = 5.482$ m⁴ at mid-span and $I = 59.612$ m⁴ at the pier face for vertical bending, with $E_c = 36\,057$ MPa ($f'_c = 45$ MPa). The inner piers T6 and T7 are monolithic with the girder, and the end piers T5 and T8 carry pot bearings. The approach spans are simply supported behind expansion joints and add nothing to $C_m$.

The acceptance load test was carried out in June 2020. The test trucks had three axles, nominally 5 + 10 + 10 t (about 25 t gross; individual weighbridge values [NEED VALUE]), with axle spacings of 3.60 m and 1.35 m and a clear gap of 6.0 m between trucks in a row, two trucks abreast. Scheme III placed four trucks (100 t) in side span N8, with the middle axle of the first row at 0.4L. Scheme IV placed six trucks (150 t) in centre span N7, the middle axle of the second row at mid-span. Deflections were read by three gauges per section, under centric and eccentric transverse positions. In the eccentric position the outer wheel was 0.6 m from the kerb. Each scheme was loaded three times with zero readings in between, and the tables give one peak value per gauge and load case. Gauge N8 is at 0.4L, 22 m from the end support; gauge N7 is at mid-span of the centre span. The mean of the six readings is 5.55 mm at N8 against 5.93 mm from the designer's FE model, and 15.42 mm at N7 against 16.70 mm.

### 4.2. Model

Influence lines and $C_m$ were computed with a two-dimensional Euler–Bernoulli FE model with variable stiffness, 10 elements per metre and rigid vertical supports. The depth was assumed to vary parabolically over a length $L_v$ from each inner pier axis, and $I = I_\mathrm{mid}(h/h_\mathrm{mid})^n$ with $n = 2.943$ fitted to the two known sections (Fig. 7a). $L_v$ is not stated in the available documents; $L_v = 44$ m was used, bracketed by 40 m and 45 m. Each inner pier was represented by a rotational spring $k$, bounded by the pinned ($k = 0$) and fixed ($k \to \infty$) limits because the pier dimensions were not available. A best estimate $k_\mathrm{FE} = 2.7\times10^7$ kN m/rad ($2.5$–$3.6\times10^7$ over the $L_v$ variants) was obtained by fitting the deflections that the test report gives for the designer's FE model; with the truck positions of the test plan, it reproduces both values within −4.2 % to +3.7 %. As a check, $C_m$ computed as the influence-line area and as the deflection under a unit uniform load, Eq. (3), agreed to 1.1 × 10⁻⁴ in every case. The indicator $N_m$ uses $EI_\mathrm{ref} = EI_\mathrm{mid}$, the minimum of $EI(x)$. The section properties were checked independently: a polygon routine applied to the cross-section drawings reproduces the designer's areas within −0.3 % and −0.5 % and the second moments within −5.8 % and −2.6 % at mid-span and at the pier face. The pier diaphragm, shear deformation, shear lag and transverse distribution are not modelled; the two-dimensional beam carries the total load of the two trucks in each row.

### 4.3. Observability of the installed gauges

The prismatic closed form already places this layout near the blind locus. With uniform rigidity, Eq. (8) gives $N_m = 0.163$ at mid side span, inside the near-blind band, because $\beta = 1.636$ exceeds the edge 1.621399 of Section 2.3. Eq. (10) gives $|C^-|/C^+ = 0.921$. Moving the sensor to $\xi^* = 0.2994$ would double the indicator to 0.332 (Table 2). The span-wise contributions, obtained by loading one span at a time, are 1.870395 and 0.195395 for the two side spans and −1.902566 for the main span, in units of $L_s^4/(192EI_s)$; the influence line keeps one sign in each span (+, −, +). A mid main-span sensor of the same prismatic beam would read 0.754630 with a cancellation of only 0.30.

Table 5 gives the results of the variable-stiffness model, and Fig. 7b shows the influence lines.

**Table 5.** Observability indicators for the Cầu Mây gauges. $N_m = 192EI_\mathrm{mid}C_m/L^4$ with $L$ the span containing the gauge; $R_m = C_m/A^+$. "Range" covers pinned to fixed piers and all $L_v$ variants.

| Gauge | Constant $EI$, pinned | Variable $EI$, $k_\mathrm{FE}$ | Range | $\lvert A^-\rvert/A^+$ at $k_\mathrm{FE}$ | $R_m$ at $k_\mathrm{FE}$ |
|---|---|---|---|---|---|
| N8, 0.4L of side span (installed) | 0.287 | **0.181** | 0.023 … 0.446 | 0.82 | 0.18 |
| N8 at mid side span (alternative) | 0.163 | 0.105 | −0.066 … 0.375 | 0.89 | 0.11 |
| N7, mid centre span (installed) | 0.755 | 0.209 | 0.145 … 0.263 | 0.41 | 0.59 |

The installed side-span gauge is near-blind in the best-estimate model. Its indicator is 0.181, and the negative lobe in the 90 m centre span cancels 82 % of its positive influence area. The result also depends strongly on pier fixity: $C_m$ at N8 is $7.3\times10^{-6}$ m²/kN with pinned piers and $1.0\times10^{-4}$ m²/kN with fixed piers, a factor of about fourteen. A BPM estimate from this gauge would therefore be governed by a support parameter that was never measured. The test tables label N8 as "mid-span" while the test plan places it at 0.4L; both positions were computed, and both are near-blind (0.181 and 0.105).

The centre-span gauge behaves differently. Including the haunches lowers its indicator from 0.755 for a prismatic beam to 0.209. The cause is not cancellation, since $R_m = 0.59$: the haunches restrain the span, so the net area is small relative to the mid-span flexibility used for normalisation. The threshold $|N_m| < 0.2$ derived for prismatic beams therefore does not transfer directly to haunched girders; it must be stated together with $EI_\mathrm{ref}$. The cancellation ratio separates the two effects. By $R_m$, N7 (0.59) is clearly better conditioned than N8 (0.18), which is the ranking the prismatic analysis predicts. The absolute constants point the same way: at $k_\mathrm{FE}$, $C_m$ is $3.61\times10^{-4}$ m²/kN at N7 and $4.38\times10^{-5}$ m²/kN at N8, so for the same vehicle the centre-span gauge records an integral about eight times larger, and a given baseline offset does about eight times less damage (Eq. (19)).

### 4.4. Static consistency check and implications for BPM and SLM

**Table 6.** Static consistency check. Measured values are the mean of three gauges under two transverse positions.

| Gauge | Convoy | Measured (mm) | Report FE (mm) | This model at $k_\mathrm{FE}$ (mm) | Measured / report FE | Measured / model | Pinned … fixed (mm) |
|---|---|---|---|---|---|---|---|
| N8, 0.4L | 4 × 25 t | 5.55 | 5.93 | 5.69 | 0.936 | 0.977 | 7.18 … 2.75 |
| N7, mid | 6 × 25 t | 15.42 | 16.70 | 17.32 | 0.923 | 0.890 | 22.99 … 8.34 |

The measured deflections are 0.92–0.94 of the designer's model. With $k$ fixed at $k_\mathrm{FE}$, they imply an effective stiffness $EI_\mathrm{eff}/EI_\mathrm{design} = 1.09$; directly against the report FE the ratio is 1.07–1.08. The bridge is thus stiffer than its design model by roughly 7–9 %. The pinned and fixed limits bracket the measurements widely (Table 6), which shows how much the support condition alone controls the response.

Linearity, on which both the theorem and SLM rest, cannot be tested directly: no span was loaded with more than one convoy size while deflections were read. The evidence is indirect. The measured-to-model ratios are similar for the four-truck and six-truck convoys (0.936 and 0.923). Transverse effects are visible: individual readings range from 5.22 to 5.91 mm at N8 and from 14.62 to 16.67 mm at N7, and in the eccentric N7 case the readings across the section spread by up to 2.05 mm. The ratio of measured to modelled deflection is therefore a section average; a single-gauge installation would also carry the transverse position of the vehicle as an error term, which a one-dimensional treatment cannot remove.

These results have three practical consequences. First, a $C_m$ taken from the design model carries the design-model stiffness bias; here BPM would underestimate the total load by roughly 7–9 %. Second, at a near-blind location the uncertainty in support conditions can change $C_m$ by an order of magnitude, so a design-model $C_m$ is unusable there. Third, SLM calibrates $C_m$ with a weighed vehicle and removes both errors, provided the response is linear; even then, a near-blind gauge delivers a small integral and a poor signal-to-noise ratio. The criterion is most useful before installation: on this bridge a gauge in the centre span, or a second gauge there, would have avoided the near-blind configuration.

The in-service girder thus confirms, on real section data, that a layout near the prismatic blind locus can be near-blind in practice, and that the cancellation ratio separates true cancellation from the effect of haunching. A direct test of Eq. (2) on a continuous girder still requires crawl or moving passes of weighed vehicles.

---

## 5. Field deflection records: baseline drift and filtering

This section has a supporting role. It uses moving-truck deflection records from two simply supported bridges to test two signal-processing claims of Section 6, the effect of baseline drift and of filtering on the integral, and not the absolute relation of Eq. (2). The data have three limitations that bound what they can show. Truck weight, speed and lane were not recorded. The ratio between the processed and the raw deflection channel differs by span (1.00, 3.25 and 5.15 at Gie Cuc I; 0.67 and 1.34 at Phuong Do), and the channel calibration is not documented. The series are quantised and partly processed by hand.

The records come from Gie Cuc I (three simply supported spans of 25.7 m) and Phuong Do (two spans, calculation length 17.5 m), measured at mid-span with an SDA-830C recorder at 200 Hz for 15 s. Seven complete crossings were identified. The integral of each crossing was computed with four baselines: a constant tare level, a straight line between quiet windows before and after the event (the reference), a cubic fitted to all quiet samples, and zero-phase high-pass filters at 0.1 Hz and 0.5 Hz (Fig. 8).

Over the 2–4 s event window the tare, linear and cubic baselines agree within about 6 % for every crossing but one; the cubic differs from the linear by +1.7 to +3.6 % at Gie Cuc and −1.2 to +0.1 % at Phuong Do. The exception is the raw Phuong Do N1 record, whose baseline steps by 2.06 mm (18 % of the peak) as the truck leaves the span; there the tare-only integral is 36.4 % below the reference. The effect of a small offset grows with the integration time. Over the whole 15 s record, tare-only integrals differ from the cubic-baseline values by +7 %, −16 % and −60 % at the three Gie Cuc spans, +34 % at Phuong Do N2 and −170 % (a sign reversal) at Phuong Do N1. This is the behaviour of Eq. (19) in Section 6.2: an offset that is harmless over a short window becomes a tens-of-per-cent error over a long one. High-pass filtering changed the event integral by −44 to −83 % at 0.1 Hz and by about −100 % at 0.5 Hz; a filter with zero gain at zero frequency removes the quantity being integrated and cannot serve as a baseline correction.

A zero-phase low-pass filter at 2 Hz, about one third of the measured fundamental frequencies of 5.2–6.0 Hz, left the event integral unchanged within a ratio of 0.9999 to 1.0010 for complete events (Fig. 9). The dynamic residual, unfiltered minus filtered, integrates to 0.001–0.022 of its absolute integral, although its peaks reach 3–16 % of the quasi-static peak. The integral is therefore insensitive to the dynamic component; part of this follows from the unit gain of the filter at zero frequency, so it confirms the processing rather than the theory.

Speeds fitted from the records were 27–36 km/h at Phuong Do, consistent with the stated 30–40 km/h, but 47–62 km/h at Gie Cuc, which is not. We report this discrepancy without resolving it. Speed-normalised integrals scatter by 26–33 % across spans and events, but with channel scale factors that differ by up to 7.7 times between records this scatter cannot be attributed to the bridge or to the truck. One record shows how processing can mimic structural behaviour. The Phuong Do N1 trace has a positive lobe after the truck leaves the span, which could suggest partial continuity between the simple spans. About 40 % of its amplitude is the 2.06 mm baseline step; a residual of about 25 % of the downward peak remains and cannot be classified as physical or artefactual from the exported data.

The records thus support two operational rules: integrate over a window tight around the crossing and re-zero the baseline before and after it, and remove dynamics with a low-pass filter, never with a high-pass filter.

---

## 6. Error budget and dynamic validity

The laboratory agreement of Section 3 was obtained on a beam of known properties under static loads. This section develops the error budget explicitly and bounds the quasi-static assumption, so that the results can be extrapolated with stated sensitivities. Monte Carlo details are in Appendix B.

### 6.1. Measurement model and error propagation

The recorded deflection at sample $i$ is modelled as

$$y_i^\mathrm{meas}=(1+\gamma)\,y_i+\varepsilon_0+\sigma_a\,\zeta_i,\qquad \zeta_i\sim\mathcal N(0,1), \tag{16}$$

with gain error $\gamma$, zero offset $\varepsilon_0$ and additive noise of standard deviation $\sigma_a$. Unlike a purely multiplicative model, Eq. (16) does not predict zero noise at the supports. To first order, the error of each estimator is

$$\Big(\frac{\delta P}{P}\Big)_\mathrm{BPM}=\frac{\delta(EI)}{EI}-4\frac{\delta l}{l}+\gamma_t+e_{q,t}+\frac{\varepsilon_{0,t}L_t}{I_{y,t}}+\frac{\delta v_t}{v_t}, \tag{17}$$

$$\Big(\frac{\delta P}{P}\Big)_\mathrm{SLM}=\frac{\delta P_0}{P_0}+(\gamma_t-\gamma_0)+(e_{q,t}-e_{q,0})+\Big(\frac{\varepsilon_{0,t}L_t}{I_{y,t}}-\frac{\varepsilon_{0,0}L_0}{I_{y,0}}\Big)+\Big(\frac{\delta v_t}{v_t}-\frac{\delta v_0}{v_0}\Big), \tag{18}$$

where $e_q$ is the quadrature bias, subscript $t$ the target crossing and subscript 0 the reference. SLM removes the structural terms outright, because they belong to $C_m$. Every other term survives as a difference, which vanishes only when the error is common to both crossings. A gain error cancels if the chain is not recalibrated between the crossings. The quadrature bias cancelled in the present tests (−0.5000 % for all three configurations) only because the spacings were integer multiples of $\Delta x$; at a spacing of 300 mm the bias would be −0.110 %, at 375 mm +0.249 %, and the residual would reach 0.4–0.75 %. The zero-offset term never cancels fully, even for equal offsets, because the sensitivity $L/I_y$ differs: for the two-load case the residual is $\varepsilon_0(1.2596-1.9893)$ mm⁻¹, a partial cancellation of about 37 %. A reference load as heavy as the target vehicles makes the cancellation nearly complete.

### 6.2. Zero-offset drift

A constant offset contributes $\varepsilon_0L_\mathrm{tot}$ to the integral without any cancellation, whereas the net integral is itself the residue of the cancellation between spans. The relative bias is

$$\Big(\frac{\delta P}{P}\Big)_{\varepsilon_0}=\frac{\varepsilon_0L_\mathrm{tot}}{I_y}. \tag{19}$$

Table 7 evaluates Eq. (19) for the laboratory configurations. An offset equal to the transducer resolution already biases the load by 0.4–1.0 %, comparable to the total errors of Section 3 and larger than any plausible random noise. On a bridge, baseline shifts of a few hundredths of a millimetre over a session bias the load by 2–10 %. Because the bias is inversely proportional to $I_y$, and therefore to $C_m$ and to the load, it is smallest for heavy vehicles, which suits overload screening, and largest at near-blind locations, which is a second reason to avoid them.

**Table 7.** Bias of the identified load caused by a zero offset $\varepsilon_0$, Eq. (19).

| Configuration | $I_y$ (mm²) | $L_\mathrm{tot}$ (mm) | $\varepsilon_0$ = 0.005 mm | 0.02 mm | 0.05 mm |
|---|---|---|---|---|---|
| Single load | 2513 | 5000 | +0.99 % | +3.98 % | +9.95 % |
| Two loads | 4168 | 5250 | +0.63 % | +2.52 % | +6.30 % |
| Three loads | 7789 | 5750 | +0.37 % | +1.48 % | +3.69 % |

### 6.3. Random noise and the SLM reference

A Monte Carlo study with 200 000 realisations per case (Appendix B) gives two results. Random noise is negligible: with $\sigma_a$ equal to half the resolution, the standard deviation of the identified load is 0.07 %, because integration averages independent perturbations. The systematic terms, gain and offset, dominate by more than an order of magnitude. SLM cancels common-mode error but not independent error. For independent perturbations of the two integrals the relative variances add, and under equal relative standard deviations

$$\frac{\sigma_{P,\mathrm{SLM}}}{P}=\sigma_r\sqrt{1+\frac{1}{N_\mathrm{rep}}}, \tag{20}$$

where $N_\mathrm{rep}$ is the number of averaged reference crossings. In the present tests the reference integral is only 60 % of the two-load one, and the observed factor is 1.47 rather than $\sqrt2$: the standard deviation under the combined model rises from 2.11 % with an averaged reference to 3.09 % with a single one, while BPM stays at 2.12 %. Averaging five or more reference crossings with a reference load comparable to the screened vehicles makes SLM better than BPM in bias and equal in scatter.

### 6.4. Traverse speed

Eq. (2) is an integral over space, whereas a monitoring system records time. For a constant speed, $I_y = v\int y_m\,\mathrm{d}t$, so the relative speed error enters the load one-for-one. This term is absent from the static laboratory tests and is likely to be the largest single field contributor. For a single axle on a two-span beam, the influence line vanishes at $x = l$ and $x = 2l$, so the interval between these two zero crossings gives $v = l/(t_2-t_1)$. The interior zero crossing is a clean sign change, whereas entry and exit are defined by a signal emerging from the noise floor; this self-calibration of speed is an advantage of a continuous beam over a simply supported one, whose influence line has no interior zero. Using entry and exit instead, the distance is $2l$ and $v = 2l/(t_\mathrm{out}-t_\mathrm{in})$; conflating the two distances costs a factor of two in the load. For a convoy the zero crossings shift, and the speed should be obtained from independent axle detection or from a least-squares fit of Eq. (1) with $v$ and the spacings as parameters. The method returns the gross weight after the crossing is complete, and two vehicles on the structure at once return their combined weight; overlapping crossings must be detected and discarded.

### 6.5. Quasi-static assumption

The laboratory programme cannot test the quasi-static premise. It was therefore quantified for a constant force crossing the specimen, which isolates bridge dynamics and is not a vehicle–bridge interaction analysis. The beam was modelled with a consistent mass matrix (1.464 kg/m) and Rayleigh damping of 2 % at the first and third modes. The computed fundamental frequency, 11.942 Hz, agrees to four figures with the analytical value. The equations of motion were integrated with the Newmark average-acceleration scheme; refining from 1000 to 16 000 steps changed the error by 0.002 percentage points. Fig. 10 shows the error of the quasi-static integral over 47 speeds spanning $T_\mathrm{cr}/T_1 = 2lf_1/v$ from 0.6 to 120, and Table 8 its envelope.

**Table 8.** Envelope of the dynamic error of the quasi-static estimator.

| $T_\mathrm{cr}/T_1 \ge$ | 2 | 3 | 4 | 6 | 8 | 10 | 15 | 20 |
|---|---|---|---|---|---|---|---|---|
| max $\lvert E_\mathrm{dyn}\rvert$ (%) | 17.6 | 8.6 | 3.8 | 1.7 | 1.00 | 0.32 | 0.15 | 0.08 |

The error oscillates with speed, as the moving-load literature leads one to expect [42], so the envelope is the appropriate summary:

$$\frac{T_\mathrm{cr}}{T_1}\ge 8\;\Rightarrow\;|E_\mathrm{dyn}|\lesssim 1\,\%;\qquad \frac{T_\mathrm{cr}}{T_1}\ge 4\;\Rightarrow\;|E_\mathrm{dyn}|<4\,\%. \tag{21}$$

Below $T_\mathrm{cr}/T_1 \approx 2.5$ the error exceeds 15 % and changes sign, and the estimator should not be used. The dominant mechanism is truncation: at high speed the beam has not returned to its datum when the load leaves (39 % of the static peak at $T_\mathrm{cr}/T_1 = 1.5$). Extending the window by four fundamental periods roughly halves the error. The error is not a residue of free vibration that damping would remove: repeating the analysis with damping ratios from 0.5 % to 5 % changes it monotonically, and less damping gives less error. A post-processing scheme that recovers the quasi-static value at rapid crossings would have to model the residual response rather than average it. Invariance survives the dynamics approximately: for a fixed total load distributed over one, two and three axles with spacings of 0.5–1.5 m, the spread of the integrals is 0.33 % at $T_\mathrm{cr}/T_1 = 11.9$ and 1.95 % at 3.0. Because the analysis omits the vehicle's own suspension and road roughness, Eq. (21) is a necessary condition for real traffic, not a sufficient one. As an order-of-magnitude orientation only, plausible fundamental frequencies for individual spans of 10 to 30 m give $T_\mathrm{cr}/T_1$ of 7 to 20 at 50 to 80 km/h. The ratio is insensitive to span, because crossing length and period scale in opposite directions, and is governed mainly by speed. At motorway speeds the margin narrows, and the ratio should be checked with the measured $f_1$ of the structure rather than converted into a speed limit.

### 6.6. Combined budget

Table 9 assembles an indicative budget in the format of the GUM [43] for the laboratory tests and for a plausible field deployment on a short-span concrete continuous bridge. The field entries are engineering scenarios propagated through the sensitivities derived above, with environmental drift values from long-term monitoring [44,45]. They are not a metrological validation of a complete system. The Type A entries were not evaluated from the three repeated cycles; they are upper bounds set by the transducer resolution and the Monte Carlo result of Section 6.3. A Type A evaluation from the cycle readings is [NEED VALUE].

**Table 9.** Indicative sensitivity-based uncertainty budget (standard uncertainties; independent terms combined in quadrature, systematic terms summed).

| Contribution | Type | Sensitivity | Laboratory (SLM) | Field (SLM) | Field (BPM) |
|---|---|---|---|---|---|
| Flexural rigidity $EI$ | B | 1 | cancels | cancels | 5–15 % |
| Span length $l$ | B | 4 | cancels | cancels | 0.4–2 % |
| Sensor gain $\gamma$ | B | 1 | cancels | cancels | 1–2 % |
| Quadrature bias $e_q$ | B | 1 | cancels | cancels | 0.5 % |
| Reference weighing $P_0$ | B | 1 | 0.1 % | 0.5–1 % | — |
| Zero offset $\varepsilon_0$ | B | $L_\mathrm{tot}/I_y$ | 0.4–1 % | 2–10 % | 2–10 % |
| Traverse speed $v$ | B | 1 | — | 1–3 % | 1–3 % |
| Dynamic effects ($T_\mathrm{cr}/T_1 \ge 8$) | B | 1 | — | < 1 % | < 1 % |
| Random noise $\sigma_a$ | A (bound) | < 0.1 | < 0.1 % | 0.1–0.3 % | 0.1–0.3 % |
| Reference scatter ($N_\mathrm{rep}$ = 1) | A (bound) | 1 | < 0.1 % | 0.1–0.3 % | — |
| **Combined** | | | **0.5–1.1 %** | **3–11 %** | **6–19 %** |

In the laboratory, SLM is limited by zero offset and reference weighing, and the combined 0.5–1.1 % is consistent with the observed deviations of 0.61 % and 0.70 %. In the field, baseline stability and speed dominate. The ranges are scenario-based and must be verified for each structure and instrumentation chain. They fall short of a certified weighing device, and the method is proposed for preliminary overload screening, with the decision threshold set sufficiently apart from the legal limit and the design live loads [46,47]; establishing that threshold requires field calibration and lies outside this study.

---

## 7. Recommendations and limitations

### 7.1. Recommendations for sensor placement and operation

The results above combine into a pre-installation procedure.

1. Compute $C_m$ for each candidate location: from Eq. (4) for two spans, Eq. (8) for symmetric three spans, or Eq. (3) with one static analysis of a model with $EI(x)$, or one static uniform-load test.
2. Check the blind locus. For prismatic beams, reject locations with $|N_m| < 0.2$; for two spans with uniform stiffness keep $\rho_L$ well below 1.45743, and for symmetric three spans note that the mid side span is near-blind from $\beta = 1.621399$.
3. For haunched girders, report $N_m$ with its $EI_\mathrm{ref}$ and also $R_m = C_m/A^+$, and rank locations by $R_m$. Where pier fixity is uncertain, evaluate $C_m$ at the pinned and fixed limits; a location whose $C_m$ changes by an order of magnitude between them is unsuitable.
4. Place the sensor near $\xi^*$ (0.42154 of the span for two equal spans; Table 2 for three spans) or, on long-main-span girders, in the main span.
5. Use SLM with a weighed vehicle comparable to the screened traffic, averaging at least five reference crossings. Use BPM only where the location is well conditioned and $EI$ is known.
6. Check $T_\mathrm{cr}/T_1 = 2lf_1/v \ge 8$ for the actual frequency, not a speed limit.
7. Integrate over a window tight around the crossing, re-zero the baseline before and after each crossing, and reject records whose end values differ by more than a set tolerance. Remove dynamics with a low-pass filter well below $f_1$, never with a high-pass filter.
8. Use Simpson quadrature or a sampling interval of $l/20$ or finer, and obtain the speed from the zero crossings of a single-axle reference record or from a fitted response model.

The procedure positions the deflection integral as a reduced alternative to BWIM rather than a competitor. It returns only the gross weight of a load group, needs one displacement channel and only the scalar $C_m$ instead of an influence line or a full model, and involves a single division rather than a regularised inversion. Its natural role is low-cost screening across many secondary structures, with instrumented BWIM or enforcement weighing reserved for the vehicles it flags. The framework also extends to several sensors without new assumptions: with $s$ sensors each crossing gives a vector of integrals proportional to the same load, a one-parameter linear model estimated by weighted least squares with variance $(\mathbf c^\mathrm T\boldsymbol\Sigma^{-1}\mathbf c)^{-1}$. A near-blind sensor then carries almost no weight, so the maps of Figs. 2 and 3 double as sensor-selection charts; because zero drift is strongly correlated between sensors on one logger, $\boldsymbol\Sigma$ must be estimated rather than assumed diagonal.

### 7.2. Limitations

The laboratory tests used one small steel specimen with idealised supports and statically positioned loads; concrete cracking, creep, bearing friction and moving traffic are not represented. The accuracy class of the calibrated weights is not reported [NEED VALUE], and the Type A component was bounded rather than evaluated from the repeated cycles. The invariance is verified only indirectly, because the configurations differ in both load and spacing. A direct test with a fixed total load at several spacings needs no new apparatus, and the predicted blind configuration (spans of 2500 mm and 3644 mm on the same rig) is a falsifiable prediction; neither has yet been carried out. The dynamic study models a constant force and omits vehicle–bridge interaction and road roughness. The treatment is one-dimensional, so transverse load position is ignored; the eccentric readings at Cầu Mây show that it matters.

The bridge application rests on static parked-convoy data, nominal truck weights, an assumed depth law and a calibrated rather than measured pier stiffness, and the designer's FE model used for calibration is itself a model. A second three-span box girder (42 + 63 + 42 m) was examined, but its two-dimensional model could not reproduce the deflections reported for the designer's FE model (misfits of −11 %, +22 % and −12 %), and cross-section and pier dimensions are missing; it is therefore not analysed here. Repeating the analysis with the full design models and testing Eq. (2) with crawl passes of weighed vehicles on a continuous girder are the next steps.

---

## 8. Conclusions

This paper examined when the total load on a continuous girder is observable from the integral of a single deflection channel. The integral over a complete crossing equals the total load times a constant $C_m$ of the structure and the sensor position, a property that underlies influence-area weigh-in-motion. By reciprocity, $C_m$ is the deflection at the sensor under a uniform unit load, which makes it available before any instrument is installed.

This characterisation gives closed forms for continuous beams. For a two-span beam of uniform stiffness the blind span ratio is $(3+\sqrt{33})/6 = 1.45743$ and the optimal sensor position is $(1+\sqrt{33})/16 = 0.42154$ of the span. For a symmetric three-span beam instrumented at mid side span, the blind main-to-side ratio is $\beta = 1.700594$, the near-blind band begins at 1.621399, and beyond $2\cos(\pi/9) = 1.879385$ no side-span position gives a positive constant, so the whole side span reads mainly the main-span load.

On a laboratory two-span beam with statically positioned loads, two- and three-load groups were identified within 1.19 % by BPM and 0.70 % by SLM against direct weighing. The entire difference between the two methods was the calibration error of the reference record.

Applied to the acceptance-test data of the 55 + 90 + 55 m Cầu Mây box girder, the criterion showed that the installed side-span gauge is near-blind: the centre span cancels 82 % of its positive influence area, and $C_m$ changes about fourteenfold between pinned and fixed piers. The measured deflections were 0.92–0.94 of the design model, so a BPM estimate using design stiffness would underestimate the load by roughly 7–9 %. For haunched girders the normalised indicator depends on the reference stiffness, and the cancellation ratio $C_m/A^+$ is the clearer measure of span interaction. This application is a static consistency check, not a validation of the integral on a continuous bridge.

The error budget places zero-offset drift, not random noise, at the top of the field error hierarchy, and field crossing records confirm that baseline handling can change the integral by tens of per cent while low-pass filtering leaves it intact. For a constant moving force the quasi-static error is about 1 % at a crossing time of eight fundamental periods. Computing $|C_m|$ and $C_m/A^+$ for each candidate location is proposed as a routine step before installing a deflection sensor for load screening on continuous bridges.

---

## Appendix A. Two-span beam: influence line and closed form

For two equal spans $l$ with a knife-edge interior support, taking the support moment as redundant gives $M_B = -Px(l^2-x^2)/(4l^2)$ for a load on the first span. The reactions for a load at $0 \le x \le l$ are

$$R_A=P\,\frac{x^3-5l^2x+4l^3}{4l^3},\qquad R_B=P\,\frac{-x^3+3l^2x}{2l^3},\qquad R_C=P\,\frac{x^3-l^2x}{4l^3}, \tag{A.1}$$

and for $x = l/2$ they give the classical values $13P/32$, $11P/16$ and $-3P/32$. Double integration on $[0,x]$, $[x,l]$ and $[l,2l]$ with six displacement conditions ($y(0) = 0$; continuity of $y$ and $y'$ at the load; $y(l) = 0$ from each side; $y(2l) = 0$) gives the influence line at $s = l/2$:

$$\eta(x)=\frac{1}{EI}\begin{cases}\dfrac{x\,(9l^2-13x^2)}{192}, & 0\le x\le l/2,\\[2mm] \dfrac{(x-l)(4l^2-29lx+19x^2)}{192}, & l/2<x\le l,\\[2mm] \dfrac{(2l-x)(3l^2-4lx+x^2)}{64}, & l<x\le 2l.\end{cases} \tag{A.2}$$

Eq. (A.2) is continuous and twice differentiable at $x = l/2$ and $x = l$; the third branch carries the denominator $64EI$, not $192EI$.

At mid-span the deflection under a mid-span load is $2.875Pl^3/(192EI)$, 71.9 % of the simply supported value; the maximum over load position, at $x = 0.480l$, is 72.1 %.

For unequal spans, the uniform-load support moment is $M_B = -q_0(L_1^3/EI_1+L_2^3/EI_2)/[8(L_1/EI_1+L_2/EI_2)]$. Superposing the simply supported uniform-load deflection of span 1 and the deflection due to $M_B$, evaluating at $x_m$ and dividing by $q_0$ gives Eq. (4) with $\mu = -8M_B/(q_0L_1^2)$, which is Eq. (5). Differentiating $\mu$ with respect to $\rho_L$ gives a numerator $\rho_{EI}(3\rho_L^2-1)+2\rho_L^3$; for $\rho_{EI} = 1$, $\mu$ falls to 0.750 at $\rho_L = 1/2$, passes 1 at equal spans and reaches 3 at $\rho_L = 2$. Table A.1 lists the normalised constant against the span ratio for a mid-span sensor.

**Table A.1.** $192EI_1C_m/L_1^4$ against the span ratio, sensor at mid-span, uniform stiffness.

| $L_2/L_1$ | 0.5 | 0.7 | 0.8 | 1.0 | 1.2 | 1.3 | 1.4 | 1.45743 | 1.6 |
|---|---|---|---|---|---|---|---|---|---|
| Value | 1.375 | 1.315 | 1.240 | 1.000 | 0.640 | 0.415 | 0.160 | 0 | −0.440 |

## Appendix B. Monte Carlo robustness analysis

The study used 200 000 realisations of Eq. (16) per case: gain error alone ($\sigma_\gamma$ = 2 %), zero offset alone ($\sigma_\varepsilon$ = 0.005 mm), random noise alone ($\sigma_a$ = 0.0025 mm) and all three combined. Each realisation perturbed the measured record, recomputed the integral with the same rule and grid and re-identified the load. For SLM, an averaged (noise-free) reference and a single noisy reference were distinguished. Table B.1 gives the two-load results; the three-load case agrees within 0.1 percentage point. The bias column reflects the deviation of the measured record from weighing (Table 4) and is constant across error sources; the information is in the spread.

**Table B.1.** Monte Carlo results, two-load configuration (relative error with respect to weighing, %).

| Error source | Method | Reference | Bias | Std. dev. | p5 | p95 |
|---|---|---|---|---|---|---|
| Gain, $\sigma_\gamma$ = 2 % | BPM | — | +1.10 | 2.01 | −2.21 | +4.40 |
| | SLM | averaged | +0.61 | 2.00 | −2.69 | +3.90 |
| | SLM | single | +0.66 | 2.85 | −3.94 | +5.41 |
| Zero offset, $\sigma_\varepsilon$ = 0.005 mm | BPM | — | +1.10 | 0.64 | +0.05 | +2.15 |
| | SLM | averaged | +0.61 | 0.63 | −0.43 | +1.65 |
| | SLM | single | +0.62 | 1.19 | −1.31 | +2.60 |
| Random, $\sigma_a$ = 0.0025 mm | BPM | — | +1.10 | 0.07 | +0.99 | +1.21 |
| | SLM | averaged | +0.61 | 0.07 | +0.50 | +0.72 |
| | SLM | single | +0.61 | 0.13 | +0.40 | +0.82 |
| Combined | BPM | — | +1.10 | 2.12 | −2.39 | +4.59 |
| | SLM | averaged | +0.61 | 2.11 | −2.87 | +4.08 |
| | SLM | single | +0.65 | 3.09 | −4.34 | +5.83 |

## Appendix C. Laboratory data

**Table C.1.** Mid-span deflection of span AB (mm), mean of three cycles. Single load 40.64 N; analytical values from Eq. (A.2).

| $x$ (mm) | Analytical, single | Measured, single | Two loads | Three loads |
|---|---|---|---|---|
| 0 | 0.0000 | 0.0000 | 0 | 0 |
| 250 | 0.8874 | 0.8844 | 0.4625 | 0.5525 |
| 500 | 1.6968 | 1.6975 | 1.8813 | 1.0450 |
| 750 | 2.3501 | 2.3525 | 3.1413 | 2.5413 |
| 1000 | 2.7693 | 2.7738 | 4.0988 | 4.8700 |
| 1250 | 2.8764 | 2.8827 | 4.6350 | 6.7588 |
| 1500 | 2.6253 | 2.6363 | 4.6238 | 7.9350 |
| 1750 | 2.0980 | 2.1100 | 4.0688 | 8.2775 |
| 2000 | 1.4087 | 1.4213 | 3.1375 | 7.6825 |
| 2250 | 0.6713 | 0.6838 | 1.9600 | 6.2800 |
| 2500 | 0.0000 | 0.0000 | 0.7715 | 4.3725 |
| 2750 | −0.5132 | −0.5069 | −0.2689 | 2.2975 |
| 3000 | −0.8644 | −0.8556 | −1.0063 | 0.3021 |
| 3250 | −1.0715 | −1.0600 | −1.4988 | −1.2588 |
| 3500 | −1.1526 | −1.1438 | −1.7813 | −2.3650 |
| 3750 | −1.1255 | −1.1200 | −1.8600 | −3.0363 |
| 4000 | −1.0085 | −1.0013 | −1.7738 | −3.3300 |
| 4250 | −0.8194 | −0.8175 | −1.5525 | −3.2663 |
| 4500 | −0.5763 | −0.5816 | −1.2213 | −2.9450 |
| 4750 | −0.2971 | −0.3019 | −0.8125 | −2.4125 |
| 5000 | 0.0000 | 0.0000 | −0.3325 | −1.7088 |
| 5250 | | | 0 | −1.0713 |
| 5500 | | | | −0.3650 |
| 5750 | | | | 0 |

## Appendix D. Asymmetric three-span beams

For arbitrary $L_1, L_2, L_3$ and $EI_1, EI_2, EI_3$, the two support moments follow from the three-moment equations at B and C, solved symbolically; the sensor deflection under a uniform load then follows by superposition, as in Appendix A. The general expressions are long and are provided in the supplementary scripts. Four asymmetric cases agree with FE to a relative error of at most 9.2 × 10⁻¹². With the sensor at mid span 1 and uniform stiffness, the blind ratio $L_1/L_2$ is 0.589774, 0.591969, 0.587260, 0.565712, 0.525757 and 0.461410 for $L_3/L_2$ = 0.3, 0.5, 0.6, 0.8, 1.0 and 1.2.

---

## Computational implementation

All analyses were implemented by the authors in reproducible scripts: the symbolic verification of the two-span solution, the closed forms of Sections 2.2 and 2.3, the quadrature and Monte Carlo studies, the bridge model of Section 4, the record processing of Section 5 and the moving-load analysis of Section 6.5. Generative artificial intelligence was used as an assistance tool during code development and debugging. Every equation and numerical output was checked independently against an analytical, finite element or convergence-based route, and the scripts and the console output of each run are provided as supplementary material.

## CRediT authorship contribution statement

**Quoc-Bao Nguyen:** Conceptualization, Methodology, Formal analysis, Software, Writing – original draft. **Thai-Son Vu:** Conceptualization, Investigation, Validation, Supervision, Project administration, Writing – review & editing. **Hung-Son Nguyen:** Investigation, Data curation, Visualization, Writing – review & editing.

## Declaration of competing interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

## Funding

This research did not receive any specific grant from funding agencies in the public, commercial or not-for-profit sectors.

## Data availability

The laboratory deflection data supporting the findings are given in full in Appendix C. The derived data behind every figure and table, the analysis scripts and the console output of each run are provided as supplementary material. The Cầu Mây acceptance-test data were provided by [NEED VALUE: owner/consultant and permission statement] and are available from the corresponding author with the permission of the owner. The field crossing records of Section 5 are available under the same condition [NEED VALUE].

## Declaration of generative AI and AI-assisted technologies in the writing process

During the preparation of this work the authors used Claude (Anthropic) to assist with code development and debugging and with language editing. All scientific formulations, procedures, numerical results and interpretations were independently reviewed and verified by the authors, who take full responsibility for the content of the manuscript.

## Acknowledgements

The authors gratefully acknowledge the Laboratory of Transportation Technology and Systems, Faculty of Bridge and Road Engineering, Hanoi University of Civil Engineering, for providing the test facilities used in this study. [NEED VALUE: acknowledgement of the Cầu Mây owner (Hai Duong PMU) and of the testing consultant for access to the acceptance-test report, if the authors wish.]

---

## Figure captions

**Fig. 1.** Continuous beams considered: (a) two-span beam with instrumented span $L_1$, adjacent span $L_2$ and sensor at $\xi L_1$; (b) symmetric three-span beam with side spans $L_s$, main span $L_m = \beta L_s$ and side-span sensor at $\xi L_s$.

**Fig. 2.** Load observability of a two-span beam: (a) normalised constant $192EI_1C_m/L_1^4$ over the span and stiffness ratios for a mid-span sensor, with the closed-form blind locus of Eq. (6) (thick line) and the near-blind band $|192EI_1C_m/L_1^4| < 0.2$ (hatched); (b) dependence on sensor position for several span ratios, with the optimum $\xi^* = (1+\sqrt{33})/16$ for the symmetric case.

**Fig. 3.** Load observability of a three-span beam with uniform rigidity: (a) symmetric beam, $192EI_sC_m/L_s^4$ over $\beta$ and the side-span sensor position $\xi$, with the blind locus (thick line), the near-blind band (hatched), the optimum $\xi^*(\beta)$ (dashed) and the Cầu Mây layout (dot); (b) asymmetric beam, sensor at mid span 1, over $L_1/L_2$ and $L_3/L_2$.

**Fig. 4.** Laboratory specimen: (a) elevation and instrumentation; (b) general view of the test rig.

**Fig. 5.** Mid-span deflection of span AB against the position of a single 40.64 N load: analytical, FE and measured. The lower panel gives the absolute difference between measurement and theory. Shaded areas are the positive and negative contributions to the deflection integral.

**Fig. 6.** Measured deflection integral against total applied load for the three configurations, with the theoretical slope $l^4/(192EI)$.

**Fig. 7.** Cầu Mây main bridge (55 + 90 + 55 m): (a) assumed stiffness profile $EI(x)/EI_\mathrm{mid}$ ($n = 2.943$, $L_v = 44$ m); (b) deflection influence lines at the installed gauges N8 (0.4L of the side span) and N7 (mid centre span) for pinned piers, the calibrated pier stiffness $k_\mathrm{FE}$ and fixed piers, with the positive and negative areas shaded for $k_\mathrm{FE}$.

**Fig. 8.** Deviation of the event deflection integral from the linear pre/post baseline for each crossing record, for tare-only, cubic and high-pass (0.1 Hz and 0.5 Hz) baselines.

**Fig. 9.** Field crossing records before and after a 2 Hz zero-phase low-pass filter (left) and the dynamic residual (right), with the ratio of filtered to unfiltered integrals.

**Fig. 10.** Error of the quasi-static deflection-integral estimator for a constant force crossing the laboratory beam, against the ratio of crossing time to fundamental period. Shaded bands mark ±1 % and ±5 %.

---

## References

[1] Y. Fan, J. Zhu, J. Pei, Z. Li, Analysis for Yangmingtan Bridge collapse, Eng. Fail. Anal. 56 (2015) 20–27. https://doi.org/10.1016/j.engfailanal.2015.05.003

[2] H.M. Salem, H.M. Helmy, Numerical investigation of collapse of the Minnesota I-35W bridge, Eng. Struct. 59 (2014) 635–645. https://doi.org/10.1016/j.engstruct.2013.11.022

[3] S. Invernizzi, F. Montagnoli, A. Carpinteri, Very high cycle corrosion fatigue study of the collapsed Polcevera bridge, Italy, J. Bridge Eng. 27 (1) (2022) 04021102. https://doi.org/10.1061/(ASCE)BE.1943-5592.0001807

[4] M. Morgese, F. Ansari, M. Domaneschi, G.P. Cimellaro, Post-collapse analysis of Morandi's Polcevera viaduct in Genoa, Italy, J. Civ. Struct. Health Monit. 10 (2020) 69–85. https://doi.org/10.1007/s13349-019-00370-7

[5] R. Ventura, B. Barabino, G. Maternini, Estimating the frequency of traffic overloading on road bridges, J. Traffic Transp. Eng. (Engl. Ed.) 11 (4) (2024) 776–796. https://doi.org/10.1016/j.jtte.2023.11.005

[6] F. Fattorini, W. Salvatore, E. Renzi, G. Tamasi, Application to the territorial authorities of the guidelines for the classification and management of risk of existing bridges: the case study of the Municipality of Rome, Procedia Struct. Integr. 44 (2023) 689–696. https://doi.org/10.1016/j.prostr.2023.01.090 [check exact title wording]

[7] J. Gajda, R. Sroka, P. Burnos, M. Daniol, Long-term assessment of the properties of load sensors applied in weigh-in-motion systems, Sensors 25 (8) (2025) 2421. https://doi.org/10.3390/s25082421

[8] I. Al-Qadi, H. Wang, Y. Ouyang, K. Grimmelsman, J.E. Purdy, LTBP Program's Literature Review on Weigh-in-Motion Systems, Report FHWA-HRT-16-024, Federal Highway Administration, Washington, DC, 2016. https://rosap.ntl.bts.gov/view/dot/35735

[9] B. Jacob, E.J. OBrien, S. Jehaes (Eds.), Weigh-in-Motion of Road Vehicles: Final Report of the COST 323 Action, LCPC, Paris, 2002.

[10] U.S. Department of Transportation, Federal Highway Administration, Comprehensive Truck Size and Weight Study, Vol. II: Issues and Background, Report FHWA-PL-00-029, Washington, DC, 2000. https://rosap.ntl.bts.gov/view/dot/4747 [CAN_TAC_GIA: confirm this is the document intended]

[11] F. Moses, Weigh-in-motion system using instrumented bridges, Transp. Eng. J. ASCE 105 (3) (1979) 233–249. https://doi.org/10.1061/TPEJAN.0000783

[12] E.J. OBrien, M.J. Quilligan, R. Karoumi, Calculating an influence line from direct measurements, Proc. Inst. Civ. Eng. Bridge Eng. 159 (1) (2006) 31–34. https://doi.org/10.1680/bren.2006.159.1.31

[13] E.J. OBrien, C.W. Rowley, A. González, M.F. Green, A regularised solution to the bridge weigh-in-motion equations, Int. J. Heavy Veh. Syst. 16 (3) (2009) 310–327. https://doi.org/10.1504/IJHVS.2009.027135

[14] A. Žnidarič, J. Kalin, M. Kreslin, Improved accuracy and robustness of bridge weigh-in-motion systems, Struct. Infrastruct. Eng. 14 (4) (2018) 412–424. https://doi.org/10.1080/15732479.2017.1406958

[15] Y. Yu, C.S. Cai, L. Deng, State-of-the-art review on bridge weigh-in-motion technology, Adv. Struct. Eng. 19 (9) (2016) 1514–1530. https://doi.org/10.1177/1369433216655922

[16] T. Ojio, C. Carey, E.J. OBrien, C. Doherty, S.E. Taylor, Contactless bridge weigh-in-motion, J. Bridge Eng. 21 (7) (2016) 04016032. https://doi.org/10.1061/(ASCE)BE.1943-5592.0000776

[17] W. He, T. Ling, E.J. OBrien, et al., Virtual axle method for bridge weigh-in-motion systems requiring no axle detector, J. Bridge Eng. 24 (9) (2019) 04019086. https://doi.org/10.1061/(asce)be.1943-5592.0001474

[18] S.S. Law, T.H.T. Chan, Q.H. Zeng, Moving force identification: a time domain method, J. Sound Vib. 201 (1) (1997) 1–22. https://doi.org/10.1006/jsvi.1996.0774

[19] T.H.T. Chan, S.S. Law, T.H. Yung, X.R. Yuan, An interpretive method for moving force identification, J. Sound Vib. 219 (3) (1999) 503–524. https://doi.org/10.1006/jsvi.1998.1904

[20] S.S. Law, X.Q. Zhu, Study on different beam models in moving force identification, J. Sound Vib. 234 (4) (2000) 661–679. https://doi.org/10.1006/jsvi.2000.2867

[21] X.Q. Zhu, S.S. Law, Moving load identification on multi-span continuous bridges with elastic bearings, Mech. Syst. Signal Process. 20 (7) (2006) 1759–1782. https://doi.org/10.1016/j.ymssp.2005.06.004

[22] L. Deng, C.S. Cai, Identification of dynamic vehicular axle loads: theory and simulations, J. Vib. Control 16 (14) (2010) 2167–2194. https://doi.org/10.1177/1077546309351221

[23] Z. Chen, Y. Fang, X. Kong, L. Deng, Identification of multi-axle vehicle loads on beam type bridge based on minimal residual norm steepest descent method, J. Sound Vib. 563 (2023) 117866. https://doi.org/10.1016/j.jsv.2023.117866

[24] S. Luo, J. Jiang, F. Zhang, M.S. Mohamed, Distributed dynamic load identification of beam structures using a Bayesian method, Appl. Sci. 13 (4) (2023) 2537. https://doi.org/10.3390/app13042537

[25] J. Jiang, S. Luo, M.S. Mohamed, Z. Liang, Real-time identification of dynamic loads using inverse solution and Kalman filter, Appl. Sci. 10 (19) (2020) 6767. https://doi.org/10.3390/app10196767

[26] T. Kapoor, H. Wang, A. Núñez, R. Dollevoet, Physics-informed machine learning for moving load problems, J. Phys. Conf. Ser. 2647 (2024) 152003. https://doi.org/10.1088/1742-6596/2647/15/152003

[27] A.J. Cardini, J.T. DeWolf, Implementation of a long-term bridge weigh-in-motion system for a steel girder bridge in the interstate highway system, J. Bridge Eng. 14 (6) (2009) 418–423. https://doi.org/10.1061/(ASCE)1084-0702(2009)14:6(418)

[28] J. Yang, P. Hou, C. Yang, Study on the method of moving load identification based on strain influence line, Appl. Sci. 11 (2) (2021) 853. https://doi.org/10.3390/app11020853

[29] J. Yang, P. Hou, C. Yang, Investigation on the moving load identification for bridges based on long-gauge strain sensing and skew-Laplace fitting, Smart Mater. Struct. 32 (8) (2023) 085026. https://doi.org/10.1088/1361-665x/ace4ac

[30] J. Zhu, C. Wang, T. Qi, Y. Zhou, Vehicle load identification on orthotropic steel box beam bridge based on the strain response area, Appl. Sci. 12 (23) (2022) 12394. https://doi.org/10.3390/app122312394

[31] P. Agüero-Barrantes, R.E. Christenson, S. Lobo-Aguilar, Utilizing Kriging metamodeling to provide practical and effective bridge weigh-in-motion, J. Bridge Eng. 28 (2) (2023) 04022138. https://doi.org/10.1061/jbenf2.beeng-5760

[32] N. Zolghadri, M.W. Halling, N.R. Johnson, P.J. Barr, Field verification of simplified bridge weigh-in-motion techniques, J. Bridge Eng. 21 (6) (2016) 04016063. https://doi.org/10.1061/(asce)be.1943-5592.0000930

[33] S. Shi, M. Yarnold, S. Hurlebaus, Evaluation of a load cell-based bridge weigh-in-motion system, Transp. Res. Rec. 2679 (2024) 535–549. https://doi.org/10.1177/03611981241263336

[34] A. Döring, M. Vogelbacher, O. Schneider, Investigations of ratio-based integrated influence lines as features for bridge-damage detection, Infrastructures 8 (4) (2023) 72. https://doi.org/10.3390/infrastructures8040072

[35] D. Huang, Y. Lu, Influence line theory supported single sensor-based strain feature for bridge defect diagnosis, Struct. Health Monit. (2025), online. https://doi.org/10.1177/14759217251376931

[36] Q.B. Nguyen, T. Hoang, H.S. Nguyen, [Determination of the load applied on a simply supported beam based on measured deflection data], J. Sci. Technol. Civ. Eng. (HUCE) 18 (2V) (2024) 61–71 (in Vietnamese). https://doi.org/10.31814/stce.huce2024-18(2V)-05

[37] M.T.A. Chaudhary, M. Morgese, T.W. Taylor, F. Ansari, Method and application for influence-line-free distributed detection of gross vehicle weights in bridges, Structures 73 (2025) 108298. https://doi.org/10.1016/j.istruc.2025.108298

[38] C. Zhou, C. Demartino, Y. Narazaki, Y. Xu, E. Chatzi, B.F. Spencer, Optimal sensor placement for bridge weigh-in-motion using an augmented Kalman filter, Mech. Syst. Signal Process. 241 (2025) 113522. https://doi.org/10.1016/j.ymssp.2025.113522

[39] J. Zhang, Y. Liu, X. Fan, An AR(1)-Tikhonov-SVD-GCV framework for stochastic moving load identification driven by bridge multi-point deflection data, Structures 88 (2026) 111844. https://doi.org/10.1016/j.istruc.2026.111844

[40] Z. Shen, W. Peng, X. Zhang, et al., A lightweight weigh-in-motion system based on vehicle-induced bridge deflection and impact dynamic responses, Int. J. Struct. Stab. Dyn. (2026), online. https://doi.org/10.1142/s0219455427503664

[41] Dassault Systèmes Simulia, ABAQUS/Standard User's Manual, Version 6.9, 2009.

[42] L. Frýba, Vibration of Solids and Structures under Moving Loads, 3rd ed., Thomas Telford, London, 1999.

[43] JCGM 100:2008, Evaluation of Measurement Data – Guide to the Expression of Uncertainty in Measurement, BIPM, Sèvres, 2008.

[44] H. Sohn, [NEED VALUE: title], Philos. Trans. R. Soc. A 365 (1851) (2007) 539–560. [NEED VALUE: DOI and title check from the JCSHM reference list]

[45] E.J. Cross, K.Y. Koo, J.M.W. Brownjohn, K. Worden, [NEED VALUE: title], Mech. Syst. Signal Process. 35 (1–2) (2013) 16–34. [NEED VALUE: DOI and title check from the JCSHM reference list]

[46] EN 1991-2:2003, Eurocode 1: Actions on Structures – Part 2: Traffic Loads on Bridges, CEN, Brussels, 2003.

[47] AASHTO, LRFD Bridge Design Specifications, 10th ed., American Association of State Highway and Transportation Officials, Washington, DC, 2024. [NEED VALUE: confirm edition and year]
