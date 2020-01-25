import solid as sp

from . import bearing


def bearing_holes():
    return sp.union()(
        bearing.mounting_holes(),
        sp.circle(d=22., segments=32),
    )
