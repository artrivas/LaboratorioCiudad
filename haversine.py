from math import radians, cos, sin, asin, sqrt

def haversine(lat1, lon1, lat2, lon2):
    r = 6371  # Radius of earth in kilometers
    phi1 = radians(lat1)
    phi2 = radians(lat2)
    dphi = radians(lat2 - lat1)
    dlambda = radians(lon2 - lon1)

    a = sin(dphi/2)**2 + cos(phi1)*cos(phi2)*sin(dlambda/2)**2
    res = r * (2*asin(sqrt(a)))

    return res
