"""s04_monte_carlo.py - Monte Carlo robustness analysis (Appendix B, Table B.1; Section 6.3).

Measurement model, Eq. (16):
    y_i^meas = (1 + gamma) y_i + eps0 + sigma_a zeta_i,   zeta_i ~ N(0, 1)
  gamma : gain error, one draw per crossing        (sigma_gamma = 2 %)
  eps0  : residual zero offset, one draw per crossing (sigma_eps = 0.005 mm)
  zeta  : additive noise, independent per sample    (sigma_a = 0.0025 mm = resolution/2)
Each realisation perturbs the MEASURED record (Appendix C), recomputes the
trapezoidal integral on the same grid and re-identifies the load.
SLM reference: "averaged" = unperturbed measured single-load record;
"single" = one independently perturbed reference crossing.

200 000 realisations per case, fixed seed 20260817.  The random stream (order
of the draws) is the same as in code/original/files-v2/03_monte_carlo.py, so
the percentiles reproduce that script digit for digit; this script adds the
standard deviation that Table B.1 reports.

Reproduces: Table B.1 (bias, std. dev., p5, p95), the statement that the
three-load case agrees within 0.1 percentage point, and Section 6.3 (0.07 %,
2.11 % -> 3.09 %, factor 1.47, BPM 2.12 %).

Run:  python3 -I code/supplementary/s04_monte_carlo.py      (about 10 s)
"""
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import beam_theory as bt  # noqa: E402

N = 200_000
SEED = 20260817
rng = np.random.default_rng(SEED)
I_REF = bt.integral_trapz(bt.Y_SINGLE, bt.X_1)


def perturbed_integral(y, x, n, gamma=0.0, eps=0.0, sigma_a=0.0, mult=0.0):
    """n realisations of the trapezoidal integral of a record perturbed by Eq. (16)."""
    gain = 1 + gamma * rng.standard_normal((n, 1)) if gamma else 1.0
    off = eps * rng.standard_normal((n, 1)) if eps else 0.0
    rnd = sigma_a * rng.standard_normal((n, y.size)) if sigma_a else 0.0
    m = 1 + mult * rng.standard_normal((n, y.size)) if mult else 1.0
    return bt.integral_trapz(gain * y * m + off + rnd, x, axis=1)


def stats(values, W):
    e = 100 * (values - W) / W
    return dict(bias=e.mean(), sd=e.std(), mae=np.abs(e).mean(),
                p5=np.percentile(e, 5), p95=np.percentile(e, 95))


SCENARIOS = [
    ("Gain, sigma_gamma = 2 %", dict(gamma=0.02)),
    ("Zero offset, sigma_eps = 0.005 mm", dict(eps=0.005)),
    ("Random, sigma_a = 0.0025 mm", dict(sigma_a=0.0025)),
    ("Combined", dict(gamma=0.02, eps=0.005, sigma_a=0.0025)),
    # kept only so that the random stream stays identical to files-v2; NOT in the manuscript
    ("Legacy 5 % multiplicative (not in manuscript)", dict(mult=0.05)),
]

TABLE_B1 = {  # manuscript Table B.1, two loads: bias, sd, p5, p95
    ("Gain, sigma_gamma = 2 %", "BPM", "n/a"): (1.10, 2.01, -2.21, 4.40),
    ("Gain, sigma_gamma = 2 %", "SLM", "averaged"): (0.61, 2.00, -2.69, 3.90),
    ("Gain, sigma_gamma = 2 %", "SLM", "single"): (0.66, 2.85, -3.94, 5.41),
    ("Zero offset, sigma_eps = 0.005 mm", "BPM", "n/a"): (1.10, 0.64, 0.05, 2.15),
    ("Zero offset, sigma_eps = 0.005 mm", "SLM", "averaged"): (0.61, 0.63, -0.43, 1.65),
    ("Zero offset, sigma_eps = 0.005 mm", "SLM", "single"): (0.62, 1.19, -1.31, 2.60),
    ("Random, sigma_a = 0.0025 mm", "BPM", "n/a"): (1.10, 0.07, 0.99, 1.21),
    ("Random, sigma_a = 0.0025 mm", "SLM", "averaged"): (0.61, 0.07, 0.50, 0.72),
    ("Random, sigma_a = 0.0025 mm", "SLM", "single"): (0.61, 0.13, 0.40, 0.82),
    ("Combined", "BPM", "n/a"): (1.10, 2.12, -2.39, 4.59),
    ("Combined", "SLM", "averaged"): (0.61, 2.11, -2.87, 4.08),
    ("Combined", "SLM", "single"): (0.65, 3.09, -4.34, 5.83),
}

hdr = "%-46s %-6s %-4s %-9s %8s %8s %8s %8s   %s"
print("Monte Carlo, N = %d per case, seed %d; relative error w.r.t. weighing (%%)" % (N, SEED))
print(hdr % ("error source", "case", "meth", "reference", "bias", "sd", "p5", "p95",
             "Table B.1 (bias sd p5 p95)"))
print("-" * 140)
results = {}
for name, kw in SCENARIOS:
    for case in ("two", "three"):
        xg, yg, W = bt.CASES[case]
        It = perturbed_integral(yg, xg, N, **kw)
        I0 = perturbed_integral(bt.Y_SINGLE, bt.X_1, N, **kw)
        for meth, ref, vals in (("BPM", "n/a", bt.bpm(It)),
                                ("SLM", "averaged", bt.slm(It, I_REF)),
                                ("SLM", "single", bt.slm(It, I0))):
            s = stats(vals, W)
            results[(name, case, meth, ref)] = s
            ms = TABLE_B1.get((name, meth, ref)) if case == "two" else None
            print(hdr % (name, case, meth, ref, "%+.2f" % s["bias"], "%.2f" % s["sd"],
                         "%+.2f" % s["p5"], "%+.2f" % s["p95"],
                         "" if ms is None else "%+.2f %.2f %+.2f %+.2f" % ms))
    print()

print("== Check against Table B.1 (two loads, values rounded to 0.01) ".ljust(78, "="))
nmis = 0
for (name, meth, ref), ms in TABLE_B1.items():
    s = results[(name, "two", meth, ref)]
    got = (round(s["bias"], 2), round(s["sd"], 2), round(s["p5"], 2), round(s["p95"], 2))
    d = max(abs(a - b) for a, b in zip(got, ms))
    flag = "match" if d < 0.0101 else "MISMATCH (max diff %.2f)" % d
    nmis += d >= 0.0101
    print("  %-36s %-3s %-8s %s" % (name, meth, ref, flag))
print("  %d of %d rows differ by more than one unit in the last digit" % (nmis, len(TABLE_B1)))

print("\n== 'The three-load case agrees within 0.1 percentage point' ".ljust(78, "="))
for name, _ in SCENARIOS[:4]:
    for meth, ref in (("BPM", "n/a"), ("SLM", "averaged"), ("SLM", "single")):
        a, b = results[(name, "two", meth, ref)], results[(name, "three", meth, ref)]
        dd = {k: b[k] - a[k] for k in ("bias", "sd", "p5", "p95")}
        mx = max(abs(v) for v in dd.values())
        print("  %-36s %-3s %-8s three - two: bias %+.2f sd %+.2f p5 %+.2f p95 %+.2f  %s"
              % (name, meth, ref, dd["bias"], dd["sd"], dd["p5"], dd["p95"],
                 "<= 0.1" if mx <= 0.1 else "> 0.1"))

print("\n== Section 6.3 / Eq. (20) ".ljust(78, "="))
xg, yg, W = bt.CASES["two"]
kw = dict(gamma=0.02, eps=0.005, sigma_a=0.0025)
It = perturbed_integral(yg, xg, N, **kw)
I0 = perturbed_integral(bt.Y_SINGLE, bt.X_1, N, **kw)
sd_avg = (100 * (bt.slm(It, I_REF) - W) / W).std()
sd_one = (100 * (bt.slm(It, I0) - W) / W).std()
print("  (independent re-draw of the combined case, as in files-v2)")
print("  SLM sd, averaged reference : %.2f %%   (2.11)" % sd_avg)
print("  SLM sd, single reference   : %.2f %%   (3.09)" % sd_one)
print("  ratio                      : %.3f    (1.47; sqrt 2 = 1.414)" % (sd_one / sd_avg))
print("  BPM sd                     : %.2f %%   (2.12)" % (100 * (bt.bpm(It) - W) / W).std())
print("  random noise alone, BPM sd : %.2f %%   (0.07)"
      % results[("Random, sigma_a = 0.0025 mm", "two", "BPM", "n/a")]["sd"])
