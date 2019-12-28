import solid as sp
import solid.utils as spu

from frame.utils import bom, entrypoint, place_at_centres

body_dimensions = (45., 85., 23.)

mounting_hole_centres = (39., 79.)
mounting_hole_diameter = 4.


def holes():
    return place_at_centres(
        mounting_hole_centres, sp.circle(d=mounting_hole_diameter, segments=32)
    )


def projection():
    return sp.square(body_dimensions[:2], center=True) - holes()


@bom.part('VESC')
def volume():
    return sp.linear_extrude(body_dimensions[2])(projection())


if __name__ == '__main__':
    entrypoint.main(volume())
