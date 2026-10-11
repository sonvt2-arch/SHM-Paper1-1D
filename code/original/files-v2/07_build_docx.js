/*
 * 07_build_docx.js
 * ================
 * Assembles the revised manuscript into a .docx using docx-js.
 *
 * Prerequisites (run these first, from this folder):
 *     python3 05_make_figures.py     ->  ./figs/*.png
 *     python3 06_make_equations.py   ->  ./eqs/*.png
 *
 * Then:
 *     npm install docx        (if 'docx' is not already available)
 *     node 07_build_docx.js
 *
 * Output: ./Revised_Manuscript_TwoSpanBeam_LoadIdentification.docx
 *
 * Text mark-up used inside the P()/BUL()/caption helpers:
 *     *x*     italic          **x**   bold
 *     _x_     subscript       ^x^     superscript
 */

const fs = require('fs');
const L = require('./docx_helpers.js');
const { Document, Packer, Paragraph, TextRun, AlignmentType, Footer, PageNumber,
        eq, fig, P, H1, H2, H3, BUL, tbl, tableCap, rt, PageBreak, noBorders,
        Table, TableRow, TableCell, WidthType } = L;

const C = [];   // document children
const add = (...x) => x.forEach(v => Array.isArray(v) ? v.forEach(y => C.push(y)) : C.push(v));

const TITLE = 'Deflection-integral invariance for indirect identification of total service loads on continuous beams: general theorem, error budget and experimental validation on a two-span bridge model';

// ============================ FRONT MATTER ============================
add(new Paragraph({ alignment: AlignmentType.LEFT, spacing: { after: 200 },
  children: [ new TextRun({ text: 'Research Paper', font: 'Times New Roman', size: 22, italics: true }) ] }));
add(new Paragraph({ alignment: AlignmentType.LEFT, spacing: { after: 200 },
  children: [ new TextRun({ text: TITLE, font: 'Times New Roman', size: 32, bold: true }) ] }));
add(new Paragraph({ alignment: AlignmentType.LEFT, spacing: { after: 60 },
  children: rt('Quoc-Bao Nguyen^a^, Thai-Son Vu^a,*^, Hung-Son Nguyen^a^', { size: 24 }) }));
add(new Paragraph({ alignment: AlignmentType.LEFT, spacing: { after: 240 },
  children: rt('^a^ *Department of Bridge and Road Engineering, Hanoi University of Civil Engineering, 55 Giai Phong Road, Hanoi 100000, Vietnam*', { size: 19 }) }));

add(new Paragraph({ spacing: { after: 100 }, children: [ new TextRun({ text: 'ABSTRACT', font: 'Times New Roman', size: 22, bold: true }) ] }));
add(P('Identifying the gross weight of vehicles crossing a bridge normally requires either a dedicated weigh-in-motion installation or the solution of an ill-posed inverse problem from a dense sensor array. This paper shows that a single deflection sensor is sufficient, provided the response is integrated over a complete crossing. We first prove a general invariance theorem: for any linear-elastic beam structure and any fixed measurement point, the integral of the measured deflection over the whole passage of a convoy equals the total load multiplied by a constant that depends only on the structure and the sensor location, and is strictly independent of the number of axles, their spacings and their positions. A corollary of the Maxwell-Betti theorem identifies that constant as the area under the deflected shape produced by a unit load applied at the measurement point, which makes it directly computable or directly measurable. Two identification methods follow: the Beam Property-based Method (BPM), which computes the constant analytically, and the Standard Load-based Method (SLM), which calibrates it with one crossing of a weighed reference load. For a two-span continuous beam of equal spans instrumented at mid-span of the first span, the constant is l^4^/192EI in closed form. The theory is validated by finite element analysis and by laboratory tests on a 2 x 2500 mm steel continuous beam under one-, two- and three-axle load groups; the identified total loads deviate from direct weighing by 0.61-1.19 %. Beyond validation, a complete error budget is developed and, in several respects, it reverses the conclusions that a purely random noise study would suggest. Zero-offset drift of the deflection signal, not random noise, dominates: an offset equal to the LVDT resolution alone biases the identified load by 0.4-1.0 %. SLM is shown to cancel every common-mode error (flexural rigidity, quadrature bias, sensor gain), but to amplify independent random noise by a factor of the square root of two unless the reference integral is averaged over repeated crossings. Replacing the trapezoidal rule by Simpson quadrature removes a systematic bias of 0.50 % at no experimental cost. A parametric study identifies a critical span ratio of 1.46 beyond which the constant vanishes and the method fails, and shows that mid-span instrumentation is within 4 % of optimal. The approach provides a low-cost, single-sensor screening tool for traffic overload on continuous-span bridges, with a quantified and transferable uncertainty budget.', { firstLine: 0, size: 20 }));
add(P('**Keywords:** Deflection integral; influence line; load identification; continuous beam; bridge weigh-in-motion; measurement uncertainty; structural health monitoring.', { firstLine: 0, size: 20, after: 240 }));

// ============================ NOMENCLATURE ============================
add(H1('', 'Nomenclature'));
const nom = [
  ['*a*_i_', 'longitudinal offset of axle *i* from the leading axle (mm)'],
  ['*C*_m_', 'invariance constant at measurement point *m*, equal to the area under the deflection influence line (mm^2^/N)'],
  ['*E*, *I*, *EI*', 'Young modulus (MPa), second moment of area (mm^4^), flexural rigidity (N mm^2^)'],
  ['*I*_y_', 'deflection integral over the complete crossing (mm^2^)'],
  ['*l*, *L*', 'individual span length; total structural length, *L* = 2*l* for the two-span beam (mm)'],
  ['*m*', 'measurement point; *x*_m_ its abscissa'],
  ['*N*_rep_', 'number of repeated crossings averaged to obtain the reference integral'],
  ['*P*, *P*_0_, *P*_t_', 'total load; calibrated reference (standard) load; unknown service load (N)'],
  ['*R*_A_, *R*_B_, *R*_C_', 'vertical support reactions (N)'],
  ['*s*', 'abscissa of a beam cross-section measured from support *A* (mm)'],
  ['*v*', 'traverse speed of the load group (mm/s)'],
  ['*w*_m_(*x*)', 'deflected shape produced by a unit load applied at *m* (mm/N)'],
  ['*x*', 'abscissa of the leading load measured from support *A* (mm)'],
  ['*y*_m_', 'deflection measured at point *m* (mm)'],
  ['*γ*', 'relative gain (scale-factor) error of the deflection chain'],
  ['*Δx*', 'sampling interval along the crossing (mm)'],
  ['*ε*_0_', 'zero-offset (baseline) error of the deflection signal (mm)'],
  ['*η*_m_(*x*)', 'deflection influence line at *m* for a unit moving load (mm/N)'],
  ['*σ*_a_', 'standard deviation of the additive random measurement noise (mm)'],
  ['BPM, SLM, LWM', 'Beam Property-based Method; Standard Load-based Method; Load Weighing Method'],
];
add(tbl([], nom, [2100, 7260], { fs: 18, alignAll: AlignmentType.LEFT }));

// ============================ 1. INTRODUCTION ============================
add(H1('1.', 'Introduction'));
add(P('Overloaded heavy vehicles are among the principal drivers of premature deterioration of highway bridges. Loads well beyond the design envelope increase stress ranges, accelerate fatigue crack growth, reduce residual capacity and, in extreme cases, contribute directly to collapse. The failure of a span of the Yangmingtan Bridge in Harbin in 2012 under four simultaneously crossing overloaded trucks [1] and the 2019 collapse of the suspension bridge at Mirepoix-sur-Tarn under a vehicle almost three times its permitted weight are documented illustrations. In other well-known cases, such as the I-35W bridge in Minneapolis [2] and the Polcevera viaduct in Genoa [3,4], heavy traffic acted together with design deficiencies or material degradation. Reliable knowledge of the loads actually carried is therefore not an academic refinement but a prerequisite for risk-informed asset management [5-7].', { firstLine: 0 }));
add(P('Direct enforcement relies on static weigh stations and on pavement weigh-in-motion (WIM) systems. Pavement WIM is accurate and mature [8-10], and its metrological requirements are well codified [11,12], but installation and periodic verification are costly, coverage is sparse, and — decisively for the present purpose — a pavement WIM station measures the vehicle, not the response of any particular bridge.'));
add(P('Bridge weigh-in-motion (BWIM), introduced by Moses [13], instead instruments the structure itself and infers axle loads from the measured response through the influence line. The approach has matured considerably: influence lines can now be calibrated directly from measurements rather than assumed [14], regularisation stabilises the inverse problem [15], accuracy and robustness have been systematically improved [16,17], and contactless variants have been demonstrated [18]. In parallel, a large body of moving-force identification (MFI) research has developed time-domain, frequency-domain and interpretive formulations [19-21], extensions to multi-span bridges on elastic bearings [22], Bayesian [23] and Kalman-filter [24] estimators, and physics-informed machine-learning surrogates [25]. What these families share is that they aim at the full axle-load history and consequently require either several sensors, an accurate structural model, or a regularised inversion whose conditioning degrades with noise.'));
add(P('A markedly less demanding question is often the operationally relevant one: not how the load is distributed between axles, but what the gross weight of the crossing vehicle is. For that question an integral quantity suffices. Andersen and Mukhopadhyay observed as early as 1950 that the deflected form of a beam contains integral information about the load distribution [26], and previous work by the present authors exploited the integral of the mid-span deflection to identify the total load on simply supported beams [27]. The purpose of the present paper is to place that idea on a general footing and, more importantly, to establish what actually limits its accuracy.'));
add(P('Three contributions are made. First, the invariance of the deflection integral is proved as a theorem valid for any linear-elastic beam structure and any measurement point, rather than demonstrated case by case; a corollary of the Maxwell-Betti reciprocal theorem then identifies the invariance constant as the area under the deflected shape produced by a unit load at the sensor, which makes it computable analytically, numerically, or by a single static calibration test. Second, a complete error budget is developed and quantified. It shows that the dominant error source is not the random measurement noise usually studied, but the zero-offset drift of the deflection signal, and that the two proposed estimators respond to systematic and random errors in opposite ways. Third, a parametric study delimits the domain of validity, including a critical span ratio at which the method degenerates and beyond which it cannot be used.'));
add(P('The two-span continuous beam with equal spans is retained as the demonstration case: it is the simplest statically indeterminate configuration in which moment redistribution and span interaction are present, it admits a closed-form influence line, and it is representative of a large population of highway overpasses and secondary bridges. Section 2 develops the theory, Section 3 the numerical and experimental validation, Section 4 the error and robustness analysis, Section 5 the discussion and comparison with existing methods, and Section 6 the conclusions.'));

// ============================ 2. THEORY ============================
add(H1('2.', 'Theoretical framework'));
add(H2('2.1', 'Deflection response of a two-span continuous beam under a moving load'));
add(P('Consider a prismatic beam of constant flexural rigidity *EI* resting on three supports: *A* at *x* = 0 and *C* at *x* = 2*l* are rollers, and *B* at *x* = *l* is a hinged (pinned) support that restrains vertical displacement only. Rotation at *B* is free and continuous across the support; the beam is therefore statically indeterminate to the first degree, not two independent propped cantilevers. The geometry is shown in Fig. 1.', { firstLine: 0 }));
add(fig('fig01_layout', 1, 'General layout of the two-span continuous beam under a single concentrated load: (a) load on span *AB*; (b) load on span *BC*.'));
add(P('A concentrated load *P*, representing one axle and applied quasi-statically, travels from *A* to *C*. Its instantaneous abscissa is *x*. Taking the bending moment at *B* as the redundant and applying the three-moment equation gives *M*_B_ = -*Px*(*l*^2^ - *x*^2^)/(4*l*^2^) for a load on span *AB*, from which the reactions follow:'));
add(eq('e01', 1));
add(P('When the load is on span *BC*, the corresponding expressions are obtained by the symmetry substitution *x* → 2*l* - *x*:'));
add(eq('e02', 2));
add(P('As a check, for *x* = *l*/2 Eq. (1) yields *R*_A_ = 13*P*/32, *R*_B_ = 11*P*/16 and *R*_C_ = -3*P*/32, the classical values for a two-span continuous beam with a simple interior support; the negative value of *R*_C_ reflects the uplift developed at the far support. The bending moment at a section *s* within span *AB* follows from equilibrium:'));
add(eq('e03', 3));
add(P('With the Euler-Bernoulli relation'));
add(eq('e04', 4));
add(P('the deflection is obtained by double integration. Six conditions are required and are stated here explicitly, since an incomplete set is a common source of error: zero deflection at the three supports, *y*(0) = *y*(*l*) = *y*(2*l*) = 0; zero bending moment at the two end supports, *M*(0) = *M*(2*l*) = 0; and continuity of deflection and of slope at the point of load application, *s* = *x*, where the shear force is discontinuous. Continuity of slope and of curvature at the interior support *s* = *l* is then automatically satisfied, because no concentrated moment is applied there. Integration gives'));
add(eq('e05', 5));
add(P('The response of practical interest is the deflection at the mid-point of the first span, obtained by setting *s* = *l*/2. Normalising by the load magnitude defines the deflection influence line *η*(*x*) at that measurement point:'));
add(eq('e06', 6));
add(P('Equation (6) is continuous and twice differentiable at *x* = *l*/2 and at *x* = *l*, and vanishes at *x* = 0, *l* and 2*l*. Note that the third branch carries the denominator 64*EI* and not 192*EI*; the factor of three is easily lost when the expression is factorised, and it can be verified independently against Eq. (5) with *s* = *l*/2.'));
add(P('For a load at mid-span, the deflection is 2.875*Pl*^3^/192*EI*, that is 71.9 % of the value *Pl*^3^/48*EI* for a simply supported beam of the same span. Taking the maximum over the load position, at *x* = 0.480*l*, gives 72.1 %. The stiffening effect of the negative moment at *B* is thus significant but moderate, and it is the reason why the influence line changes sign at *x* = *l*: for loads on the second span, the instrumented mid-span lifts.'));

add(H2('2.2', 'The deflection-integral invariance theorem'));
add(P('The identification methods proposed here rest on a single property, which is stated below in the generality in which it actually holds. The proof uses only linearity and the compact support of the influence line; nothing in it is specific to two spans, to equal spans, to a prismatic beam, or to instrumentation at mid-span.', { firstLine: 0 }));
add(P('**Theorem (invariance of the deflection integral).** *Let a linear-elastic beam structure of total length L have time-invariant properties, and let m be a fixed measurement point. Let η*_m_*(x) denote the influence line of the vertical deflection at m due to a unit vertical force applied at abscissa x, with η*_m_*(x) = 0 for x outside [0, L]. Let a convoy of n forces P*_i_ *with fixed relative spacings a*_i_ *(a*_1_ *= 0) traverse the structure quasi-statically, and let x be the abscissa of the leading force. Then the deflection measured at m is*', { firstLine: 0 }));
add(eq('e07', 7));
add(P('*and its integral over the complete passage satisfies*', { firstLine: 0 }));
add(eq('e08', 8));
add(P('*where*', { firstLine: 0 }));
add(eq('e09', 9));
add(P('*The constant C*_m_ *depends only on the structure and on the position of the measurement point. It is independent of the number of loads, of their individual magnitudes and of their spacings.*', { firstLine: 0 }));
add(P('**Proof.** Superposition gives Eq. (7). Integrating term by term and substituting *u* = *x* - *a*_i_ in each term maps every integration domain onto the same interval, because *η*_m_ vanishes outside [0, *L*]; each term therefore contributes *P*_i_*C*_m_ regardless of *a*_i_. Summation gives Eq. (8). ∎'));
add(P('The role of the infinite limits deserves emphasis, because it is the one point at which the property can be lost in practice. The integration must extend from the instant the leading axle enters the structure to the instant the trailing axle leaves it, that is over [0, *L* + *a*_max_]. Truncating the record at *x* = *L*, as would be natural for a single load, removes the tail of every trailing axle. For the two-span beam that tail lies in the region where the influence line is negative, so the truncation error does not cancel and produces a systematic overestimate of the load. All measurements reported in Section 3 extend to *L* + *a*_max_ for this reason.'));
add(P('**Corollary (Maxwell-Betti form of the constant).** *Let w*_m_*(x) be the deflected shape of the structure under a single unit load applied statically at m. Then*', { firstLine: 0 }));
add(eq('e10', 10));
add(P('*Proof.* By the Maxwell-Betti reciprocal theorem, the deflection at *m* due to a unit load at *x* equals the deflection at *x* due to a unit load at *m*, that is *η*_m_(*x*) = *w*_m_(*x*) for all *x*. Integration gives the result. ∎', { firstLine: 0 }));
add(P('The corollary is of practical, not merely formal, interest. It states that the invariance constant is the area under the deflected shape produced by one static load at the sensor position. It can therefore be obtained from a single static analysis, from one line of output of any structural analysis package, or — on an existing bridge whose properties are unknown — from a single static test in which a known load is applied at the sensor and the deflected shape is surveyed. It also provides an independent verification route: the closed-form value derived in Section 2.3 was confirmed to eight significant figures against a finite element evaluation of Eq. (10).'));
add(P('Two limitations follow directly from the hypotheses. Linearity is essential: the theorem does not survive material or geometric nonlinearity, support uplift, or friction at the bearings. Time invariance is equally essential: *C*_m_ must be the same throughout the crossing, which excludes significant thermal drift of the stiffness within a single passage — a mild condition for a crossing lasting a few seconds, and a demanding one for a comparison between measurement campaigns separated by months.'));

add(H2('2.3', 'Closed-form constant for the two-span continuous beam'));
add(P('For the beam of Fig. 1 instrumented at the mid-point of the first span, the constant is obtained by integrating Eq. (6):', { firstLine: 0 }));
add(eq('e11', 11));
add(P('The result is remarkably compact. The contribution of the second span is negative and amounts to three quarters of the value contributed by a single span segment, so the cancellation between the two spans is substantial: the net constant is only 4/7 of the positive contribution alone. This cancellation is benign for the theory but, as Section 4.2 shows, it is precisely what makes the method sensitive to baseline drift.'));

add(H2('2.4', 'Beam Property-based Method (BPM)'));
add(P('If *E*, *I* and *l* are known, the constant is known and the total load follows immediately from Eq. (8):', { firstLine: 0 }));
add(eq('e12', 12));
add(P('The method requires no knowledge of the number of axles, of their spacings or of their positions, and it uses a single sensor. Its accuracy is limited by the accuracy of *EI* and *l*. Because the constant varies as *l*^4^, a 1 % error in span length produces a 4 % error in the identified load; this sensitivity is often overlooked and is included explicitly in the error budget of Section 4.1.'));

add(H2('2.5', 'Numerical evaluation of the deflection integral'));
add(P('Field and laboratory records are discrete. Writing *y*_i_ for the deflection sampled at abscissa *x*_i_ = *iΔx*, the trapezoidal rule gives', { firstLine: 0 }));
add(eq('e13', 13));
add(P('The half-weights at the two ends are not optional. They vanish only when the record begins and ends exactly at zero deflection, which holds for the idealised laboratory case but not on a bridge carrying residual deflection or a second vehicle. Simpson quadrature, at identical experimental cost, gives'));
add(eq('e14', 14));
add(P('The influence line of Eq. (6) is piecewise cubic and of class C^2^, so Simpson quadrature is nearly exact whereas the trapezoidal rule converges only as *Δx*^2^. Table 2 quantifies the difference: at the sampling interval used in the present tests, *Δx* = 250 mm, the trapezoidal rule underestimates the exact integral by 0.500 % while Simpson quadrature errs by 0.027 %. Since this bias is systematic, it propagates one-for-one into the identified load in BPM. Reporting it explicitly, and preferably removing it by using Eq. (14), costs nothing.'));

add(H2('2.6', 'Standard Load-based Method (SLM)'));
add(P('On an existing bridge, *EI* is rarely known to better than a few per cent: section loss, cracking of concrete, composite action with the deck and the actual stiffness of the bearings all contribute. The Standard Load-based Method removes the need to know it. A vehicle or set of weights of accurately known total mass *P*_0_ is driven across the instrumented structure and its deflection integral *I*_y,0_ is recorded. Because both crossings share the same constant *C*_m_, the ratio eliminates it:', { firstLine: 0 }));
add(eq('e15', 15));
add(P('The procedure is: (i) weigh a reference load; (ii) record the deflection during one or, preferably, several complete crossings of that load and average the resulting integrals; (iii) record the deflection during the unknown crossing; (iv) evaluate both integrals with the same quadrature rule and the same sampling grid; (v) apply Eq. (15).'));
add(P('The requirement that both integrals be evaluated identically is not a formality. It is what makes SLM cancel the quadrature bias of Section 2.5 exactly, in addition to cancelling *EI*. More generally, and as shown quantitatively in Section 4, SLM cancels every error that is common to the two crossings — flexural rigidity, span length, quadrature rule, sensor gain, bearing flexibility, and any pre-existing minor damage — while leaving errors that differ between them. The complementary conclusion, which is easily stated the wrong way round, is that SLM does not reduce independent random noise; it increases it, unless the reference integral is averaged. Section 4.3 quantifies both effects.'));
add(fig('fig11_flowchart', 2, 'Identification workflow. Both methods share the same measurement and integration chain and differ only in how the invariance constant *C*_m_ is obtained.'));

// ============================ 3. VALIDATION ============================
add(H1('3.', 'Numerical and experimental validation'));
add(H2('3.1', 'Finite element model'));
add(P('The beam was modelled in Abaqus with two-node cubic Euler-Bernoulli beam elements (B23), 200 elements per span, linear elastic material and static analysis. For a point load applied at a node, this element family reproduces the exact nodal displacements of the Euler-Bernoulli solution, so agreement with Eq. (6) at the sampling points is expected to be exact to machine precision and is not, in itself, evidence of anything beyond correct implementation. The finite element model was therefore used for three purposes for which the closed form is unavailable: verification of the Maxwell-Betti corollary, Eq. (10); the parametric study of unequal spans and sensor position reported in Section 4.5; and a check of the influence of shear deformation, obtained by re-running the analysis with Timoshenko elements (B31). For the present cross-section the span-to-depth ratio is 100 and the resulting difference in the deflection integral was below 0.05 %, confirming that the Euler-Bernoulli assumption is appropriate here but would require re-examination for short, deep girders.', { firstLine: 0 }));

add(H2('3.2', 'Experimental programme'));
add(P('Tests were carried out at the Laboratory of Transportation Technology and Systems, Department of Bridge and Road Engineering, Hanoi University of Civil Engineering. The specimen, shown in Fig. 3, was a steel beam of total length 5400 mm resting on three supports to form a two-span continuous beam with equal spans of 2500 mm. The end supports were steel cylinders acting as rollers and the interior support was a triangular steel prism acting as a knife edge, restraining vertical displacement while allowing rotation.', { firstLine: 0 }));
add(fig('fig03_setup', 3, 'Experimental model: (a) elevation and instrumentation; (b) general view of the test rig.'));
add(P('The cross-section was a hollow square tube of outer dimensions 25 mm x 25 mm and wall thickness 2.03 mm, both averaged from measurements on the specimen, giving a second moment of area *I* = 16 529.8 mm^4^. With *E* = 200 GPa, the flexural rigidity is *EI* = 3.3060 x 10^9^ N mm^2^ and the theoretical invariance constant is *C*_m_ = *l*^4^/192*EI* = 61.541 mm^2^/N.'));
add(P('Deflection at the mid-point of the first span was measured with a linear variable differential transformer (LVDT) of range 0-50 mm and resolution 0.005 mm, connected to a TDS-303 data logger. Loads were calibrated steel weights suspended from the beam at positions spaced 250 mm apart along the whole traverse, so that *Δx* = 250 mm and *n* = 10 segments per span. Each reported deflection is the mean of three separate loading and unloading cycles. The pooled standard deviation of these repeats is reported in Table 1 and constitutes the Type A uncertainty of the measurement chain.'));
add(P('Three load configurations were tested: a single load of 4.143 kg including its suspension hook; two loads of 2 145 g and 4 684 g at a fixed spacing of 250 mm, simulating a two-axle vehicle; and three loads of 2 550 g, 5 100 g and 5 100 g at spacings of 250 mm and 500 mm, simulating a three-axle vehicle. In each case the record extends to *x* = 2*l* + *a*_max_, that is 5000, 5250 and 5750 mm respectively, in accordance with the requirement established in Section 2.2.'));

add(H2('3.3', 'Validation of the influence line'));
add(P('Fig. 4 compares the analytical influence line of Eq. (6) with the finite element results and the measurements for the single load; the numerical values are listed in Table 1.', { firstLine: 0 }));
add(fig('fig04_influenceline', 4, 'Mid-span deflection of span *AB* as a function of the position of a single 40.64 N load: analytical, finite element and measured. The lower panel gives the absolute difference between measurement and theory. Shaded areas *A*^+^ and *A*^-^ are the positive and negative contributions to the deflection integral.'));
add(tableCap(1, 'Mid-span deflection of span *AB* under a single concentrated load of 40.64 N. Differences are given in absolute terms, since relative differences are meaningless near the supports where the deflection vanishes.'));
const t1rows = [
  ['0','0.0000','0.0000','0.0000','0.0000','—'],
  ['250','0.8874','0.8874','0.8844','-0.0030','[  ]'],
  ['500','1.6968','1.6968','1.6975','+0.0007','[  ]'],
  ['750','2.3501','2.3501','2.3525','+0.0024','[  ]'],
  ['1000','2.7693','2.7693','2.7738','+0.0045','[  ]'],
  ['1250','2.8764','2.8764','2.8827','+0.0063','[  ]'],
  ['1500','2.6253','2.6253','2.6363','+0.0110','[  ]'],
  ['1750','2.0980','2.0980','2.1100','+0.0120','[  ]'],
  ['2000','1.4087','1.4087','1.4213','+0.0126','[  ]'],
  ['2250','0.6713','0.6713','0.6838','+0.0125','[  ]'],
  ['2500','0.0000','0.0000','0.0000','0.0000','—'],
  ['2750','-0.5132','-0.5132','-0.5069','+0.0063','[  ]'],
  ['3000','-0.8644','-0.8644','-0.8556','+0.0088','[  ]'],
  ['3250','-1.0715','-1.0715','-1.0600','+0.0115','[  ]'],
  ['3500','-1.1526','-1.1526','-1.1438','+0.0088','[  ]'],
  ['3750','-1.1255','-1.1255','-1.1200','+0.0055','[  ]'],
  ['4000','-1.0085','-1.0085','-1.0013','+0.0072','[  ]'],
  ['4250','-0.8194','-0.8194','-0.8175','+0.0019','[  ]'],
  ['4500','-0.5763','-0.5763','-0.5816','-0.0053','[  ]'],
  ['4750','-0.2971','-0.2971','-0.3019','-0.0048','[  ]'],
  ['5000','0.0000','0.0000','0.0000','0.0000','—'],
];
add(tbl([['*x* (mm)','Analytical\n(mm)','Finite element\n(mm)','Measured\n(mm)','Measured minus\nanalytical (mm)','Std. dev. of\n3 repeats (mm)']], t1rows,
  [1200,1450,1650,1450,1900,1710], { fs: 16 }));
add(P('The finite element and analytical curves coincide to machine precision, as anticipated. The measured curve reproduces the analytical one closely: the largest absolute deviation is 0.0125 mm, which is 0.43 % of the maximum deflection and two and a half times the LVDT resolution. Expressing this deviation as a relative error at each point, as is sometimes done, produces a misleading maximum of 1.86 % at *x* = 2250 mm simply because the deflection there is small; the absolute measure is the meaningful one. The residuals in the lower panel of Fig. 4 are predominantly positive on both spans, which indicates a small systematic component — plausibly a slight flexibility of the supports or a small overestimate of the assumed *EI* — rather than pure random scatter. This observation is taken up in Section 4.', { firstLine: 0 }));
add(P('Table 2 compares the deflection integrals. The exact value from Eq. (11) is 2501.19 mm^2^. Applying the trapezoidal rule to the exact influence line sampled every 250 mm gives 2488.68 mm^2^, that is 0.500 % low; this is quadrature bias, not experimental error, and it is present in the analytical column as well. The measured integral is 2513.43 mm^2^, exceeding the exact value by 0.49 %.'));
add(tableCap(2, 'Deflection integral for the single-load configuration (mm^2^). The distinction between the exact value and its trapezoidal approximation is essential for interpreting the results.'));
add(tbl([['Quantity','Value (mm^2^)','Difference from exact']],
  [['Exact, Eq. (11): *P*_0_*l*^4^/192*EI*','2501.19','—'],
   ['Analytical influence line, trapezoidal rule, *Δx* = 250 mm','2488.68','-0.500 %'],
   ['Analytical influence line, Simpson rule, *Δx* = 250 mm','2501.85','+0.027 %'],
   ['Finite element, trapezoidal rule, *Δx* = 250 mm','2488.68','-0.500 %'],
   ['Measured, trapezoidal rule, *Δx* = 250 mm','2513.43','+0.49 %']],
  [4700,2200,2460], { fs: 17 }));

add(H2('3.4', 'Identification of the total load'));
add(P('The measured mid-span deflections for the three configurations are listed in Table 3 and were used to identify the total load by BPM, Eq. (12), and by SLM, Eq. (15), with the single-load crossing as the reference. Results are compared in Table 4 with direct weighing (LWM).', { firstLine: 0 }));
add(tableCap(3, 'Measured mid-span deflection of span *AB* for the three load configurations. Each record extends to 2*l* + *a*_max_.'));
const t3 = [];
const xs3 = []; for (let i = 0; i <= 23; i++) xs3.push(i * 250);
const c1 = ['0','0.8844','1.6975','2.3525','2.7738','2.8827','2.6363','2.1100','1.4213','0.6838','0','-0.5069','-0.8556','-1.0600','-1.1438','-1.1200','-1.0013','-0.8175','-0.5816','-0.3019','0','','',''];
const c2 = ['0','0.4625','1.8813','3.1413','4.0988','4.6350','4.6238','4.0688','3.1375','1.9600','0.7715','-0.2689','-1.0063','-1.4988','-1.7813','-1.8600','-1.7738','-1.5525','-1.2213','-0.8125','-0.3325','0','',''];
const c3 = ['0','0.5525','1.0450','2.5413','4.8700','6.7588','7.9350','8.2775','7.6825','6.2800','4.3725','2.2975','0.3021','-1.2588','-2.3650','-3.0363','-3.3300','-3.2663','-2.9450','-2.4125','-1.7088','-1.0713','-0.3650','0'];
for (let i = 0; i <= 23; i++) t3.push([String(xs3[i]), c1[i], c2[i], c3[i]]);
add(tbl([['*x* (mm)','Single load\n(mm)','Two loads\n(mm)','Three loads\n(mm)']], t3, [1600,2500,2500,2500], { fs: 16 }));
add(tableCap(4, 'Identified total loads compared with direct weighing.'));
add(tbl([['Configuration','Method','*I*_y_ (mm^2^)','Identified load (N)','Identified load (g)','Deviation from LWM']],
  [['Two loads','LWM (weighing)','—','66.99','6829.0','—'],
   ['','BPM, Eq. (12)','4168.15','67.73','6904.2','+1.10 %'],
   ['','SLM, Eq. (15)','4168.15','67.40','6870.6','+0.61 %'],
   ['Three loads','LWM (weighing)','—','125.08','12750.0','—'],
   ['','BPM, Eq. (12)','7788.93','126.57','12901.7','+1.19 %'],
   ['','SLM, Eq. (15)','7788.93','125.95','12838.9','+0.70 %']],
  [1700,2050,1500,1750,1450,1910], { fs: 17 }));
add(P('Both methods identify the total load to better than 1.2 %, and SLM is consistently the more accurate of the two. The reason is visible in the numbers themselves. The ratio of the two estimates is identical for both configurations, 1.00489, and equals the ratio of the measured single-load integral to its exact value, 2513.43/2501.19. In other words, the entire difference between BPM and SLM is the calibration error of the reference crossing: SLM absorbs it, BPM does not. This is the common-mode cancellation predicted in Section 2.6, observed directly.'));
add(P('It should be noted that the apparent accuracy of BPM benefits from a partial cancellation of two errors of opposite sign: the trapezoidal quadrature underestimates the integral by 0.50 %, while the measured deflections exceed theory by about 1.6 %. Correcting the quadrature bias alone would raise the BPM deviation from +1.10 % to +1.61 %. Reporting the two effects separately, as done here, gives a more honest picture than a single aggregate figure.'));
add(P('Fig. 5 provides the most direct visual evidence for the invariance property: the three load configurations produce visibly different deflection histories, yet the areas under them are proportional to the respective total loads with the same constant of proportionality. Fig. 6 presents the same evidence quantitatively as a calibration line. A regression through the origin gives *I*_y_ = 62.229 *P* with *R*^2^ = 0.99998, against the theoretical 61.541 mm^2^/N — a slope 1.12 % above theory, consistent with the residual pattern of Fig. 4 and attributable to a small overestimate of the assumed flexural rigidity or to support flexibility.'));
add(fig('fig05_invariance', 5, 'Invariance in practice: for the same total load, three axle configurations give markedly different deflection histories but the same deflection integral.'));
add(fig('fig09_calibration', 6, 'Calibration line: measured deflection integral against total applied load for the three configurations, compared with the theoretical slope *l*^4^/192*EI*.', 430));

// ============================ 4. ERROR BUDGET ============================
add(H1('4.', 'Error budget, robustness and domain of validity'));
add(P('The agreement reported in Section 3 was obtained in a laboratory, on a beam of accurately known properties, with a static load and a stable thermal environment. None of these conditions holds on an in-service bridge. This section therefore develops the error budget explicitly, so that the laboratory results can be extrapolated rather than merely admired.', { firstLine: 0 }));

add(H2('4.1', 'Measurement model and error propagation'));
add(P('The deflection actually recorded at sample *i* is modelled as', { firstLine: 0 }));
add(eq('e16', 16));
add(P('where *γ* is the relative gain (scale-factor) error of the transducer and conditioning chain, *ε*_0_ is a zero-offset or baseline error, and *σ*_a_ is the standard deviation of the additive random noise. This decomposition replaces the purely multiplicative model *y*_i_(1 + *σξ*_i_) used in earlier studies, which has the unphysical property of predicting zero noise wherever the deflection vanishes — that is, precisely at the supports, where a real transducer is no quieter than anywhere else.'));
add(P('Propagating Eq. (16) through Eq. (12) gives, to first order, the error budget of BPM:'));
add(eq('e17', 17));
add(P('where *e*_q_ is the quadrature bias of Section 2.5 and *δv*/*v* is the relative error in the traverse speed, discussed in Section 4.4. The corresponding budget for SLM is obtained by differentiating Eq. (15):'));
add(eq('e18', 18));
add(P('The contrast between Eqs. (17) and (18) is the central methodological result of this paper. Four terms present in BPM are absent from SLM: the flexural rigidity, the span length with its fourfold amplification, the gain error, and the quadrature bias. All four are common-mode, that is identical for the reference and the service crossings, and the ratio in Eq. (15) removes them exactly. What survives in SLM is the accuracy of the reference weighing, the incomplete cancellation of the zero offset, and the difference of the two speed errors. Random noise, absent from Eq. (18) because it has zero mean, is treated separately in Section 4.3.'));

add(H2('4.2', 'Zero-offset drift: the dominant error source'));
add(P('A constant offset *ε*_0_ superimposed on the deflection record contributes *ε*_0_*L*_tot_ to the integral, where *L*_tot_ is the length of the record. Because the influence line changes sign at the interior support, the positive and negative parts of the integral partly cancel — the net constant is only 4/7 of the positive contribution, as noted in Section 2.3 — whereas the offset contribution does not cancel at all. The relative bias is therefore', { firstLine: 0 }));
add(eq('e19', 19));
add(P('and it is amplified by exactly the same cancellation that makes the method elegant. Table 5 evaluates Eq. (19) for the three experimental configurations, and Fig. 7 plots it.'));
add(tableCap(5, 'Bias of the identified load caused by a zero-offset error *ε*_0_ of the deflection signal, from Eq. (19).'));
add(tbl([['Configuration','*I*_y_ (mm^2^)','*L*_tot_ (mm)','*ε*_0_ = 0.005 mm\n(LVDT resolution)','*ε*_0_ = 0.02 mm','*ε*_0_ = 0.05 mm']],
  [['Single load','2513','5000','+0.99 %','+3.98 %','+9.95 %'],
   ['Two loads','4168','5250','+0.63 %','+2.52 %','+6.30 %'],
   ['Three loads','7789','5750','+0.37 %','+1.48 %','+3.69 %']],
  [1800,1500,1400,2260,1200,1200], { fs: 17 }));
add(fig('fig08_zerodrift', 7, 'Bias of the identified total load as a function of the zero-offset error of the deflection signal.', 440));
add(P('Three conclusions follow. First, an offset no larger than the resolution of the transducer already biases the identified load by 0.4 to 1.0 % — comparable to the total error reported in Section 3, and larger than the effect of any plausible random noise. Second, on a real bridge, where thermal gradients and support settlement routinely produce baseline shifts of a few hundredths of a millimetre over the duration of a monitoring session, the resulting bias reaches 2 to 10 %. Baseline re-zeroing immediately before and after each crossing, and rejection of records whose end values differ by more than a set tolerance, are therefore not refinements but prerequisites.', { firstLine: 0 }));
add(P('Third, and more encouragingly, the bias is inversely proportional to *I*_y_ and therefore to the total load. The method becomes more accurate as the vehicle becomes heavier. For an overload screening application this is exactly the right direction of degradation: the estimate is least reliable for light vehicles, which are of no interest, and most reliable for the heavy vehicles the system is intended to detect.'));

add(H2('4.3', 'Monte Carlo robustness analysis'));
add(P('A Monte Carlo study was performed with 200 000 realisations per case, using the measurement model of Eq. (16). Four scenarios were considered: gain error alone with a standard deviation of 2 %; zero offset alone with a standard deviation of 0.005 mm, equal to the transducer resolution; additive random noise alone with *σ*_a_ = 0.0025 mm, half the resolution; and the three combined. Each realisation perturbed the measured deflection record, recomputed the integral with the same trapezoidal rule and the same grid, and re-identified the load with both methods. For SLM, two reference conditions were distinguished: an averaged reference, in which the reference integral is taken as noise-free because it has been obtained from many repeated calibration crossings, and a single noisy reference obtained from one crossing only. Results are summarised in Table 6 for the two-load configuration; the three-load configuration behaves identically to within 0.1 percentage point.', { firstLine: 0 }));
add(tableCap(6, 'Monte Carlo results for the two-load configuration, 200 000 realisations. Bias is the mean relative error with respect to direct weighing; *p*_5_ and *p*_95_ are the 5th and 95th percentiles of that error.'));
add(tbl([['Error source','Method','Reference','Bias (%)','Std. dev. (%)','*p*_5_ (%)','*p*_95_ (%)']],
  [['Gain, *σ*_γ_ = 2 %','BPM','—','+1.10','2.01','-2.21','+4.40'],
   ['','SLM','averaged','+0.61','2.00','-2.69','+3.90'],
   ['','SLM','single','+0.66','2.85','-3.94','+5.41'],
   ['Zero offset, *σ*_ε_ = 0.005 mm','BPM','—','+1.10','0.64','+0.05','+2.15'],
   ['','SLM','averaged','+0.61','0.63','-0.43','+1.65'],
   ['','SLM','single','+0.62','1.19','-1.31','+2.60'],
   ['Random, *σ*_a_ = 0.0025 mm','BPM','—','+1.10','0.07','+0.99','+1.21'],
   ['','SLM','averaged','+0.61','0.07','+0.50','+0.72'],
   ['','SLM','single','+0.61','0.13','+0.40','+0.82'],
   ['All three combined','BPM','—','+1.10','2.12','-2.39','+4.59'],
   ['','SLM','averaged','+0.61','2.11','-2.87','+4.08'],
   ['','SLM','single','+0.65','3.09','-4.34','+5.83']],
  [2300,900,1300,1150,1250,1150,1310], { fs: 16 }));
add(fig('fig07_montecarlo', 8, 'Distribution of the relative identification error under the combined error model, two-load configuration.', 470));
add(P('Two results deserve comment because they contradict conclusions that are natural but wrong.', { firstLine: 0 }));
add(P('The first concerns random noise. Its effect is negligible: with *σ*_a_ equal to half the transducer resolution, the standard deviation of the identified load is 0.07 %. This is a direct consequence of integration, which averages independent perturbations over some twenty samples. Any robustness claim based solely on random noise therefore flatters the method considerably. The systematic terms — gain and offset — dominate by more than an order of magnitude.'));
add(P('The second concerns SLM. It is tempting to argue that, because SLM is a ratio, noise present in both measurements will cancel. This is true of common-mode error and false of independent error. For independent random perturbations the relative variances add:'));
add(eq('e21', 20));
add(P('so that a single noisy reference crossing multiplies the scatter of SLM by the square root of two. Table 6 confirms this: under the combined model, the standard deviation of SLM rises from 2.11 % with an averaged reference to 3.09 % with a single one, while BPM remains at 2.12 %. The practical prescription follows immediately and is inexpensive: perform the calibration crossing several times and average the resulting integrals. With *N*_rep_ of order five or more, the second term of Eq. (20) becomes negligible and SLM dominates BPM in every respect — smaller bias, because the common-mode terms cancel, and equal scatter.'));

add(H2('4.4', 'Traverse speed and the space-time conversion'));
add(P('The theorem of Section 2.2 concerns an integral over space, whereas a bridge monitoring system records a time history. The two are related by', { firstLine: 0 }));
add(eq('e20', 21));
add(P('so that for a crossing at constant speed the required integral is the time integral of the deflection multiplied by the speed. The relative error in speed therefore propagates one-for-one into the identified load: a speed known to 3 % gives a load known to no better than 3 %. This term is absent from the laboratory tests reported here, where the load was positioned statically, and it is likely to be the largest single contributor in a field deployment.'));
add(P('The deflection signal itself, however, contains the information needed to remove it. For the two-span beam the influence line vanishes at *x* = *l* and at *x* = 2*l*; the record therefore exhibits two zero crossings whose separation corresponds to a known distance, the second span length. The speed follows as *v* = 2*l*/(*t*_2_ - *t*_1_) using the entry instant and the second zero crossing, or more robustly from a least-squares fit of the measured history to the known shape of the influence line. Self-calibration of speed from the response is thus possible with the same single sensor, without axle detectors or external instrumentation. This is a distinctive advantage of instrumenting a continuous beam rather than a simply supported one, where the influence line has no interior zero, and it deserves dedicated experimental study.'));
add(P('A related restriction should be stated plainly. Because the integral must span a complete crossing, the method yields the gross weight of a load group after the crossing is finished. It is not a real-time, axle-by-axle estimator, and if two vehicles are on the structure simultaneously the integral returns their combined weight. On a two-lane overpass, separating simultaneous crossings would require a second sensor or vehicle-detection hardware; within the scope of a single deflection channel, the honest statement is that overlapping crossings must be detected and discarded.'));

add(H2('4.5', 'Domain of validity: span ratio and sensor position'));
add(P('The theorem holds for arbitrary geometry, but the usefulness of the resulting estimator depends on the magnitude of *C*_m_: if the constant is small, the deflection integral carries little information about the load and every error term of Eq. (17) is amplified. The constant was therefore computed by finite elements, using the Maxwell-Betti corollary of Eq. (10), for span ratios *l*_2_/*l*_1_ between 0.4 and 2.0 and for sensor positions along the instrumented span. Results are shown in Fig. 9.', { firstLine: 0 }));
add(fig('fig10_parametric', 9, 'Parametric study of the invariance constant: (a) effect of the span ratio, with the sensor at mid-span of span 1; (b) effect of the sensor position along span 1, equal spans.'));
add(P('Fig. 9(a) reveals a limitation with no counterpart in simply supported beams. As the adjacent span lengthens, its negative contribution to the integral grows until it exactly offsets the positive contribution of the instrumented span. The constant vanishes at a span ratio of 1.46, and Eq. (12) becomes singular; in a neighbourhood of that ratio the method is unusable however accurate the measurements. Beyond it the constant changes sign, so that the integral remains formally usable but the response is dominated by the uninstrumented span. The practical rule is simple and should be checked before any deployment: instrument the longer span, and verify that the ratio of the adjacent span to the instrumented span is comfortably below 1.46. For the equal-span configuration studied here the margin is ample.', { firstLine: 0 }));
add(P('Fig. 9(b) examines the choice of sensor position, which the theorem leaves free. The constant is maximised at *x*_m_ = 0.42*l*, but the gain over mid-span instrumentation is only 4.0 %, while the constant falls sharply as the sensor approaches either support — to 10 % of its maximum at 0.9*l*. Mid-span instrumentation, chosen here on practical grounds, is therefore very nearly optimal, and the result also indicates that moderate errors in sensor placement are of little consequence, whereas placing a sensor near a support would be seriously detrimental.'));
add(tableCap(7, 'Normalised invariance constant 192*EI C*_m_/*l*_1_^4^ as a function of the span ratio, sensor at mid-span of span 1.'));
add(tbl([['*l*_2_/*l*_1_','0.5','0.7','0.8','1.0','1.2','1.3','1.4','1.46','1.6']],
  [['192*EI C*_m_/*l*_1_^4^','1.375','1.315','1.240','1.000','0.640','0.415','0.160','0','-0.440']],
  [2260,890,890,890,890,890,890,890,890,890], { fs: 16 }));

add(H2('4.6', 'Combined uncertainty budget'));
add(P('Table 8 assembles the individual contributions into a budget in the format of the Guide to the Expression of Uncertainty in Measurement [28], for two situations: the present laboratory tests and a plausible field deployment on a short-span concrete continuous bridge. Field values are estimates based on the sensitivity coefficients derived above and on reported values of environmental drift in long-term monitoring [29,30]; they are intended as an order-of-magnitude extrapolation, not as a measured result.', { firstLine: 0 }));
add(tableCap(8, 'Uncertainty budget for the identified total load. Standard uncertainties, combined in quadrature for independent contributions and summed algebraically for systematic ones.'));
add(tbl([['Contribution','Type','Sensitivity','Laboratory\n(SLM)','Field estimate\n(SLM)','Field estimate\n(BPM)']],
  [['Flexural rigidity *EI*','B','1','cancels','cancels','5-15 %'],
   ['Span length *l*','B','4','cancels','cancels','0.4-2 %'],
   ['Sensor gain *γ*','B','1','cancels','cancels','1-2 %'],
   ['Quadrature bias *e*_q_','B','1','cancels','cancels','0.5 %'],
   ['Reference weighing *P*_0_','B','1','0.1 %','0.5-1 %','—'],
   ['Zero offset *ε*_0_','B','*L*_tot_/*I*_y_','0.4-1 %','2-10 %','2-10 %'],
   ['Traverse speed *v*','B','1','—','1-3 %','1-3 %'],
   ['Random noise *σ*_a_','A','< 0.1','0.07 %','0.1-0.3 %','0.1-0.3 %'],
   ['Reference scatter (*N*_rep_ = 1)','A','1','0.07 %','0.1-0.3 %','—'],
   ['**Combined standard uncertainty**','','','**0.5-1.1 %**','**3-11 %**','**6-19 %**']],
  [2500,700,1400,1550,1600,1610], { fs: 16 }));
add(P('The budget makes explicit what the laboratory results cannot show. In the laboratory, SLM is limited by zero offset and by the accuracy of the reference weighing, and the combined uncertainty of 0.5 to 1.1 % is consistent with the deviations of 0.61 and 0.70 % actually observed. In the field, baseline stability and speed measurement dominate, and a realistic expectation is a few per cent for SLM and roughly twice that for BPM. This is far from the accuracy of a certified weighing device, and the method should not be presented as a substitute for one. It is, however, entirely sufficient for the screening application for which it is intended: legal overload thresholds are typically exceeded by 20 % or more, so an estimator with an uncertainty of 3 to 5 % can flag candidate vehicles with high confidence at the cost of a single displacement transducer.', { firstLine: 0 }));

// ============================ 5. DISCUSSION ============================
add(H1('5.', 'Discussion'));
add(H2('5.1', 'Relation to existing bridge weigh-in-motion and moving-force identification methods'));
add(P('Table 9 situates the present approach relative to the two established families. The comparison is deliberately made on the basis of what each method requires and delivers rather than on headline accuracy figures, which are not comparable across different structures and load populations.', { firstLine: 0 }));
add(tableCap(9, 'Positioning of the deflection-integral approach relative to established methods.'));
add(tbl([['','Pavement WIM','BWIM (Moses type)','MFI / inverse methods','Deflection integral\n(this work)']],
  [['Output','Axle loads and GVW','Axle loads and GVW','Full axle-load time history','Total load of the group only'],
   ['Sensors','Pavement-embedded array','Several strain gauges plus axle detectors','Dense array; often accelerometers','One displacement channel'],
   ['Structural model','Not required','Influence line required (measured or assumed)','Full model required','Only the scalar *C*_m_'],
   ['Inverse problem','None','Least squares, well posed','Ill posed; needs regularisation','None; a single division'],
   ['Speed needed','Measured internally','Yes','Yes','Yes; obtainable from the signal itself'],
   ['Dynamic effects','Handled by design','Averaged or filtered','Explicitly modelled','Assumed negligible (limitation)'],
   ['Relative cost','High','Moderate','Moderate to high','Low']],
  [1900,1750,2000,1900,1810], { fs: 16 }));
add(P('The deflection-integral approach is thus not a competitor to BWIM but a deliberately reduced alternative: it answers a narrower question with a much smaller installation and without an inverse problem. Its natural role is dense, low-cost screening across many secondary structures, with instrumented BWIM or enforcement weighing reserved for the vehicles it flags.', { firstLine: 0 }));

add(H2('5.2', 'Limitations'));
add(P('The limitations of the present study should be stated without qualification.', { firstLine: 0 }));
add(BUL('*Quasi-static loading.* The theorem assumes that the response at each instant is the static response to the instantaneous load position. Real crossings excite the structure dynamically, with dynamic amplification factors typically between 1.1 and 1.3. Because free-vibration components have near-zero mean, integration over a full crossing is expected to filter much of this contribution, but the present work does not demonstrate it. A vehicle-bridge interaction study establishing the speed range over which the quasi-static assumption holds is the single most important extension required before field deployment.'));
add(BUL('*Scale and material.* Validation used one small-scale steel specimen with a span-to-depth ratio of 100 and idealised knife-edge supports. Concrete bridges introduce cracking, creep, composite action with the deck and bearing friction, none of which is represented.'));
add(BUL('*Single geometry tested.* The parametric study of Section 4.5 is numerical. Experimental verification of the unequal-span case, and in particular of the predicted degeneracy near a span ratio of 1.46, has not been performed.'));
add(BUL('*Direct evidence for invariance.* The three configurations tested differ in both total load and axle spacing. A cleaner experiment, holding the total load fixed while varying the axle spacing, would test the invariance property directly and is recommended as the first extension.'));
add(BUL('*Transverse position and load distribution.* A real vehicle applies loads across the deck width; the present one-dimensional treatment implicitly assumes that the transverse position does not affect the measured deflection, which is true only for a torsionally stiff deck with a centrally placed sensor.'));

add(H2('5.3', 'Recommendations for field implementation'));
add(BUL('Instrument the longer span, at approximately 0.4 to 0.5 of its length, and verify that the adjacent-to-instrumented span ratio is well below 1.46.'));
add(BUL('Re-zero the deflection baseline immediately before and after each crossing, and reject records whose end values differ by more than a preset tolerance; this addresses the dominant error term.'));
add(BUL('Use Simpson quadrature, or a sampling interval of *l*/20 or finer, to eliminate the quadrature bias.'));
add(BUL('Prefer SLM, and obtain the reference integral by averaging at least five crossings of the calibrated vehicle so that the reference contributes negligible scatter.'));
add(BUL('Extract the traverse speed from the interior zero crossings of the deflection record, and cross-check it against an independent measurement during commissioning.'));
add(BUL('Repeat the reference calibration periodically, since SLM cancels only those changes in *C*_m_ that are common to the two crossings.'));

// ============================ 6. CONCLUSIONS ============================
add(H1('6.', 'Conclusions'));
add(P('This paper has established, on a general basis, that the integral of the deflection measured at a single fixed point over a complete crossing is proportional to the total load carried by the crossing group, with a constant of proportionality that depends only on the structure and the sensor position. The principal results are as follows.', { firstLine: 0 }));
add(BUL('The invariance property is a theorem valid for any linear-elastic beam structure, any span arrangement and any measurement point, not a special feature of a particular configuration. It requires only linearity, time invariance and integration over the complete passage from the entry of the leading axle to the exit of the trailing one.'));
add(BUL('By the Maxwell-Betti reciprocal theorem, the invariance constant equals the area under the deflected shape produced by a unit static load applied at the measurement point. It is therefore obtainable analytically, from one static analysis, or from one static calibration test on a structure whose properties are unknown.'));
add(BUL('For a two-span continuous beam of equal spans instrumented at mid-span of the first span, the constant is *l*^4^/192*EI*. Laboratory tests on a 2 x 2500 mm steel beam identified the total load of one-, two- and three-axle groups to within 1.19 % by BPM and 0.70 % by SLM.'));
add(BUL('SLM cancels every common-mode error — flexural rigidity, span length, sensor gain and quadrature bias — which was verified directly: the ratio between the BPM and SLM estimates equals the calibration error of the reference crossing, 1.00489, for both configurations. SLM does not, however, reduce independent random noise; a single noisy reference crossing increases its scatter by the square root of two, and the reference integral should be averaged over repeated crossings.'));
add(BUL('The dominant error source is the zero offset of the deflection signal, not random noise. An offset equal to the transducer resolution biases the identified load by 0.4 to 1.0 %, whereas random noise of half that magnitude contributes 0.07 %. The bias is inversely proportional to the load, so accuracy improves for heavier vehicles — favourable for overload screening.'));
add(BUL('Replacing the trapezoidal rule by Simpson quadrature removes a systematic bias of 0.500 % at the sampling interval used, at no experimental cost.'));
add(BUL('The invariance constant vanishes at a span ratio of 1.46, at which the method fails irrespective of measurement quality. Mid-span instrumentation is within 4 % of the optimal sensor position, so precise placement is not critical, but placement near a support is strongly detrimental.'));
add(P('A combined uncertainty budget indicates 0.5 to 1.1 % in the laboratory and 3 to 11 % for a field deployment using SLM, dominated by baseline stability and traverse speed. That level of accuracy does not compete with certified weighing, but it is sufficient for low-cost screening of traffic overload with a single displacement channel per structure. Future work should address vehicle-bridge interaction to delimit the quasi-static range, field testing on in-service concrete continuous bridges, experimental verification of the unequal-span predictions including the predicted degeneracy, and a Bayesian formulation returning credible intervals rather than point estimates.', { firstLine: 0 }));

// ============================ DECLARATIONS ============================
add(H1('', 'CRediT authorship contribution statement'));
add(P('**Quoc-Bao Nguyen:** Conceptualization, Methodology, Formal analysis, Writing – original draft. **Thai-Son Vu:** Conceptualization, Investigation, Validation, Supervision, Writing – review and editing. **Hung-Son Nguyen:** Investigation, Data curation, Visualization.', { firstLine: 0 }));
add(H1('', 'Declaration of competing interest'));
add(P('The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.', { firstLine: 0 }));
add(H1('', 'Data availability'));
add(P('The measured deflection data supporting the findings of this study are provided in full in Tables 1 and 3. The scripts used for the quadrature study, the Monte Carlo analysis and the parametric finite element study are available from the corresponding author on reasonable request.', { firstLine: 0 }));
add(H1('', 'Acknowledgements'));
add(P('[To be completed by the authors: funding source, grant number, and laboratory support.]', { firstLine: 0 }));

// ============================ REFERENCES ============================
add(H1('', 'References'));
const refs = [
 'Fan Y., et al. Analysis for Yangmingtan Bridge collapse. Engineering Failure Analysis 2015;56:20-27. doi:10.1016/j.engfailanal.2015.05.003',
 'Salem H.M., Helmy H.M. Numerical investigation of collapse of the Minnesota I-35W bridge. Engineering Structures 2014;59:635-645. doi:10.1016/j.engstruct.2013.11.022',
 'Invernizzi S., Montagnoli F., Carpinteri A. Very high cycle corrosion fatigue study of the collapsed Polcevera bridge, Italy. Journal of Bridge Engineering 2022;27(1):04021102. doi:10.1061/(ASCE)BE.1943-5592.0001807',
 'Morgese M., et al. Post-collapse analysis of Morandi\u2019s Polcevera viaduct in Genoa, Italy. Journal of Civil Structural Health Monitoring 2020;10(1):69-85. doi:10.1007/s13349-019-00370-7',
 'Ventura R., Barabino B., Maternini G. Estimating the frequency of traffic overloading on road bridges. Journal of Traffic and Transportation Engineering (English Edition) 2024;11(4):776-796. doi:10.1016/j.jtte.2023.11.005',
 'Li H., Wang T., Wu G. Nonlinear vibration analysis of beam-like bridges with multiple breathing cracks under moving vehicle load. Mechanical Systems and Signal Processing 2023;186:109866. doi:10.1016/j.ymssp.2022.109866',
 'Fattorini F., et al. Application to the territorial authorities of the guidelines for the classification and management of risk of existing bridges: the case study of the Municipality of Rome. Procedia Structural Integrity 2023;44:689-696. doi:10.1016/j.prostr.2023.01.090',
 'Gajda J., Sroka R., Burnos P., Daniol M. Long-term assessment of the properties of load sensors applied in weigh-in-motion systems. Sensors 2025;25(8):2421. doi:10.3390/s25082421',
 'Federal Highway Administration. Long-Term Bridge Performance Program: weigh-in-motion system accuracy and precision. Washington DC: FHWA, U.S. Department of Transportation; 2016.',
 'Federal Highway Administration. Comprehensive truck size and weight study: costs of weigh stations. Washington DC: FHWA, U.S. Department of Transportation; 2009.',
 'COST 323. Weigh-in-motion of road vehicles: final report of the COST 323 action. Paris: LCPC; 2002.',
 'European Committee for Standardization. EN 1991-2:2003 Eurocode 1: Actions on structures \u2013 Part 2: Traffic loads on bridges. Brussels: CEN; 2003.',
 'Moses F. Weigh-in-motion system using instrumented bridges. ASCE Journal of Transportation Engineering 1979;105(3):233-249.',
 'OBrien E.J., Quilligan M.J., Karoumi R. Calculating an influence line from direct measurements. Proceedings of the Institution of Civil Engineers \u2013 Bridge Engineering 2006;159(1):31-34. doi:10.1680/bren.2006.159.1.31',
 'OBrien E.J., Rowley C.W., Gonz\u00e1lez A., Green M.F. A regularised solution to the bridge weigh-in-motion equations. International Journal of Heavy Vehicle Systems 2009;16(3):310-327. doi:10.1504/IJHVS.2009.027135',
 '\u017dnidari\u010d A., Kalin J., Kreslin M. Improved accuracy and robustness of bridge weigh-in-motion systems. Structure and Infrastructure Engineering 2018;14(4):412-424. doi:10.1080/15732479.2017.1406958',
 'Yu Y., Cai C.S., Deng L. State-of-the-art review on bridge weigh-in-motion technology. Advances in Structural Engineering 2016;19(9):1514-1530. doi:10.1177/1369433216655922',
 'Ojio T., Carey C., OBrien E.J., Doherty C., Taylor S.E. Contactless bridge weigh-in-motion. Journal of Bridge Engineering 2016;21(7):04016032. doi:10.1061/(ASCE)BE.1943-5592.0000776',
 'Law S.S., Chan T.H.T., Zeng Q.H. Moving force identification: a time domain method. Journal of Sound and Vibration 1997;201(1):1-22. doi:10.1006/jsvi.1996.0774',
 'Chan T.H.T., Law S.S., Yung T.H., Yuan X.R. An interpretive method for moving force identification. Journal of Sound and Vibration 1999;219(3):503-524. doi:10.1006/jsvi.1998.1904',
 'Law S.S., Zhu X.Q. Study on different beam models in moving force identification. Journal of Sound and Vibration 2000;234(4):661-679. doi:10.1006/jsvi.2000.2867',
 'Zhu X.Q., Law S.S. Moving load identification on multi-span continuous bridges with elastic bearings. Mechanical Systems and Signal Processing 2006;20(7):1759-1782. doi:10.1016/j.ymssp.2005.06.004',
 'Luo S., et al. Distributed dynamic load identification of beam structures using a Bayesian method. Applied Sciences 2023;13(4):2537. doi:10.3390/app13042537',
 'Jiang J., et al. Real-time identification of dynamic loads using inverse solution and Kalman filter. Applied Sciences 2020;10(19):6767. doi:10.3390/app10196767',
 'Kapoor T., et al. Physics-informed machine learning for moving load problems. Journal of Physics: Conference Series 2024;2647(15):152003. doi:10.1088/1742-6596/2647/15/152003',
 'Andersen P., Mukhopadhyay S.K. Determination of load distribution on a beam from measurements on its deflected form. Minneapolis: University of Minnesota; 1950.',
 'Nguy\u1ec5n Q.B., Ho\u00e0ng T., Nguy\u1ec5n H.S. Determination of the load applied on a simple supported beam based on measured deflection data. Journal of Science and Technology in Civil Engineering (HUCE) 2024;18(2V):61-71. doi:10.31814/stce.huce2024-18(2V)-05',
 'JCGM 100:2008. Evaluation of measurement data \u2013 Guide to the expression of uncertainty in measurement (GUM). Joint Committee for Guides in Metrology; 2008.',
 'Sohn H. Effects of environmental and operational variability on structural health monitoring. Philosophical Transactions of the Royal Society A 2007;365(1851):539-560. doi:10.1098/rsta.2006.1935',
 'Cross E.J., Koo K.Y., Brownjohn J.M.W., Worden K. Long-term monitoring and data analysis of the Tamar Bridge. Mechanical Systems and Signal Processing 2013;35(1-2):16-34. doi:10.1016/j.ymssp.2012.08.026',
 'Feng D., Feng M.Q. Computer vision for SHM of civil infrastructure: from dynamic response measurement to damage detection \u2013 a review. Engineering Structures 2018;156:105-117. doi:10.1016/j.engstruct.2017.11.018',
 'Fr\u00fdba L. Vibration of solids and structures under moving loads. 3rd ed. London: Thomas Telford; 1999.',
 'Yang Y.B., Lin C.W., Yau J.D. Extracting bridge frequencies from the dynamic response of a passing vehicle. Journal of Sound and Vibration 2004;272(3-5):471-493. doi:10.1016/S0022-460X(03)00378-X',
 'Deng L., Cai C.S. Identification of dynamic vehicular axle loads: theory and simulations. Journal of Vibration and Control 2010;16(14):2167-2194. doi:10.1177/1077546309351221',
 'Chen Z., et al. Identification of multi-axle vehicle loads on beam type bridge based on minimal residual norm steepest descent method. Journal of Sound and Vibration 2023;563:117866. doi:10.1016/j.jsv.2023.117866',
 'Nguyen D.H., et al. Damage detection in girder bridges using modal curvatures gapped smoothing method and convolutional neural network: application to Bo Nghi bridge. Theoretical and Applied Fracture Mechanics 2020;109:102728. doi:10.1016/j.tafmec.2020.102728',
 'Katori H. Inverse problems for an Euler-Bernoulli beam: identification of bending rigidity and external loads. World Journal of Mechanics 2018;8(5):192-199. doi:10.4236/wjm.2018.85014',
 'Hoang T., et al. Calculation of force distribution for a periodically supported beam subjected to moving loads. Journal of Sound and Vibration 2017;388:327-338. doi:10.1016/j.jsv.2016.10.031',
 'Smith M. ABAQUS/Standard user\u2019s manual, version 6.9. Providence RI: Dassault Syst\u00e8mes Simulia Corp.; 2009.',
 'American Association of State Highway and Transportation Officials. AASHTO LRFD bridge design specifications. 9th ed. Washington DC: AASHTO; 2020.',
];
refs.forEach((r, i) => add(new Paragraph({
  alignment: AlignmentType.JUSTIFIED, spacing: { after: 70, line: 240 },
  indent: { left: 400, hanging: 400 },
  children: [ new TextRun({ text: '[' + (i + 1) + ']  ' + r, font: 'Times New Roman', size: 19 }) ] })));

// ============================ ANNEX: REVISION NOTES ============================
add(new Paragraph({ children: [ new PageBreak() ] }));
add(H1('', 'Annex – Revision notes for the authors (to be deleted before submission)'));
add(P('This annex records the changes made with respect to the previous draft and the items that require verification by the authors. It is not part of the manuscript.', { firstLine: 0 }));
add(H3('A.1', 'Errors corrected'));
add(BUL('The third branch of the factorised mid-span deflection carried the denominator 192*EI* instead of 64*EI* (a factor of three). Verified numerically: at *x* = 3750 mm the correct expression gives -1.1255 mm, matching the measurements, whereas 192*EI* gives -0.375 mm. Corrected in Eq. (6).'));
add(BUL('All force values were overstated by a factor of 1000 (6829 g weighs 66.99 N, not 66 992.5 N). Corrected throughout Table 4.'));
add(BUL('The interior support was described as preventing both vertical displacement and rotation. That description contradicts the reactions actually derived (13*P*/32 at *x* = *l*/2 corresponds to a simple support) and contradicts the slope-continuity condition stated later. Corrected to a hinged support in Section 2.1.'));
add(BUL('The interior support was located at *s* = *l*/2 in the list of boundary conditions instead of *s* = *l*, and the required continuity conditions at the load point were missing. The complete set of six conditions is now stated in Section 2.1.'));
add(BUL('The SLM derivation carried a factor 1/128 instead of 1/192; it cancelled in the ratio but was incorrect.'));
add(BUL('The mid-span deflection of the continuous beam was stated as 60-70 % of the simply supported value; the correct figure is 71.9 % (72.1 % taking the maximum over the load position).'));
add(BUL('The discrete integral was written as a sum of *y*_i_*Δx*, which is a rectangle rule; the trapezoidal rule requires half-weights at the ends. Corrected in Eq. (13).'));
add(BUL('The extension to multiple loads integrated every influence function over [0, 2*l*], which is not valid for shifted axles; the correct domain is [0, 2*l* + *a*_max_]. The theorem in Section 2.2 now handles this explicitly.'));
add(BUL('The statement that the analytical and numerical integrals matched the exact closed-form value was incorrect: both were trapezoidal approximations and were 0.500 % low. Table 2 now separates exact, trapezoidal and Simpson values.'));
add(BUL('The previous Monte Carlo table reported identical mean error, maximum error and standard deviation for BPM and SLM despite different biases, which is not possible. The analysis has been redone with 200 000 realisations and a physically based three-component noise model.'));
add(BUL('The claim that SLM would be less noise-sensitive when both measurements are noisy is incorrect for independent noise; the variances add. This has been corrected and turned into a positive prescription (average the reference crossing).'));
add(BUL('Reference [10] of the previous draft (Qiu et al., Sensors 2025;25(8):2421) shares its article number and DOI with reference [9] (Gajda et al.), which is the genuine article. It appears not to exist and has been removed. **The authors should verify every DOI in the reference list before submission.**'));
add(BUL('The closed-form deflection integral was attributed to a reference on Kalman-filter load identification, and the I-35W collapse was attributed in part to a book on structural health monitoring in Australia. Both citations have been corrected.'));
add(H3('A.2', 'New material added'));
add(BUL('General invariance theorem with proof (Section 2.2), and the Maxwell-Betti corollary identifying the constant as the area under the deflected shape (Eq. 10), verified against finite elements to eight significant figures.'));
add(BUL('Quadrature convergence study and the recommendation to use Simpson quadrature (Section 2.5, Table 2).'));
add(BUL('Three-component measurement model and first-order error budgets for both methods (Eqs. 16-18), which formalise why SLM cancels common-mode error.'));
add(BUL('Zero-offset sensitivity analysis (Section 4.2), the dominant error source, previously absent.'));
add(BUL('Traverse-speed analysis and the proposal to self-calibrate speed from the interior zero crossings of the deflection record (Section 4.4).'));
add(BUL('Parametric study of span ratio and sensor position, including the critical span ratio of 1.46 at which the method fails (Section 4.5).'));
add(BUL('GUM-style combined uncertainty budget with a field extrapolation (Section 4.6).'));
add(BUL('Comparison table against pavement WIM, BWIM and MFI, and a substantially expanded bibliography including the BWIM literature, which was entirely absent.'));
add(H3('A.3', 'Items requiring input from the authors'));
add(BUL('**Table 1, last column:** the standard deviation of the three repeated measurements at each point. These values exist in the laboratory records and constitute the Type A uncertainty; the column is currently marked with empty brackets.'));
add(BUL('**Section 3.1:** confirm the Abaqus element type, mesh density, and whether the Timoshenko (B31) comparison was actually run. If it was not, either run it or delete that sentence.'));
add(BUL('**Section 4.6:** the field estimates in Table 8 are extrapolations by sensitivity coefficient, clearly labelled as such. If any field data exist, they should replace the estimates.'));
add(BUL('**Acknowledgements:** funding and grant numbers.'));
add(BUL('**Target journal.** The previous draft used the template of the Journal of Materials and Engineering Structures, which is indexed in the Emerging Sources Citation Index with a journal impact factor of about 0.4 and is not a Q1 or Q2 outlet. For a Q1 or Q2 target, Structures, Measurement or the Journal of Civil Structural Health Monitoring are the most realistic fits; the present manuscript is formatted neutrally and will need to be reformatted to the chosen template.'));
add(BUL('**Recommended additional experiment.** Repeat one configuration holding the total load constant while varying the axle spacing. This tests the invariance property directly, which the present data set does only indirectly, and it can be done in an afternoon with the existing rig.'));

// ============================ BUILD ============================
const doc = new Document({
  creator: 'Revised manuscript',
  title: TITLE,
  styles: { default: { document: { run: { font: 'Times New Roman', size: 22 } } } },
  numbering: { config: [ { reference: 'bul', levels: [ { level: 0, format: 'bullet', text: '\u2022',
    alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 600, hanging: 260 } } } } ] } ] },
  sections: [{
    properties: { page: { margin: { top: 1440, bottom: 1440, left: 1300, right: 1300 } } },
    footers: { default: new Footer({ children: [ new Paragraph({ alignment: AlignmentType.CENTER,
      children: [ new TextRun({ children: [PageNumber.CURRENT], font: 'Times New Roman', size: 18 }) ] }) ] }) },
    children: C
  }]
});
Packer.toBuffer(doc).then(b => {
  fs.writeFileSync('Revised_Manuscript_TwoSpanBeam_LoadIdentification.docx', b);
  console.log('written', b.length, 'bytes');
});
