import solid as sp

from frame.utils import place_at_centres

from .dimensions import size, corner_radius


def place_mounting_holes(obj):
    return place_at_centres([d - 5. for d in size], obj)


def outer_projection():
    p = sp.hull()(
        place_at_centres(
            [d - corner_radius for d in size],
            sp.circle(r=corner_radius, segments=32)
        )
    )

    return p - place_mounting_holes(sp.circle(d=3.1, segments=32))
