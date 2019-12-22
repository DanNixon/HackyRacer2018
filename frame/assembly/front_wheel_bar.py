#!/usr/bin/env python3

import solid as sp
import solid.utils as spu

from frame.assembly import wheel_centre_distance
from frame.materials import box_section
from frame.utils import entrypoint, place_at_centres

bar_length = wheel_centre_distance - (100 * 2) - 70

mount_overhang = 50
mount_overlap = 50


def assembly():
    main_bar = sp.rotate([0, 90, 0])(
        box_section.volume(length=bar_length, center=True)
    )

    d = box_section.default_size[0]

    padding_bars = sp.color('green')(
        sp.translate([-bar_length / 2., 0, -d])(
            sp.rotate([0, 90, 0])(
                box_section.volume(length=mount_overlap, center=False)
            )
        )
    )

    mount_bars = sp.color('blue')(
        [
            sp.translate([(-bar_length / 2.) - mount_overhang, 0, z])(
                sp.rotate([0, 90, 0])(
                    box_section.volume(
                        length=mount_overhang + mount_overlap, center=False
                    )
                )
            ) for z in [d, -d * 2.]
        ]
    )

    return sp.union()(
        sp.color('red')(main_bar),
        [sp.rotate([0, 0, a])(
            padding_bars,
            mount_bars,
        ) for a in [0, 180]],
    )


if __name__ == '__main__':
    entrypoint.main(assembly())
