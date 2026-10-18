"""Event fitting and integration for the Smart Road Bridge field records."""
import numpy as np
from scipy.signal import butter, sosfiltfilt
import nb_beam as bm

_M = bm.model(True, 2.0)
_XIL, _IL = bm.moment_il(_M)
_IL = _IL / np.max(np.abs(_IL))


def il_at(x):
    """Normalised moment IL at the sensor; zero off the bridge."""
    return np.interp(x, _XIL, _IL, left=0.0, right=0.0)


def lowpass(y, fs, fc=0.5):
    sos = butter(4, fc / (0.5 * fs), output="sos")
    return sosfiltfilt(sos, y)


def shape(t, t_entry, v, axles, w, direction):
    """Predicted quasi-static global strain shape (compression -> negative)."""
    s = np.zeros_like(t)
    for d, p in zip(axles, w):
        xa = v * (t - t_entry) - d                 # distance travelled from entry abutment
        x = xa if direction > 0 else bm.LTOT - xa
        s += p * il_at(np.where((xa >= 0) & (xa <= bm.LTOT), x, -1.0))
    return -s


def fit_event(t, y, axles, w, vgrid=np.arange(8.0, 32.01, 0.25), t_mid_guess=0.0):
    """Grid fit of direction, speed and entry time to the low-passed record (y in
    microstrain, baseline already roughly removed). Returns dict."""
    best = None
    for direction in (+1, -1):
        xs = bm.X_SENSOR if direction > 0 else bm.LTOT - bm.X_SENSOR
        for v in vgrid:
            Lt = axles[-1]
            for dt in np.arange(-3.0, 3.01, 0.05):
                t_entry = t_mid_guess - (xs + 0.5 * Lt) / v + dt
                s = shape(t, t_entry, v, axles, w, direction)
                A = np.vstack([s, np.ones_like(s), t - t.mean()]).T
                c, res, *_ = np.linalg.lstsq(A, y, rcond=None)
                r = np.sum((A @ c - y) ** 2)
                if best is None or r < best["res"]:
                    best = dict(res=r, direction=direction, v=v, t_entry=t_entry,
                                amp=c[0], t_exit=t_entry + (bm.LTOT + Lt) / v)
    best["r2"] = 1 - best["res"] / np.sum((y - y.mean()) ** 2)
    return best


def integrate(t, y, ta, tb, nbase):
    """Time integral of y over [ta,tb] after removing a linear baseline through the
    means of nbase-second segments before ta and after tb."""
    pre = (t >= ta - nbase) & (t < ta)
    post = (t > tb) & (t <= tb + nbase)
    t1, y1 = t[pre].mean(), y[pre].mean()
    t2, y2 = t[post].mean(), y[post].mean()
    base = y1 + (y2 - y1) * (t - t1) / (t2 - t1)
    m = (t >= ta) & (t <= tb)
    return np.trapezoid(y[m] - base[m], t[m]), y - base
