import solid as sp
import solid.utils as spu

from frame.utils import place_at_centres
from frame.assembly import axle_diameter, wheel_centre_distance, brake_disc_mount, drive_sprocket_mount
from frame.utils import entrypoint
import frame.parts.wheel as wheel

sprocket_pos = 145
brake_disc_pos = 150

axle_length = wheel_centre_distance + 120


def assembly():
    axle = sp.color(spu.Red)(
        sp.cylinder(d=axle_diameter, h=axle_length, center=True)
    )

    drive_sprocket = spu.down(sprocket_pos)(
        sp.color(spu.Green)(
            sp.rotate([180, 0, 0])(drive_sprocket_mount.assembly())
        )
    )
    brake_disc = spu.up(brake_disc_pos)(
        sp.color(spu.Blue)(brake_disc_mount.assembly())
    )

    _wheel = spu.right(wheel_centre_distance / 2.)(wheel.volume())
    wheels = [sp.rotate([0, a, 0])(_wheel) for a in [0, 180]]

    return sp.union()(
        sp.rotate([0, 90, 0])(sp.union()(
            axle,
            drive_sprocket,
            brake_disc,
        )),
        wheels,
    )


if __name__ == '__main__':
    entrypoint.main(assembly())
