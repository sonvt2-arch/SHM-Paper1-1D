"""
06_make_equations.py
====================
Renders every display equation of the revised paper to a transparent PNG
in ./eqs/, using LaTeX (amsmath + mathptmx, so the maths matches Times).

Requires: a TeX distribution with pdflatex, and pdftoppm (Poppler).

Numbering follows the revised manuscript:
  e01-e02  support reactions            e13-e14  trapezoid / Simpson
  e03      bending moment               e15      SLM
  e04      Euler-Bernoulli relation     e16      measurement model
  e05      full deflection field        e17-e18  error budgets BPM / SLM
  e06      influence line (64EI!)       e19      zero-offset bias
  e07-e09  invariance theorem           e20      SLM variance
  e10      Maxwell-Betti corollary      e21      speed / space-time
  e11      closed-form constant         e22      critical span ratio (unused)
  e12      BPM

Run:  python3 06_make_equations.py
"""

import os, subprocess, json
from PIL import Image
OUT="eqs/"; os.makedirs(OUT,exist_ok=True)

EQS = {
"e01": r"""\left\{\;\begin{aligned}
R_A^{AB} &= P\,\frac{x^{3}-5l^{2}x+4l^{3}}{4l^{3}}\\[2pt]
R_B^{AB} &= P\,\frac{-x^{3}+3l^{2}x}{2l^{3}}\\[2pt]
R_C^{AB} &= P\,\frac{x^{3}-l^{2}x}{4l^{3}}
\end{aligned}\right.\qquad 0\le x\le l""",

"e02": r"""\left\{\;\begin{aligned}
R_A^{BC} &= P\,\frac{-x^{3}+6lx^{2}-11l^{2}x+6l^{3}}{4l^{3}}\\[2pt]
R_B^{BC} &= P\,\frac{x^{3}-6lx^{2}+9l^{2}x-2l^{3}}{2l^{3}}\\[2pt]
R_C^{BC} &= P\,\frac{-x^{3}+6lx^{2}-7l^{2}x+2l^{3}}{4l^{3}}
\end{aligned}\right.\qquad l< x\le 2l""",

"e03": r"""M_s=\begin{cases}
R_A^{AB}\,s = P\,\dfrac{x^{3}-5l^{2}x+4l^{3}}{4l^{3}}\,s, & 0\le s\le x\le l\\[8pt]
R_A^{AB}\,s-P(s-x) = P\,\dfrac{x\left(sx^{2}-5sl^{2}+4l^{3}\right)}{4l^{3}}, & 0\le x\le s\le l\\[8pt]
R_A^{BC}\,s = P\,\dfrac{-x^{3}+6lx^{2}-11l^{2}x+6l^{3}}{4l^{3}}\,s, & 0\le s\le l< x\le 2l
\end{cases}""",

"e04": r"""\frac{d^{2}y}{ds^{2}}=-\,\frac{M_s}{EI}""",

"e05": r"""y_s=\frac{P}{24EI\,l^{3}}\begin{cases}
7l^{4}sx-4l^{3}s^{3}-12l^{3}sx^{2}+5l^{2}s^{3}x+5l^{2}sx^{3}-s^{3}x^{3}, & 0\le s\le x\le l\\[4pt]
7l^{4}sx-4l^{3}x^{3}-12l^{3}s^{2}x+5l^{2}s^{3}x+5l^{2}sx^{3}-s^{3}x^{3}, & 0\le x\le s\le l\\[4pt]
6l^{5}s-11l^{4}sx-6l^{3}s^{3}+6l^{3}sx^{2}+11l^{2}s^{3}x-l^{2}sx^{3}\\[1pt]
\qquad\qquad -\,6ls^{3}x^{2}+s^{3}x^{3}, & 0\le s\le l< x\le 2l
\end{cases}""",

"e06": r"""\eta(x)\;\equiv\;\frac{y_{l/2}(x)}{P}=\frac{1}{EI}\begin{cases}
\dfrac{x\left(9l^{2}-13x^{2}\right)}{192}, & 0\le x\le \dfrac{l}{2}\\[10pt]
\dfrac{(x-l)\left(4l^{2}-29lx+19x^{2}\right)}{192}, & \dfrac{l}{2}<x\le l\\[10pt]
\dfrac{(2l-x)\left(3l^{2}-4lx+x^{2}\right)}{64}, & l<x\le 2l\\[8pt]
0, & x<0 \ \text{ or }\ x>2l
\end{cases}""",

"e07": r"""y_m(x)=\sum_{i=1}^{n}P_i\,\eta_m\!\left(x-a_i\right),
\qquad a_1=0,\quad a_i\ \text{fixed}""",

"e08": r"""I_y\;=\;\int_{-\infty}^{+\infty}\! y_m(x)\,dx
\;=\;\sum_{i=1}^{n}P_i\int_{-\infty}^{+\infty}\!\eta_m\!\left(x-a_i\right)dx
\;=\;\left(\sum_{i=1}^{n}P_i\right)\!\int_{0}^{L}\!\eta_m(u)\,du\;=\;C_m\,P_{\mathrm{tot}}""",

"e09": r"""C_m=\int_{0}^{L}\eta_m(u)\,du
\qquad\text{and in practice}\qquad
I_y=\int_{0}^{\,L+a_{\max}} y_m(x)\,dx""",

"e10": r"""C_m=\int_{0}^{L}\eta_m(u)\,du=\int_{0}^{L}w_m(x)\,dx""",

"e11": r"""\begin{aligned}
C_m&=\int_{0}^{l/2}\!\eta\,dx+\int_{l/2}^{l}\!\eta\,dx+\int_{l}^{2l}\!\eta\,dx\\[2pt]
&=\frac{1}{192EI}\Big(\tfrac{59}{64}l^{4}+\tfrac{53}{64}l^{4}\Big)-\frac{1}{64EI}\cdot\tfrac{1}{4}l^{4}
\;=\;\frac{l^{4}}{192\,EI}
\end{aligned}""",

"e12": r"""P_{\mathrm{tot}}=\frac{I_y}{C_m}=\frac{192\,EI}{l^{4}}\,I_y""",

"e13": r"""I_y^{\mathrm{trap}}=\Delta x\left[\frac{y_0}{2}+\sum_{i=1}^{N-1}y_i+\frac{y_N}{2}\right],
\qquad \Delta x=\frac{L+a_{\max}}{N}""",

"e14": r"""I_y^{\mathrm{Simp}}=\frac{\Delta x}{3}\left[y_0+4\!\!\sum_{i\ \mathrm{odd}}\!\!y_i
+2\!\!\sum_{i\ \mathrm{even}}^{\,i\neq 0,N}\!\!y_i+y_N\right],\qquad N\ \text{even}""",

"e15": r"""P_t=P_0\,\frac{I_{y,t}}{I_{y,0}}
\qquad\text{(no knowledge of }EI\text{, }l\text{ or }C_m\text{ required)}""",

"e16": r"""y_i^{\mathrm{meas}}=(1+\gamma)\,y_i+\varepsilon_0+\sigma_a\,\xi_i,
\qquad \xi_i\sim\mathcal{N}(0,1)""",

"e17": r"""\left(\frac{\delta P}{P}\right)_{\!\mathrm{BPM}}
=\underbrace{\frac{\delta(EI)}{EI}-4\frac{\delta l}{l}}_{\text{structural}}
+\underbrace{\gamma}_{\text{gain}}
+\underbrace{\frac{\varepsilon_0\,L_{\mathrm{tot}}}{I_y}}_{\text{zero drift}}
+\underbrace{e_q}_{\text{quadrature}}
+\underbrace{\frac{\delta v}{v}}_{\text{speed}}""",

"e18": r"""\left(\frac{\delta P}{P}\right)_{\!\mathrm{SLM}}
=\frac{\delta P_0}{P_0}
+\varepsilon_0\!\left(\frac{L_{\mathrm{tot},t}}{I_{y,t}}-\frac{L_{\mathrm{tot},0}}{I_{y,0}}\right)
+\left(\frac{\delta v_t}{v_t}-\frac{\delta v_0}{v_0}\right)""",

"e19": r"""\left(\frac{\delta P}{P}\right)_{\!\varepsilon_0}=\frac{\varepsilon_0\,L_{\mathrm{tot}}}{I_y}""",

"e20": r"""I_y=\int y_m\,dx=\int y_m\,v(t)\,dt
\;\;\xrightarrow[\ ]{\;v=\mathrm{const}\;}\;\;v\!\int\! y_m\,dt,
\qquad v=\frac{2l}{t_{2}-t_{1}}""",

"e21": r"""\frac{\sigma^{2}_{P,\mathrm{SLM}}}{P^{2}}
=\frac{\sigma^{2}_{I_{y,t}}}{I_{y,t}^{2}}+\frac{1}{N_{\mathrm{rep}}}\frac{\sigma^{2}_{I_{y,0}}}{I_{y,0}^{2}}
\;\xrightarrow[\ N_{\mathrm{rep}}=1\ ]{}\;\sqrt{2}\,\frac{\sigma_{I_y}}{I_y}""",

"e22": r"""\left.\frac{l_2}{l_1}\right|_{\mathrm{crit}}=1.46
\qquad\Longrightarrow\qquad C_m=0\ \ \text{(method breaks down)}""",
}

TPL = r"""\documentclass[11pt,preview,border=1pt]{standalone}
\usepackage{amsmath,amssymb,mathptmx}
\begin{document}
$\displaystyle %s$
\end{document}
"""

meta={}
for k,v in EQS.items():
    open("/tmp/%s.tex"%k,"w").write(TPL % v)
    r=subprocess.run(["pdflatex","-interaction=nonstopmode","-output-directory=/tmp","/tmp/%s.tex"%k],
                     capture_output=True,text=True)
    if not os.path.exists("/tmp/%s.pdf"%k):
        print("FAIL",k); print(r.stdout[-1200:]); continue
    subprocess.run(["pdftoppm","-r","600","-png","-singlefile","/tmp/%s.pdf"%k,OUT+k],check=True)
    im=Image.open(OUT+k+".png").convert("RGBA")
    import numpy as _np
    a=_np.array(im); mask=(a[:,:,:3].min(axis=2)>245); a[:,:,3]=_np.where(mask,0,255)
    Image.fromarray(a).save(OUT+k+".png")
    im=Image.open(OUT+k+".png"); meta[k]=im.size
    print("%-5s %s"%(k,im.size))
json.dump(meta,open("eqmeta.json","w"))
