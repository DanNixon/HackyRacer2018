#!/usr/bin/env python3

import solid as sp
import solid.utils as spu

from frame.utils import bom, place_at_centres

body_dimensions = [45, 85, 23]
mounting_hole_centres = [39, 79]


@bom.part('VESC')
def volume():
    holes = spu.down(-1)(
        place_at_centres(
            mounting_hole_centres, sp.cylinder(d=4, h=body_dimensions[2] + 2)
        )
    )

    return spu.up(body_dimensions[2] / 2
                 )(sp.cube(body_dimensions, center=True)) - holes


if __name__ == '__main__':
    print(sp.scad_render(volume()))
