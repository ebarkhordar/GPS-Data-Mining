from math import sin, cos, sqrt, atan2, radians
from data_utils.models import Location


def calculate_distance(point1, point2):
    R = 6373.0
    if isinstance(point1, Location) and isinstance(point2, Location):
        lat1 = radians(point1.lat)
        lon1 = radians(point1.long)
        lat2 = radians(point2.lat)
        lon2 = radians(point2.long)
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        distance = R * c
        return distance
