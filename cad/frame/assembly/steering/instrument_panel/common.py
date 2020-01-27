import solid as sp

from frame.utils import place_at_centres

from .dimensions import size, corner_radius, mounting_hole_corner_offset


def place_mounting_holes(obj):
    return place_at_centres(
        [d - (mounting_hole_corner_offset * 2.) for d in size], obj
    )


def outer_projection(mount_hole_diameter, segments=32):
    p = sp.hull()(
        place_at_centres(
            [d - (2. * corner_radius) for d in size],
            sp.circle(r=corner_radius, segments=32)
        )
    )

    return p - place_mounting_holes(
        sp.circle(d=mount_hole_diameter, segments=segments)
    )
