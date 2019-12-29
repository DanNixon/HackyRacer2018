import solid as sp
import solid.utils as spu

from frame.utils import bom, place_at_centres

# TODO
body_dimensions = (50., 40., 2.)

# TODO
mounting_hole_centres = (40., 30.)
mounting_hole_diameter = 2.2


def holes():
    return place_at_centres(
        mounting_hole_centres, sp.circle(d=mounting_hole_diameter, segments=16)
    )


def projection():
    return sp.square(body_dimensions[:2], center=True) - holes()


@bom.part('Arduino UNO')
def volume():
    return sp.linear_extrude(body_dimensions[2])(projection())


if __name__ == '__main__':
    print(sp.scad_render(volume()))
