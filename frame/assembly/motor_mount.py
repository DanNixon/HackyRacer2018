#!/usr/bin/env python3

import solid as sp
import solid.utils as spu

from frame.utils import entrypoint
import frame.parts.motor as motor
import frame.parts.motor_mount as motor_mount


def assembly():
    return spu.forward(motor_mount.mount_holes_offset)(
        sp.union()(
            sp.color('red')(spu.down(motor_mount.plate_thickness)(motor_mount.volume())),
            sp.color('green')(sp.rotate([180, 0, 0])(motor.volume())),
        )
    )


if __name__ == '__main__':
    entrypoint.main(assembly())
