#!/usr/bin/env python3

import solid as sp
import solid.utils as spu

from frame.utils import bom, place_at_centres

shaft_diameter = 18
shaft_height = 30

width = 40

base_length = 125
base_height = 15

mounting_hole_diameter = 14
mounting_hole_centres = 100


@bom.part('Rear Axle Bearing')
def volume():
    base = spu.up(base_height / 2.)(
        sp.cube([width, base_length, base_height], center=True)
    )

    mounting_holes = spu.down(1)(
        place_at_centres(
            [0, mounting_hole_centres],
            sp.cylinder(d=mounting_hole_diameter, h=base_height + 2)
        )
    )

    base -= mounting_holes

    bearing = spu.up(shaft_height)(
        sp.rotate([0, 90, 0])(
            sp.cylinder(d=60, h=width, center=True) -
            sp.cylinder(d=shaft_diameter, h=width + 1, center=True)
        )
    )

    return sp.union()(
        base,
        bearing,
    )


if __name__ == '__main__':
    print(sp.scad_render(volume()))
