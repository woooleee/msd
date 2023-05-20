# import c as const
import numpy as np
import math

def distance_decay(value, distance) -> float:
    """
    :param value: value such as population or od activity data
    :param distance: distance in meter
    :return processed_value
    """
    km_distance = distance / 1000
    distance_decay_index = math.exp(-km_distance)
    return value * distance_decay_index

def sphere_distance(addr0: (float, float), addr1: (float, float)) -> float:
    """
    Distance is sphere distance - using haversine formula
    haversine formula
    a = sin^2 (delta(latitute) / 2) + cos latitude1 * cos latitude 2 * sin^2(delta longitude / 2)
    c = 2 * atan2 (sqrt(a), sqrt(1 - a))
    d = Earth Radius * c
    
    :param addr0: x, y coordinate of one point
    :param addr1: x, y coordinate of the other point
    :return distance: distance in meter(between addr0 and addr1)
    """
    # convert coordinate to radian
    lat_trans0, lat_trans1 = (addr0[0] * np.pi / 180,
                              addr1[0] * np.pi / 180)
    d_lat = (addr1[0] - addr0[0]) * np.pi / 180
    d_lmb = (addr1[1] - addr0[1]) * np.pi / 180

    a = (
            (np.sin(d_lat / 2)) ** 2 +
            (np.cos(lat_trans0) * np.cos(lat_trans1) * (np.sin(d_lmb / 2) ** 2))
    )
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))
    return const.EARTH_RADIUS_METER * c  # meter




