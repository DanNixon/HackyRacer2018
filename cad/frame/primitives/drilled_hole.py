import solid as sp


def projection(diameter):
    return sp.circle(d=diameter, segments=32)


def volume(diameter):
    return sp.linear_extrude(1000, center=True)(projection(diameter))
