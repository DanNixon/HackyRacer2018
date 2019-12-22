#!/usr/bin/env python3

import solid as sp
import solid.utils as spu

from frame.utils import entrypoint

from . import motor
from . import mount


def assembly():
    return spu.forward(mount.mount_holes_offset)(
        sp.union()(
            sp.color('red')(spu.down(mount.plate_thickness)(mount.volume())),
            sp.color('green')(sp.rotate([180, 0, 0])(motor.volume())),
        )
    )


if __name__ == '__main__':
    entrypoint.main(assembly())
