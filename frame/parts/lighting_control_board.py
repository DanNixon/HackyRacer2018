import solid as sp
import solid.utils as spu

from frame.utils import bom, place_at_centres

body_dimensions = [60, 40]
thickness = 2
mounting_hole_centres = [56, 36]


def projection():
    holes = place_at_centres(mounting_hole_centres, sp.circle(d=2))

    return sp.square(body_dimensions, center=True) - holes


@bom.part('Lighting Control Board')
def volume():
    return sp.linear_extrude(thickness)(projection())


if __name__ == '__main__':
    print(sp.scad_render(volume()))
