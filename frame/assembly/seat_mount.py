#!/usr/bin/env python3

import solid as sp
import solid.utils as spu

from frame.utils import split_centers, place_at_centres
from frame.primitives.drilled_hole import volume as drilled_hole
from frame.materials import box_section, plate
from frame.assembly import outer
from frame.utils import entrypoint

seat_depth = 280

seat_mount_centres = [300, 200]
seat_mount_hole_diameter = 8


def assembly():
    x_bars = sp.rotate([0, 90, 0])(
        [
            spu.back(d)(
                box_section.volume(
                    length=outer * 2. + box_section.default_size[0],
                    center=True
                )
            ) for d in split_centers(seat_depth)
        ]
    )

    y_bars = sp.rotate([90, 0, 0])(
        [
            spu.left(d)(
                box_section.volume(
                    length=seat_depth - box_section.default_size[0],
                    center=True
                )
            ) for d in [
                -outer, outer, -seat_mount_centres[0] /
                2, seat_mount_centres[0] / 2
            ]
        ]
    )

    frame = sp.union()(
        sp.color('red')(x_bars),
        sp.color('green')(y_bars),
    )

    holes = place_at_centres(
        seat_mount_centres, drilled_hole(seat_mount_hole_diameter)
    )

    return frame - holes


if __name__ == '__main__':
    entrypoint.main(assembly())
