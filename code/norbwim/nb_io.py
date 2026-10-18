"""Readers for the NOR-BWIM figshare dataset (doi:10.7294/26880898.v1).

Data are treated as untrusted text: only parsed numerically, never executed.
Paths are passed explicitly; nothing is imported from the data directory.
"""
import os
import numpy as np
import pandas as pd

DATA = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "data",
                                    "public", "norbwim_figshare26880898"))
# Raw-to-microstrain factor used by the authors in mainSmartRoadBridgeNORBWIM.mlx:
#   Test1_st40 = (-521.2*521.2*0.001) * A.st40(...)
GAIN = -521.2 * 521.2 * 0.001


def _cache(name):
    d = os.path.join(os.path.dirname(__file__), "cache")
    os.makedirs(d, exist_ok=True)
    return os.path.join(d, name)


def load_datawed():
    """DataWed.csv: 200 Hz, columns st40, st36, st31, st34 (Trucks 3 and 4, 2020-09-30).
    Row index i (0-based) corresponds to MATLAB timetable row i+1."""
    c = _cache("datawed.pkl")
    if os.path.exists(c):
        return pd.read_pickle(c)
    df = pd.read_csv(os.path.join(DATA, "DataWed.csv"), encoding="utf-8-sig", low_memory=False)
    df["Time"] = pd.to_datetime(df["Time"], format="ISO8601")
    df.to_pickle(c)
    return df


def load_strains200():
    """Strains200Hz.dat (TOA5 logger file, 4 header lines), same channels, longer record."""
    c = _cache("strains200.pkl")
    if os.path.exists(c):
        return pd.read_pickle(c)
    df = pd.read_csv(os.path.join(DATA, "Strains200Hz.dat"), skiprows=[0, 2, 3])
    df = df.rename(columns={"TIMESTAMP": "Time"})
    df["Time"] = pd.to_datetime(df["Time"], format="ISO8601")
    df.to_pickle(c)
    return df


def load_bcsv():
    """B.csv: 100 Hz, Column5 = st40 (Trucks 1 and 2, 2020-09-10)."""
    c = _cache("bcsv.pkl")
    if os.path.exists(c):
        return pd.read_pickle(c)
    df = pd.read_csv(os.path.join(DATA, "B.csv"))
    df["Column1"] = pd.to_datetime(df["Column1"], format="ISO8601")
    df.to_pickle(c)
    return df


def load_allstrain():
    """AllStrainData_construction trucks.dat: 100 Hz, 12 unnamed channels, 2020-09-10."""
    c = _cache("allstrain.pkl")
    if os.path.exists(c):
        return pd.read_pickle(c)
    df = pd.read_csv(os.path.join(DATA, "AllStrainData_construction trucks.dat"),
                     header=None)
    df.columns = ["Time"] + [f"ch{k}" for k in range(1, df.shape[1])]
    df["Time"] = pd.to_datetime(df["Time"], format="ISO8601")
    df.to_pickle(c)
    return df


def load_txt(name):
    """One value per line (model-generated or extracted run files)."""
    return np.loadtxt(os.path.join(DATA, name))
