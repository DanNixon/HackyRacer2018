import itertools

import solid as sp
import solid.utils as spu

body_dimensions = [45, 85, 23]
mounting_hole_centres = [39, 79]


def vesc():
    _x = [-mounting_hole_centres[0] / 2, mounting_hole_centres[0] / 2]
    _y = [-mounting_hole_centres[1] / 2, mounting_hole_centres[1] / 2]

    holes = [
        sp.translate([x, y, -1])(sp.cylinder(d=4, h=body_dimensions[2] + 2))
        for x, y in itertools.product(_x, _y)
    ]

    return spu.up(body_dimensions[2] / 2
                  )(sp.cube(body_dimensions, center=True)) - holes


if __name__ == '__main__':
    print(sp.scad_render(vesc()))
