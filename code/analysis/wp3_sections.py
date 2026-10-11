"""WP3 - cross-section properties of the two continuous box girders.

Polygon (Green's theorem) section properties for single-cell box sections.
Coordinates: half-section (x >= 0, symmetric about the bridge axis), z upward
from the soffit at the axis, units m.  Vertical-bending I = I about the
horizontal centroidal axis.

Sources (every dimension is quoted with its source in `SOURCES` below):
  CM  = Cau May, "04 - Danh gia tai trong cau chinh.pdf" (Drive id
        1HNyul9T5k12wWprgo9gNZMh-w0qRNyWw), p.3 (cross-section drawing, mm)
        and p.5 (MIDAS-type section table).
  TB  = Thai Binh, "T.Minh Thai Binh - 10-9-2020.doc" (Drive id
        1LZZj8e5R0HtDuHVhP6-bAZkVOFLdgE39), section "Ket cau phan tren".
"""
import numpy as np


def poly_props(pts):
    """Area, centroid z and I about horizontal centroidal axis of a closed
    polygon (counter-clockwise), via Green's theorem."""
    p = np.asarray(pts, float)
    x, z = p[:, 0], p[:, 1]
    x1, z1 = np.roll(x, -1), np.roll(z, -1)
    cr = x * z1 - x1 * z
    A = 0.5 * cr.sum()
    Sz = (cr * (z + z1)).sum() / 6.0          # first moment about z=0 (int z dA)
    Izz0 = (cr * (z * z + z * z1 + z1 * z1)).sum() / 12.0   # int z^2 dA
    return A, Sz, Izz0


def box_props(outer, hole):
    """Full (both halves) A, z_c (from soffit), I_horizontal for a half outer
    polygon and half hole polygon, both CCW, both touching x=0."""
    Ao, So, Io = poly_props(_mirror(outer))
    Ah, Sh, Ih = poly_props(_mirror(hole))
    A = Ao - Ah
    S = So - Sh
    I0 = Io - Ih
    zc = S / A
    return A, zc, I0 - A * zc ** 2


def _mirror(half):
    """Build full CCW polygon from a half polygon given CCW on x>=0 side,
    starting at (0, z_bottom) and ending at (0, z_top)."""
    h = np.asarray(half, float)
    left = h[::-1].copy()
    left[:, 0] *= -1
    full = np.vstack([h, left[1:-1]])
    return full


# ---------------------------------------------------------------- Cau May
def caumay_mid():
    """Mid-span section, p.3 right drawing (depth 2400 at axis, 2% crossfall,
    flange tip 250, flange root 550 at x=2.999, webs 400 normal (slope 1:8),
    bottom width 5550, bottom slab 250, bottom haunch 300x300,
    top slab 272 at axis over 2194, haunch 1500 to 550 at inner web face)."""
    H = 2.400
    top = lambda x: H - 0.02 * x
    xb = 5.550 / 2
    xj = xb + 0.224                       # outer web top (2851 cantilever)
    zj = top(xj) - 0.550
    outer = [(0, 0), (xb, 0), (xj, zj), (5.850, top(5.850) - 0.250),
             (5.850, top(5.850)), (0, H)]
    tw = 0.400 * np.sqrt(1 + 1 / 64)      # horizontal web thickness
    xin = lambda z: xb + z / 8 - tw
    ts = 0.250
    zt_c = H - 0.272                      # top-slab soffit at axis
    x_h = 2.194 / 2
    x_w = x_h + 1.500
    zt_w = top(x_w) - 0.550
    hole = [(0, ts), (xin(ts + 0.3) - 0.3, ts), (xin(ts + 0.3), ts + 0.3),
            (xin(zt_w), zt_w), (x_h, zt_c), (0, zt_c)]
    return box_props(outer, hole), dict(xin_top=xin(zt_w), x_w=x_w)


def caumay_pier():
    """Pier-face section, p.3 left drawing (depth 5400 at axis = 5283+117,
    flange root 550 at x=2.999, webs 600 normal, bottom width 4800,
    bottom slab 800, haunch 300x300, top slab 472 at axis over 1752, haunch
    1500 to 710 at inner web face)."""
    H = 5.400
    top = lambda x: H - 0.02 * x
    xb = 4.800 / 2
    xj = xb + 0.599
    zj = top(xj) - 0.550
    outer = [(0, 0), (xb, 0), (xj, zj), (5.850, top(5.850) - 0.250),
             (5.850, top(5.850)), (0, H)]
    tw = 0.600 * np.sqrt(1 + 1 / 64)
    xin = lambda z: xb + z / 8 - tw
    ts = 0.800
    zt_c = H - 0.472
    x_h = 1.752 / 2
    x_w = x_h + 1.500
    zt_w = top(x_w) - 0.710
    hole = [(0, ts), (xin(ts + 0.3) - 0.3, ts), (xin(ts + 0.3), ts + 0.3),
            (xin(zt_w), zt_w), (x_h, zt_c), (0, zt_c)]
    return box_props(outer, hole), dict(xin_top=xin(zt_w), x_w=x_w)


# --------------------------------------------------------------- Thai Binh
def thaibinh(H, b_bot, t_web, t_bot, t_root=0.55, t_tip=0.22, t_top=0.25,
             web_slope=0.24, haunch_w=1.5, bot_haunch=0.3):
    """Thai Binh single-cell box with inclined webs.
    Given in TB design note: top width 11.7, depth H (2.0 mid / 4.0 pier),
    bottom width b_bot (5.759 mid / 4.8 pier), web t_web (0.25 mid / 0.60
    near pier), flange tip min 0.22, top slab inside box 0.25, 2% crossfall.
    NOT given ([NEED VALUE], analogue values from Cau May drawing):
    t_bot (bottom slab), t_root (flange root, CM: 0.55), top haunch width
    (CM: 1.5), bottom haunch (CM: 0.3x0.3).  web_slope (horizontal per
    vertical) = 0.24 follows from the two bottom widths if the web/flange
    junction is at a fixed x (as in the CM drawing): (5.759-4.8)/2/(4.0-2.0).
    """
    top = lambda x: H - 0.02 * x
    xb = b_bot / 2
    # web/flange junction (outer face meets flange soffit)
    # x_j = xb + s*z_j, z_j = top(x_j) - t_root  -> solve linear
    s = web_slope
    xj = (xb + s * (H - t_root)) / (1 + s * 0.02)
    zj = top(xj) - t_root
    outer = [(0, 0), (xb, 0), (xj, zj), (5.850, top(5.850) - t_tip),
             (5.850, top(5.850)), (0, H)]
    tw = t_web * np.sqrt(1 + s * s)
    xin = lambda z: xb + s * z - tw
    zt_c = H - t_top
    # inner web top: where inner web face meets top-slab soffit (thickness t_root)
    # z = top(x) - t_root, x = xin(z)
    zt_w = (top(xb - tw) - t_root) / (1 + 0.02 * s)
    zt_w = top(xin(zt_w)) - t_root
    x_w = xin(zt_w)
    x_h = max(x_w - haunch_w, 0.2)
    zt_h = top(x_h) - t_top
    hole = [(0, t_bot), (xin(t_bot + bot_haunch) - bot_haunch, t_bot),
            (xin(t_bot + bot_haunch), t_bot + bot_haunch),
            (x_w, zt_w), (x_h, zt_h), (0, zt_c)]
    return box_props(outer, hole)


if __name__ == "__main__":
    for name, f, ref in [("CM mid", caumay_mid, (7.233, 1.572, 5.482)),
                         ("CM pier face", caumay_pier, (14.437, 3.053, 59.612))]:
        (A, zc, I), _ = f()
        print(f"{name:14s} A={A:7.3f} (ref {ref[0]})  z(-)={zc:6.3f} (ref {ref[1]})"
              f"  I={I:7.3f} (ref Iyy {ref[2]})  err_I={100*(I/ref[2]-1):+.1f}%")
    for tb in (0.21, 0.25):
        A, zc, I = thaibinh(2.0, 5.759, 0.25, tb)
        print(f"TB mid t_bot={tb}: A={A:.3f} zc={zc:.3f} I={I:.3f}")
    for tb in (0.59, 0.80):
        A, zc, I = thaibinh(4.0, 4.8, 0.60, tb)
        print(f"TB pier t_bot={tb}: A={A:.3f} zc={zc:.3f} I={I:.3f}")
