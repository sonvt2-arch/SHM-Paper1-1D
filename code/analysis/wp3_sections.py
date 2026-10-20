"""Cross-section properties of the Mây Bridge (Cau May) box girder.

Polygon (Green's theorem) section properties for single-cell box sections.
Coordinates: half-section (x >= 0, symmetric about the bridge axis), z upward
from the soffit at the axis, units m.  Vertical-bending I = I about the
horizontal centroidal axis.

Source: load-rating report of the Mây Bridge main girder (supplied by the
consultancy, not public), p. 3 (cross-section drawings, mm) and p. 5
(section-property table).  The polygon routine is checked against that table.
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


if __name__ == "__main__":
    for name, f, ref in [("CM mid", caumay_mid, (7.233, 1.572, 5.482)),
                         ("CM pier face", caumay_pier, (14.437, 3.053, 59.612))]:
        (A, zc, I), _ = f()
        print(f"{name:14s} A={A:7.3f} (ref {ref[0]})  z(-)={zc:6.3f} (ref {ref[1]})"
              f"  I={I:7.3f} (ref Iyy {ref[2]})  err_I={100*(I/ref[2]-1):+.1f}%")
