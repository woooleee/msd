import pyproj
from pyproj import Transformer
import numpy as np
import warnings; warnings.filterwarnings('ignore')
# ent_xs = ["949303.8677014101"]
# ent_ys = ["1948019.7300865133"]
def coord_tranformation(xs:list, ys:list, p1_type:str, p2_type:str) -> tuple:
    """
    Change coordinate system
    :param xs: numpy array consists of x coords
    :param ys: numpy array consists of y coords
    :param p1_type: input coordinate system information ex) epsg:5179
    :param p2_type: output coordinate system information ex) epsg:4326
    :return np stack of x coords and y coords
    :ref :https://pyproj4.github.io/pyproj/stable/gotchas.html#upgrading-to-pyproj-2-from-pyproj-1
    """
    p1 = pyproj.Proj(init=p1_type)
    p2 = pyproj.Proj(init=p2_type)
    fx, fy = pyproj.transform(p1, p2, xs, ys)
    xs_transformed, ys_transformed = list(fx), list(fy)
    return xs_transformed, ys_transformed