import solid as sp
import solid.utils as spu

from frame.utils import bom, entrypoint, place_at_centres

# TODO
body_dimensions = (25., 60., 15.)

# TODO
mounting_hole_centres = (30., 30.)
mounting_hole_diameter = 3.


def holes():
    return place_at_centres(
        mounting_hole_centres, sp.circle(d=mounting_hole_diameter, segments=32)
    )


def projection():
    return sp.square(body_dimensions[:2], center=True)


@bom.part('BEC')
def volume():
    return sp.linear_extrude(body_dimensions[2])(projection())


if __name__ == '__main__':
    entrypoint.main(volume())
