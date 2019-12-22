#!/usr/bin/env python3

import solid as sp
import solid.utils as spu

from frame.materials import box_section
from frame.utils import entrypoint
from frame.primitives import drilled_hole

pedal_width = 80.

pedal_side_length = 100.
cable_side_length = 50.

pivot_hole_diameter = 8.


def assembly():
    main = sp.translate(
        [box_section.default_size[0] / 2., 0, -cable_side_length]
    )(box_section.volume(length=pedal_side_length + cable_side_length)
     ) - sp.rotate([0, 90, 0])(drilled_hole.volume(pivot_hole_diameter))

    pedal = sp.translate(
        [
            0, -box_section.default_size[1],
            pedal_side_length - box_section.default_size[1] / 2.
        ]
    )(
        sp.rotate([0, 90,
                   0])(box_section.volume(length=pedal_width, center=True))
    )

    return sp.union()(
        sp.color('red')(main),
        sp.color('green')(pedal),
    )


if __name__ == '__main__':
    entrypoint.main(assembly())
