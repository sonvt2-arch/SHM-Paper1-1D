"""Secondary check on the model-generated (CSiBridge, Varina-Enon Bridge, NOT the Smart
Road Bridge) strain records shipped with the NOR-BWIM dataset (100 Hz, 20 m/s).
Truck/lane assignment of each file from mainMPNORBWIM.mlx (read as text); truck data
from dissertation Table 3.3. Run: python3 -I nb_fe_veb.py
"""
import os
import sys
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import nb_io as nio  # noqa: E402

T33 = {1: (3, 23.2), 2: (3, 23.3), 3: (5, 32.9), 4: (5, 38.6), 5: (4, 32.1), 6: (4, 27.8)}
FILES = [  # file, lane, trucks (Table 3.3 numbers), role in the script
    ("Run2.txt", 2, [2], "Test 1 L2"), ("Run1_2.txt", 2, [1], "Test 2 L2"),
    ("Run13.txt", 2, [1], "Test 3 L2"), ("Run5_2.txt", 2, [3], "Test 5 L2"),
    ("Run6.txt", 2, [4], "Test 6 L2"), ("Run9_2.txt", 2, [5], "Test 7 L2 (calib.)"),
    ("Run10.txt", 2, [6], "Test 8 L2 (calib.)"), ("Run4.txt", 1, [2], "Test 1 L1"),
    ("Run3_2.txt", 1, [1], "Test 2 L1"), ("Run14.txt", 1, [1], "Test 3 L1"),
    ("Run7_2.txt", 1, [3], "Test 5 L1"), ("Run8.txt", 1, [4], "Test 6 L1"),
    ("Run11_2.txt", 1, [5], "Test 7 L1 (calib.)"), ("Run12.txt", 1, [6], "Test 8 L1 (calib.)"),
    ("Run17.txt", 1, [2, 4], "Eva 1: 3-ax + 5-ax in line, L1"),
    ("Run18.txt", 2, [2, 4], "Eva 2: 3-ax + 5-ax in line, L2"),
]
FS, V = 100.0, 20.0


def integ(y, fs=FS, v=V, nb=50):
    """Primary: plain integral (simulations start at rest, y[0] = 0, and the added noise
    is zero-mean). Alternative: linear end baseline to the mean of the last nb samples."""
    yb = np.linspace(0.0, np.mean(y[-nb:]), len(y))
    return np.trapezoid(y, dx=1 / fs) * v, np.trapezoid(y - yb, dx=1 / fs) * v


rows = []
for f, lane, trk, role in FILES:
    y = nio.load_txt(f)
    I, I0 = integ(y)
    W = sum(T33[t][1] for t in trk)
    rows.append(dict(file=f, lane=lane, trucks="+".join(map(str, trk)),
                     axles="+".join(str(T33[t][0]) for t in trk), GVW=W, role=role,
                     N=len(y), duration_s=len(y) / FS, Idx=I, Idx_endbase=I0,
                     Idx_per_t=I / W, Idx_per_t_endbase=I0 / W))
R = pd.DataFrame(rows)
# speed series (3-axle; 3axle_speed_20 is byte-identical to Run2.txt = Truck 2, lane 2)
sp = []
for v in [15, 20, 22, 25, 27, 30, 32, 35]:
    y = nio.load_txt(f"3axle_speed_{v}.txt")
    I, I0 = integ(y, v=v)
    sp.append(dict(file=f"3axle_speed_{v}.txt", v=v, N=len(y), Idx=I, Idx_per_t=I / 23.3,
                   Idx_endbase=I0, record_length_m=len(y) / FS * v))
S = pd.DataFrame(sp)
out = os.path.join(HERE, "results")
R.to_csv(os.path.join(out, "fe_veb_integrals.csv"), index=False)
S.to_csv(os.path.join(out, "fe_veb_speed.csv"), index=False)
with open(os.path.join(HERE, "logs", "fe_veb.log"), "w") as L:
    for lane in (1, 2):
        sub = R[(R.lane == lane) & ~R.trucks.str.contains(r"\+")]
        # one record per truck (truck 1 has duplicates); all records used
        cv = sub.Idx_per_t.std(ddof=1) / abs(sub.Idx_per_t.mean())
        cv0 = sub.Idx_per_t_endbase.std(ddof=1) / abs(sub.Idx_per_t_endbase.mean())
        L.write(f"lane {lane}: n={len(sub)} mean Idx/GVW={sub.Idx_per_t.mean():.3f} "
                f"CV={cv:.3f} (with end baseline: CV={cv0:.3f})\n")
        m = R[(R.lane == lane) & R.trucks.str.contains(r"\+")]
        for _, e in m.iterrows():
            pred = sub.Idx_per_t.mean() * e.GVW
            L.write(f"  {e.file}: Idx={e.Idx:.1f}, single-truck prediction {pred:.1f}, "
                    f"ratio {e.Idx / pred:.3f}; SLM GVW={e.Idx / sub.Idx_per_t.mean():.1f} "
                    f"t vs {e.GVW}\n")
    L.write(f"speed series: CV of Idx = {S.Idx.std(ddof=1) / abs(S.Idx.mean()):.3f}\n")
    L.write(R.round(3).to_string() + "\n" + S.round(3).to_string() + "\n")
print(open(os.path.join(HERE, "logs", "fe_veb.log")).read())

fig, ax = plt.subplots(1, 2, figsize=(7.2, 2.8))
for lane, mk in [(1, "o"), (2, "s")]:
    sub = R[R.lane == lane]
    ax[0].plot(range(len(sub)), sub.Idx_per_t, mk, label=f"lane {lane}")
ax[0].set_xticks(range(len(R[R.lane == 1])))
ax[0].set_xticklabels([f"{a}\n{b}" for a, b in zip(R[R.lane == 1].trucks,
                                                    R[R.lane == 1].axles)], fontsize=6)
ax[0].set_ylabel(r"$\int\varepsilon dx$/GVW ($\mu\varepsilon$ m/t)")
ax[0].set_title("VEB CSiBridge records (truck no. / axles)", fontsize=8)
ax[0].legend(fontsize=7)
ax[1].plot(S.v, S.Idx_per_t, "o-")
ax[1].set_xlabel("speed (m/s)")
ax[1].set_ylabel(r"$\int\varepsilon dx$/GVW")
ax[1].set_title("VEB 3-axle speed series", fontsize=8)
fig.tight_layout()
for e in ("png", "pdf"):
    fig.savefig(os.path.join(HERE, "figures", f"fig7_fe_veb.{e}"), dpi=300)
