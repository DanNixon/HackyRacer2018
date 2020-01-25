import solid as sp

from frame.utils import bom, entrypoint, place_at_centres

bore = 17.

mounting_hole_diameter = 7.
mounting_hole_centres = 56.

height = 18.


def place_mounting_holes(obj):
    return place_at_centres((mounting_hole_centres, 0), obj)


def mounting_holes():
    return place_mounting_holes(
        sp.circle(d=mounting_hole_diameter, segments=32)
    )


def projection():
    """
    This is an approximation of the body.
    It matches the maximum outer dimensions but does not accurately reflect the profile.
    """
    body = sp.union()(
        sp.circle(d=45., segments=32),
        sp.hull()(
            sp.circle(d=30., segments=32),
            place_mounting_holes(sp.circle(d=15., segments=32)),
        ),
    )
    return body - sp.circle(d=bore, segments=32) - mounting_holes()


@bom.part('Steering Column Bearing')
def volume():
    return sp.linear_extrude(height)(projection())


if __name__ == '__main__':
    entrypoint.main(volume())
