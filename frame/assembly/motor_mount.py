import solid as sp
import solid.utils as spu

from frame.assembly import axle_diameter
from frame.utils import entrypoint, place_at_centres
import frame.parts.motor as motor

plate_thickness = 6

mount_holes_offset = 70
mount_holes_distance = 80
mount_holes_diameter = 6

lower_extent = mount_holes_offset + 15


def motor_mount_projection():
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


def motor_mount_volume():
    return sp.linear_extrude(plate_thickness)(motor_mount_projection())


def assembly():
    return spu.forward(mount_holes_offset)(
        sp.union()(
            sp.color('red')(spu.down(plate_thickness)(motor_mount_volume())),
            sp.color('green')(sp.rotate([180, 0, 0])(motor.volume())),
        )
    )


if __name__ == '__main__':
    # entrypoint.main(assembly())
    entrypoint.main(motor_mount_projection())
