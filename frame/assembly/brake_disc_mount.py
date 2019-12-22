#!/usr/bin/env python3

import solid as sp
import solid.utils as spu

from frame.assembly import axle_diameter
from frame.utils import entrypoint
import frame.parts.brake_disc as brake_disc
import frame.parts.brake_disc_mount as brake_disc_mount


def assembly():
    return sp.union()(
        sp.color('red')(brake_disc_mount.volume()),
        sp.color('green')(spu.down(brake_disc.thickness)(brake_disc.volume())),
    )


if __name__ == '__main__':
    entrypoint.main(assembly())
