import solid as sp

from .dimensions import panel_corner_radius, mounting_hole_diameter


def projection(points):
    panel = sp.hull()(
        [
            sp.translate(p)(sp.circle(r=panel_corner_radius, segments=32))
            for p in points
        ]
    )

    mounting_holes = sp.union()(
        [
            sp.translate(p)(sp.circle(d=mounting_hole_diameter, segments=16))
            for p in points
        ]
    )

    return panel - mounting_holes
