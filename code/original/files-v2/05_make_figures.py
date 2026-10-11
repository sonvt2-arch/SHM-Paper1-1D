"""
05_make_figures.py
==================
Generates every figure of the revised paper at 600 dpi into ./figs/.

Figures produced
----------------
  fig01_layout.png        beam layout, load on span AB / BC          (Fig. 1)
  fig02_twoloads.png      two-load layout          (kept for reference, unused)
  fig03_setup.png         experimental model, schematic + photo      (Fig. 3)
  fig04_influenceline.png influence line: analytical / FE / measured (Fig. 4)
  fig05_invariance.png    invariance demonstration                   (Fig. 5)
  fig06_quadrature.png    trapezoid vs Simpson bias                  (Table 2)
  fig07_montecarlo.png    Monte Carlo error distributions            (Fig. 8)
  fig08_zerodrift.png     zero-offset sensitivity                    (Fig. 7)
  fig09_calibration.png   calibration line I_y vs P                  (Fig. 6)
  fig10_parametric.png    span ratio and sensor position             (Fig. 9)
  fig11_flowchart.png     BPM / SLM workflow                         (Fig. 2)

The photograph for fig03 panel (b) is extracted from the original Word
file.  Set PHOTO below, or leave it as None to render panel (a) only.

Run:  python3 05_make_figures.py
"""

import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Rectangle, FancyArrowPatch, FancyBboxPatch
from scipy.integrate import simpson
from scipy.optimize import brentq
from PIL import Image

import beam_theory as bt

# Path to the laboratory photograph (word/media/image30.png inside the
# original .docx).  Set to None to skip panel (b) of Fig. 3.
PHOTO = "dx/word/media/image30.png"

plt.rcParams.update({"font.family": "serif", "font.serif": ["DejaVu Serif"],
                     "font.size": 9, "axes.linewidth": 0.8, "savefig.dpi": 600,
                     "savefig.bbox": "tight", "mathtext.fontset": "dejavuserif",
                     "axes.grid": False})
OUT = "figs/"
os.makedirs(OUT, exist_ok=True)

# ---------- constants and data, taken from the shared module ----------
EI, L, g, P0 = bt.EI, bt.L_SPAN, bt.G, bt.P0
Cth = bt.C_M
x1, y1e, ya = bt.X_1, bt.Y_SINGLE, bt.Y_ANALYTICAL
x2, y2e = bt.X_2, bt.Y_TWO
x3, y3e = bt.X_3, bt.Y_THREE
I1 = bt.integral_trapz(y1e, x1)
I2 = bt.integral_trapz(y2e, x2)
I3 = bt.integral_trapz(y3e, x3)
eta = bt.eta


def supports(ax,xs,ys,kind,s=1.0):
    for X,K in zip(xs,kind):
        w=0.045*s; h=0.075*s
        ax.add_patch(Polygon([[X,ys],[X-w,ys-h],[X+w,ys-h]],closed=True,fc="white",ec="k",lw=0.9,zorder=5))
        if K=="r":
            for d in(-0.55,0,0.55):
                ax.add_patch(plt.Circle((X+d*w,ys-h-0.018*s),0.018*s,fc="white",ec="k",lw=0.7,zorder=5))
            ax.plot([X-1.5*w,X+1.5*w],[ys-h-0.037*s]*2,"k",lw=0.9,zorder=5)
        else:
            ax.plot([X-1.5*w,X+1.5*w],[ys-h]*2,"k",lw=0.9,zorder=5)
            for i in np.linspace(-1.4,1.4,7):
                ax.plot([X+i*w,X+i*w-0.022*s],[ys-h,ys-h-0.045*s],"k",lw=0.6,zorder=5)

# ============ Fig 1 : layout ============
fig,axs=plt.subplots(2,1,figsize=(6.4,3.0))
for ax,xp,tag in zip(axs,[0.30,0.72],["(a)","(b)"]):
    ax.set_xlim(-0.06,1.10); ax.set_ylim(-0.40,0.62); ax.axis("off")
    ax.add_patch(Rectangle((0,0),1.0,0.045,fc="0.88",ec="k",lw=0.9))
    supports(ax,[0,0.5,1.0],0,["r","p","r"])
    ax.annotate("",xy=(xp,0.05),xytext=(xp,0.36),arrowprops=dict(arrowstyle="-|>",lw=1.1,color="k"))
    ax.text(xp,0.40,"$P$",ha="center",fontsize=10)
    ax.annotate("",xy=(xp,0.50),xytext=(0,0.50),arrowprops=dict(arrowstyle="<->",lw=0.7))
    ax.text(xp/2,0.53,"$x$",ha="center",fontsize=9)
    ax.text(0.80,0.115,"$EI$ = const",ha="center",fontsize=9)
    for a,b,lab in [(0,0.5,"$l$"),(0.5,1.0,"$l$")]:
        ax.annotate("",xy=(b,-0.16),xytext=(a,-0.16),arrowprops=dict(arrowstyle="<->",lw=0.7))
        ax.text((a+b)/2,-0.145,lab,ha="center",fontsize=9)
    for X,lab in [(0,"$A$"),(0.5,"$B$"),(1.0,"$C$")]:
        ax.text(X,0.075,lab,ha="center",fontsize=9,fontweight="bold")
    for X,lab in [(0,"$R_A$"),(0.5,"$R_B$"),(1.0,"$R_C$")]:
        ax.annotate("",xy=(X,-0.09),xytext=(X,-0.26),arrowprops=dict(arrowstyle="-|>",lw=0.9))
        ax.text(X+0.030,-0.30,lab,fontsize=8.5,ha="center")
    ax.text(1.07,0.02,tag,fontsize=10,fontweight="bold")
plt.tight_layout(h_pad=0.4); plt.savefig(OUT+"fig01_layout.png"); plt.close()

# ============ Fig 2 : two loads ============
fig,ax=plt.subplots(figsize=(6.4,1.7))
ax.set_xlim(-0.06,1.10); ax.set_ylim(-0.30,0.62); ax.axis("off")
ax.add_patch(Rectangle((0,0),1.0,0.045,fc="0.88",ec="k",lw=0.9))
supports(ax,[0,0.5,1.0],0,["r","p","r"])
for xp,lab in [(0.34,"$P_1$"),(0.22,"$P_2$")]:
    ax.annotate("",xy=(xp,0.05),xytext=(xp,0.34),arrowprops=dict(arrowstyle="-|>",lw=1.1))
    ax.text(xp,0.375,lab,ha="center",fontsize=10)
ax.annotate("",xy=(0.34,0.28),xytext=(0.22,0.28),arrowprops=dict(arrowstyle="<->",lw=0.7))
ax.text(0.28,0.30,"$a$",ha="center",fontsize=9)
ax.annotate("",xy=(0.34,0.50),xytext=(0,0.50),arrowprops=dict(arrowstyle="<->",lw=0.7))
ax.text(0.17,0.525,"$x$",ha="center",fontsize=9)
for a,b in [(0,0.5),(0.5,1.0)]:
    ax.annotate("",xy=(b,-0.16),xytext=(a,-0.16),arrowprops=dict(arrowstyle="<->",lw=0.7))
    ax.text((a+b)/2,-0.145,"$l$",ha="center",fontsize=9)
for X,lab in [(0,"$A$"),(0.5,"$B$"),(1.0,"$C$")]: ax.text(X,0.075,lab,ha="center",fontsize=9,fontweight="bold")
ax.text(0.78,0.115,"$EI$ = const",ha="center",fontsize=9)
plt.tight_layout(); plt.savefig(OUT+"fig02_twoloads.png"); plt.close()

# ============ Fig 3 : experimental setup ============
fig=plt.figure(figsize=(6.4,4.8))
ax=fig.add_axes([0.02,0.53,0.96,0.45]); ax.set_xlim(-0.10,1.14); ax.set_ylim(-0.86,0.72); ax.axis("off")
ax.add_patch(Rectangle((0,0),1.0,0.05,fc="0.88",ec="k",lw=0.9))
ax.add_patch(Rectangle((-0.058,0),0.058,0.05,fc="0.95",ec="k",lw=0.7))
ax.add_patch(Rectangle((1.0,0),0.058,0.05,fc="0.95",ec="k",lw=0.7))
supports(ax,[0,0.5,1.0],0,["r","p","r"])
ax.annotate("",xy=(0.25,0.06),xytext=(0.25,0.36),arrowprops=dict(arrowstyle="-|>",lw=1.2))
ax.text(0.25,0.39,"calibrated weight",ha="center",fontsize=8)
ax.plot([0.25],[0.055],"kv",ms=4)
ax.add_patch(Rectangle((0.225,-0.34),0.05,0.10,fc="0.6",ec="k",lw=0.7))
ax.plot([0.25,0.25],[-0.10,-0.18],"k",lw=0.8)
ax.add_patch(Rectangle((0.213,-0.19),0.074,0.10,fc="white",ec="k",lw=0.9))
ax.text(0.25,-0.145,"LVDT",ha="center",fontsize=7.5)
ax.text(0.02,-0.45,"LVDT: range 0–50 mm, resolution 0.005 mm",ha="left",fontsize=7,va="center")
ax.annotate("",xy=(0.25,0.50),xytext=(0,0.50),arrowprops=dict(arrowstyle="<->",lw=0.7))
ax.text(0.125,0.525,"$l/2$ = 1250",ha="center",fontsize=8)
for a,b,lab in [(0,0.5,"$l$ = 2500 mm"),(0.5,1.0,"$l$ = 2500 mm")]:
    ax.annotate("",xy=(b,-0.62),xytext=(a,-0.62),arrowprops=dict(arrowstyle="<->",lw=0.7))
    ax.text((a+b)/2,-0.605,lab,ha="center",fontsize=8)
ax.annotate("",xy=(1.058,-0.74),xytext=(-0.058,-0.74),arrowprops=dict(arrowstyle="<->",lw=0.7))
ax.text(0.5,-0.725,"total length 5400 mm",ha="center",fontsize=8)
for X,lab in [(0,"$A$ (roller)"),(0.5,"$B$ (knife edge)"),(1.0,"$C$ (roller)")]:
    ax.text(X,0.09,lab,ha="center",fontsize=8,fontweight="bold")
ax.text(0.72,0.185,"hollow square tube 25×25×2.03 mm,  $E$ = 200 GPa",ha="center",fontsize=8)
ax.text(-0.095,0.62,"(a)",fontsize=10,fontweight="bold")
if PHOTO and os.path.exists(PHOTO):
    im = Image.open(PHOTO).rotate(-1.8, expand=False, resample=Image.BICUBIC)
    im = im.crop((0, 180, 2560, 1400))
    ax2 = fig.add_axes([0.09, 0.01, 0.82, 0.44]); ax2.imshow(im); ax2.axis("off")
    ax2.text(-0.03, 1.02, "(b)", transform=ax2.transAxes, fontsize=10, fontweight="bold")
else:
    print("  (photo not found at %s -- Fig. 3 panel (b) skipped)" % PHOTO)
plt.savefig(OUT+"fig03_setup.png"); plt.close()

# ============ Fig 4 : influence line + error ============
fig,axs=plt.subplots(2,1,figsize=(6.0,4.4),sharex=True,gridspec_kw=dict(height_ratios=[3,1.25],hspace=0.10))
xf=np.linspace(0,2*L,1201)
axs[0].plot(xf,eta(xf,P0),"-",color="0.15",lw=1.3,label="Analytical, Eq. (10)")
axs[0].plot(x1,ya,"o",mfc="none",mec="C0",ms=5.5,mew=1.0,label="FE (Abaqus, B23)")
axs[0].plot(x1,y1e,"s",mfc="none",mec="C3",ms=5.0,mew=1.0,label="Experiment")
axs[0].axhline(0,color="k",lw=0.6); axs[0].axvline(L,color="0.6",lw=0.7,ls=":")
axs[0].fill_between(xf,0,eta(xf,P0),where=eta(xf,P0)>0,color="C0",alpha=0.10)
axs[0].fill_between(xf,0,eta(xf,P0),where=eta(xf,P0)<0,color="C3",alpha=0.10)
axs[0].set_ylabel("Mid-span deflection $y_{l/2}$  (mm)")
axs[0].legend(frameon=False,loc="upper right",fontsize=8.5)
axs[0].text(1250,0.55,"$A^+$",ha="center",color="C0",fontsize=10)
axs[0].text(3620,-0.62,"$A^-$",ha="center",color="C3",fontsize=10)
axs[0].text(L+90,2.9,"support $B$",fontsize=8,color="0.35")
axs[0].set_ylim(-1.6,3.4)
err=(y1e-ya)
axs[1].bar(x1,err,width=90,color="C3",alpha=0.8)
axs[1].axhline(0,color="k",lw=0.6); axs[1].axvline(L,color="0.6",lw=0.7,ls=":")
axs[1].set_ylabel("Exp. $-$ Anal.\n(mm)",fontsize=8.5)
axs[1].set_xlabel("Position of the load from support $A$,  $x$ (mm)")
axs[1].set_ylim(-0.021,0.026)
axs[1].text(0.03,0.90,"max $|\\Delta y|$ = 0.0125 mm  (0.43 % of $y_{max}$)",transform=axs[1].transAxes,fontsize=8)
for a in axs: a.set_xlim(0,2*L); a.tick_params(direction="in",top=True,right=True)
plt.savefig(OUT+"fig04_influenceline.png"); plt.close()

# ============ Fig 5 : invariance (graphical abstract) ============
fig,axs=plt.subplots(1,3,figsize=(6.6,2.5),sharey=True)
Ptot=1.0
cfgs=[([1.0],[0],"single axle"),([0.5,0.5],[0,0.30],"2 axles, $a$=0.30$l$"),([0.3,0.35,0.35],[0,0.25,0.55],"3 axles")]
xf=np.linspace(-0.1,2.7,1400)
for ax,(ws,offs,lab) in zip(axs,cfgs):
    yy=sum(w*eta(np.clip((xf-o)*L,-1,3*L),1.0) for w,o in zip(ws,offs))
    yy=yy/ (P0*Cth/L) *0+ sum(w*eta((xf-o)*L,P0) for w,o in zip(ws,offs))
    ax.plot(xf,yy,color="0.15",lw=1.3)
    ax.fill_between(xf,0,yy,where=yy>0,color="C0",alpha=0.22)
    ax.fill_between(xf,0,yy,where=yy<0,color="C3",alpha=0.22)
    ax.axhline(0,color="k",lw=0.6)
    A=np.trapezoid(yy,xf*L)
    ax.set_title(lab,fontsize=9)
    ax.text(0.5,0.05,"$I_y$ = %.0f mm$^2$"%A,transform=ax.transAxes,ha="center",fontsize=9,
            bbox=dict(fc="white",ec="0.6",lw=0.6,pad=2))
    for o,w in zip(offs,ws):
        ax.annotate("",xy=(0.55+o*0,0),xytext=(0,0),arrowprops=dict(arrowstyle="-"))
    ax.set_xlim(-0.1,2.7); ax.tick_params(direction="in",labelsize=8)
    ax.set_xlabel("$x/l$",fontsize=9)
axs[0].set_ylabel("$y_{l/2}$ (mm)",fontsize=9)
fig.suptitle("Same total load $P$ = 40.64 N — different axle configurations — identical deflection integral",
             fontsize=9.2,y=1.02)
plt.tight_layout(); plt.savefig(OUT+"fig05_invariance.png"); plt.close()

# ============ Fig 6 : quadrature ============
ns=[2,4,5,10,20,25,50]
tr=[];si=[]
for n in ns:
    xs=np.linspace(0,2*L,2*n+1); yy=eta(xs,P0)
    tr.append(abs(100*(np.trapezoid(yy,xs)-P0*Cth)/(P0*Cth)))
    si.append(max(abs(100*(simpson(yy,x=xs)-P0*Cth)/(P0*Cth)),1e-4))
fig,ax=plt.subplots(figsize=(5.0,3.2))
idx=np.arange(len(ns)); w=0.38
b1=ax.bar(idx-w/2,tr,w,color="C3",label="Trapezoidal rule")
b2=ax.bar(idx+w/2,si,w,color="C0",label="Simpson's rule")
ax.set_yscale("log"); ax.set_ylim(5e-5,60)
for b,v in list(zip(b1,tr))+list(zip(b2,si)):
    ax.text(b.get_x()+b.get_width()/2,v*1.35,("%.3f"%v if v>=1e-3 else "<0.001"),
            ha="center",fontsize=6.8,rotation=90)
ax.set_xticks(idx); ax.set_xticklabels(["%d\n(%.0f)"%(n,L/n) for n in ns])
ax.set_xlabel("Segments per span $n$   (sampling interval $\\Delta x$, mm)")
ax.set_ylabel("|Quadrature bias of $I_y$|  (%)")
ax.axvspan(2.5,3.5,color="C1",alpha=0.10,zorder=0)
ax.text(3,2.5e-4,"present tests",ha="center",fontsize=7.6,color="0.3")
ax.legend(frameon=False,fontsize=8.5,loc="upper right",bbox_to_anchor=(1.0,1.02))
ax.tick_params(direction="in",which="both",top=True,right=True)
ax.grid(axis="y",which="major",lw=0.3,alpha=0.4)
plt.tight_layout(); plt.savefig(OUT+"fig06_quadrature.png"); plt.close()

# ============ Fig 7 : Monte Carlo ============
rng=np.random.default_rng(20260817); N=120000
def draw(y,x,n,gam,eps,sa):
    G=1+gam*rng.standard_normal((n,1)); E=eps*rng.standard_normal((n,1)); A=sa*rng.standard_normal((n,y.size))
    return np.trapezoid(G*y+E+A,x,axis=1)
W2=6.829*g
kw=dict(gam=0.02,eps=0.005,sa=0.0025)
It=draw(y2e,x2,N,**kw); I0n=draw(y1e,x1,N,**kw)
eB=100*(192*EI*It/L**4-W2)/W2; eSc=100*(P0*It/I1-W2)/W2; eSn=100*(P0*It/I0n-W2)/W2
fig,ax=plt.subplots(figsize=(5.4,3.2))
bins=np.linspace(-9,11,120)
for e,lab,c in [(eB,"BPM","C3"),(eSc,"SLM, averaged reference","C0"),(eSn,"SLM, single noisy reference","C2")]:
    ax.hist(e,bins=bins,histtype="step",lw=1.4,color=c,density=True,
            label="%s  ($\\mu$=%.2f%%, $\\sigma$=%.2f%%)"%(lab,e.mean(),e.std()))
ax.axvline(0,color="k",lw=0.8)
ax.set_xlabel("Relative error of the identified total load (%)"); ax.set_ylabel("Probability density")
ax.set_ylim(0,0.29)
ax.legend(frameon=False,fontsize=8,loc="upper left"); ax.tick_params(direction="in",top=True,right=True)
plt.tight_layout(); plt.savefig(OUT+"fig07_montecarlo.png"); plt.close()

# ============ Fig 8 : zero drift ============
eps=np.linspace(0,0.10,200)
fig,ax=plt.subplots(figsize=(4.8,3.2))
for I,Lt,lab,c in [(I1,5000,"single load ($I_y$ = 2513 mm$^2$)","C3"),
                   (I2,5250,"two loads ($I_y$ = 4168 mm$^2$)","C1"),
                   (I3,5750,"three loads ($I_y$ = 7789 mm$^2$)","C0")]:
    ax.plot(eps,100*eps*Lt/I,lw=1.4,color=c,label=lab)
ax.axvline(0.005,color="0.5",ls=":",lw=0.9); ax.text(0.0062,9.6,"LVDT resolution",fontsize=7.4,color="0.35",rotation=90,va="top")
ax.axvspan(0.02,0.06,color="0.85",alpha=0.55,zorder=0)
ax.text(0.040,9.6,"typical thermal /\nsettlement drift\non a real bridge",fontsize=7.6,ha="center",va="top",color="0.3")
ax.set_xlabel("Zero-offset error of the deflection signal, $\\varepsilon_0$ (mm)")
ax.set_ylabel("Resulting bias of identified load (%)")
ax.legend(frameon=False,fontsize=7.8,loc="lower right"); ax.set_ylim(0,10); ax.set_xlim(0,0.10)
ax.tick_params(direction="in",top=True,right=True)
plt.tight_layout(); plt.savefig(OUT+"fig08_zerodrift.png"); plt.close()

# ============ Fig 9 : calibration ============
Ps=np.array([P0,6.829*g,12.750*g]); Is=np.array([I1,I2,I3])
a=np.sum(Ps*Is)/np.sum(Ps*Ps); r2=1-np.sum((Is-a*Ps)**2)/np.sum((Is-Is.mean())**2)
fig,ax=plt.subplots(figsize=(4.4,3.2))
pp=np.linspace(0,135,50)
ax.plot(pp,Cth*pp,"--",color="0.35",lw=1.1,label="Theory, $I_y = P\\,l^4/192EI$")
ax.plot(pp,a*pp,"-",color="C0",lw=1.2,label="Fit, $I_y$ = %.2f$P$  ($R^2$ = %.5f)"%(a,r2))
ax.plot(Ps,Is,"o",color="C3",ms=6,label="Measured (1, 2, 3 loads)")
ax.set_xlabel("Total applied load $P$ (N)"); ax.set_ylabel("Deflection integral $I_y$ (mm$^2$)")
ax.legend(frameon=False,fontsize=8,loc="upper left"); ax.tick_params(direction="in",top=True,right=True)
ax.set_xlim(0,135); ax.set_ylim(0,8600)
plt.tight_layout(); plt.savefig(OUT+"fig09_calibration.png"); plt.close()

# ============ Fig 10 : parametric ============
C_of = bt.C_of
rr=np.linspace(0.4,2.0,60); Cr=[C_of(1.,r,0.5) for r in rr]
rc=brentq(lambda r:C_of(1.,r,0.5),1.3,1.7)
xx=np.linspace(0.10,0.95,50); Cx=[C_of(1.,1.,v) for v in xx]; Cm=C_of(1.,1.,0.5)
fig,axs=plt.subplots(1,2,figsize=(6.6,2.9))
axs[0].plot(rr,np.array(Cr)*192,lw=1.4,color="C0")
axs[0].axhline(0,color="k",lw=0.7); axs[0].axvline(rc,color="C3",ls="--",lw=1.0)
axs[0].plot([1.0],[1.0],"o",color="C3",ms=6)
axs[0].text(rc+0.05,0.62,"$l_2/l_1$ = %.2f\n$C_m\\to 0$:\nmethod fails"%rc,fontsize=7.8,color="C3",va="top")
axs[0].text(0.98,1.22,"equal spans\n(present study)",fontsize=7.8,ha="right")
axs[0].axvspan(rc,2.0,color="C3",alpha=0.08)
axs[0].set_xlabel("Span ratio $l_2/l_1$  (sensor at mid-span of span 1)")
axs[0].set_ylabel("$192\\,EI\\,C_m/l_1^4$  ( = 1 for equal spans)")
axs[0].tick_params(direction="in",top=True,right=True); axs[0].set_xlim(0.4,2.0); axs[0].set_ylim(-2.2,1.7)
axs[1].plot(xx,np.array(Cx)/Cm,lw=1.4,color="C0")
axs[1].plot([0.5],[1.0],"o",color="C3",ms=6); axs[1].plot([0.42],[C_of(1,1,0.42)/Cm],"^",color="C2",ms=7)
axs[1].text(0.30,0.60,"optimum at\n$x_m$ = 0.42$l$\n(only +4.0 %)",fontsize=7.8,color="C2")
axs[1].text(0.56,0.94,"mid-span\n(present study)",fontsize=7.8,color="C3")
axs[1].set_xlabel("Sensor position on span 1,  $x_m/l$")
axs[1].set_ylabel("$C_m$ normalised by its mid-span value")
axs[1].tick_params(direction="in",top=True,right=True); axs[1].set_xlim(0.1,0.95); axs[1].set_ylim(0,1.22)
for a,tg in zip(axs,["(a)","(b)"]): a.text(0.01,1.03,tg,transform=a.transAxes,fontsize=10,fontweight="bold")
plt.tight_layout(); plt.savefig(OUT+"fig10_parametric.png"); plt.close()

# ============ Fig 11 : flowchart ============
fig,ax=plt.subplots(figsize=(6.4,3.6)); ax.set_xlim(0,10); ax.set_ylim(0,6.4); ax.axis("off")
def box(x,y,w,h,txt,fc="white",fs=8.2,bold=False):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle="round,pad=0.06",fc=fc,ec="0.25",lw=0.9))
    ax.text(x+w/2,y+h/2,txt,ha="center",va="center",fontsize=fs,
            fontweight="bold" if bold else "normal",linespacing=1.35)
def arr(x1_,y1_,x2_,y2_):
    ax.add_patch(FancyArrowPatch((x1_,y1_),(x2_,y2_),arrowstyle="-|>",mutation_scale=9,lw=0.9,color="0.25"))
box(3.1,5.5,3.8,0.72,"Record $y_m(t)$ for one full crossing\n(first axle on → last axle off)","0.93",bold=True)
box(3.1,4.35,3.8,0.72,"Convert to space: $x = \\int v\\,dt$\n(speed from the two zero-crossings)","0.96")
box(3.1,3.20,3.8,0.72,"Compute $I_y=\\int y_m\\,dx$\n(Simpson, Eq. (16))","0.96")
box(0.35,1.55,4.1,1.25,"BPM\n$P=I_y/C_m$,  $C_m=l^4/192EI$\nrequires $EI$ and $l$","#e8f1fa",bold=True)
box(5.55,1.55,4.1,1.25,"SLM\n$P=P_0\\,I_y/I_{y,0}$\nrequires one calibrated crossing","#fdeeea",bold=True)
box(2.9,0.15,4.2,0.85,"Total load $P$  →  overload screening","0.93",bold=True)
arr(5,5.5,5,5.07); arr(5,4.35,5,3.92); arr(5,3.20,5,2.80)
arr(4.2,2.80,2.4,2.80); arr(5.8,2.80,7.6,2.80)
arr(2.4,1.55,4.2,1.00); arr(7.6,1.55,5.8,1.00)
ax.text(0.35,3.35,"cancels:\n• $EI$ uncertainty\n• quadrature bias\n• sensor gain error",fontsize=7.6,color="C0",va="top")
ax.text(9.65,3.35,"but: reference must be\naveraged over repeats,\notherwise $\\sigma$ increases\nby $\\sqrt{2}$",fontsize=7.6,color="C3",va="top",ha="right")
plt.tight_layout(); plt.savefig(OUT+"fig11_flowchart.png"); plt.close()
print("figures written to %s:" % OUT)
for f in sorted(os.listdir(OUT)):
    print("   ", f)
