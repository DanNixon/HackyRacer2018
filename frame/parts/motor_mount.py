#!/usr/bin/env python3

import solid as sp
import solid.utils as spu

from frame.utils import entrypoint, place_at_centres
import frame.parts.motor as motor

plate_thickness = 6

mount_holes_offset = 70
mount_holes_distance = 80
mount_holes_diameter = 6

lower_extent = mount_holes_offset + 15


def projection():
    d = motor.body_diameter + 10
    outer = sp.hull()(
        sp.square([d, d], center=True),
        spu.back(lower_extent - 5)(sp.square([d, 10], center=True)),
    )

    mounting_holes = spu.back(mount_holes_offset)(
        place_at_centres(
            [mount_holes_distance, 0], sp.circle(d=mount_holes_diameter)
        )
    )

    return outer - motor.mountable_face() - mounting_holes


def volume():
    return sp.linear_extrude(plate_thickness)(projection())


if __name__ == '__main__':
    entrypoint.main(projection())
