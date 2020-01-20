import solid as sp
import solid.utils as spu

from frame.utils import entrypoint, place_at_centres

from . import motor

plate_width = 120.
plate_thickness = 10.

mount_holes_offset = 70.
mount_holes_distance = 60.
mount_slots_size = (40., 6.)

lower_extent = mount_holes_offset + 15.


def mounting_slot():
    return sp.hull()(
        place_at_centres(
            (mount_slots_size[0] / 2., 0.), sp.circle(d=mount_slots_size[1])
        )
    )


def projection():
    d = motor.body_diameter + 10.
    outer = sp.hull()(
        sp.square((plate_width, d), center=True),
        spu.back(lower_extent - 5.)(sp.square((plate_width, 10.), center=True)),
    )

    mounting_holes = spu.back(mount_holes_offset)(
        place_at_centres((mount_holes_distance, 0.), mounting_slot())
    )

    return outer - motor.mountable_face() - mounting_holes


def volume():
    return sp.linear_extrude(plate_thickness)(projection())


if __name__ == '__main__':
    entrypoint.main(projection())
