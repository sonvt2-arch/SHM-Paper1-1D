"""
03_monte_carlo.py
=================
Monte Carlo robustness analysis, Table 6 of the revised paper.

Measurement model, Eq. (16):

    y_i^meas = (1 + gamma) y_i + eps0 + sigma_a xi_i

  gamma    relative gain (scale-factor) error   -- systematic, common-mode
  eps0     zero-offset / baseline error         -- systematic, NOT common-mode
  sigma_a  additive random noise                -- independent per sample

This replaces the purely multiplicative model y_i (1 + sigma xi_i) used in
the original draft, which predicts zero noise wherever the deflection
vanishes -- i.e. exactly at the supports, where a real transducer is no
quieter than anywhere else.

Two reference conditions are distinguished for SLM:
  "averaged"  the reference integral is taken as noise-free  (many repeats)
  "single"    the reference comes from one noisy crossing

The key result the old draft got backwards: for INDEPENDENT noise the
relative variances of the two integrals ADD, so a single noisy reference
multiplies the scatter of SLM by sqrt(2).  SLM cancels common-mode error;
it does not cancel independent noise.

Run:  python3 03_monte_carlo.py
"""

import numpy as np
import beam_theory as bt

N = 200_000
SEED = 20260817
rng = np.random.default_rng(SEED)
G = bt.G

I_REF = bt.integral_trapz(bt.Y_SINGLE, bt.X_1)


def perturbed_integral(y, x, n, gamma=0.0, eps=0.0, sigma_a=0.0, mult=0.0):
    """n realisations of the trapezoidal integral of a perturbed record."""
    gain = 1 + gamma * rng.standard_normal((n, 1)) if gamma else 1.0
    off = eps * rng.standard_normal((n, 1)) if eps else 0.0
    rnd = sigma_a * rng.standard_normal((n, y.size)) if sigma_a else 0.0
    m = 1 + mult * rng.standard_normal((n, y.size)) if mult else 1.0
    return np.trapezoid(gain * y * m + off + rnd, x, axis=1)


def stats(values, W):
    e = 100 * (values - W) / W
    return dict(mean_g=values.mean() / G * 1000,
                bias=e.mean(), mae=np.abs(e).mean(), sd=e.std(),
                p5=np.percentile(e, 5), p95=np.percentile(e, 95))


SCENARIOS = [
    ("Gain, sigma_gamma = 2 %",        dict(gamma=0.02)),
    ("Zero offset, sigma = 0.005 mm",  dict(eps=0.005)),
    ("Random, sigma_a = 0.0025 mm",    dict(sigma_a=0.0025)),
    ("All three combined",             dict(gamma=0.02, eps=0.005, sigma_a=0.0025)),
    ("Legacy model: 5 % multiplicative", dict(mult=0.05)),
]

hdr = "%-34s %-6s %-5s %-9s %9s %8s %8s %8s %8s"
print(hdr % ("scenario", "case", "meth", "reference",
             "mean (g)", "bias %", "MAE %", "p5 %", "p95 %"))
print("-" * 106)

for name, kw in SCENARIOS:
    for case in ("two", "three"):
        xg, yg, W = bt.CASES[case]
        It = perturbed_integral(yg, xg, N, **kw)
        I0 = perturbed_integral(bt.Y_SINGLE, bt.X_1, N, **kw)
        entries = [("BPM", "-", bt.bpm(It)),
                   ("SLM", "averaged", bt.slm(It, I_REF)),
                   ("SLM", "single", bt.slm(It, I0))]
        for meth, ref, vals in entries:
            s = stats(vals, W)
            print(hdr % (name if (case, meth, ref) == ("two", "BPM", "-") else "",
                         case, meth, ref, "%9.1f" % s["mean_g"],
                         "%+8.2f" % s["bias"], "%8.2f" % s["mae"],
                         "%+8.2f" % s["p5"], "%+8.2f" % s["p95"]))
    print()

# --------------------------------------------------------------------------
print("== Variance check, Eq. (20) ".ljust(74, "="))
xg, yg, W = bt.CASES["two"]
kw = dict(gamma=0.02, eps=0.005, sigma_a=0.0025)
It = perturbed_integral(yg, xg, N, **kw)
I0 = perturbed_integral(bt.Y_SINGLE, bt.X_1, N, **kw)
sd_clean = (100 * (bt.slm(It, I_REF) - W) / W).std()
sd_noisy = (100 * (bt.slm(It, I0) - W) / W).std()
print("SLM std dev, averaged reference : %.2f %%" % sd_clean)
print("SLM std dev, single reference   : %.2f %%" % sd_noisy)
print("ratio                           : %.3f   (sqrt(2) = 1.414)"
      % (sd_noisy / sd_clean))
print("BPM std dev                     : %.2f %%"
      % (100 * (bt.bpm(It) - W) / W).std())
print("\n-> prescription: average the calibration crossing over N_rep >= 5,")
print("   then SLM dominates BPM in bias and equals it in scatter.")
