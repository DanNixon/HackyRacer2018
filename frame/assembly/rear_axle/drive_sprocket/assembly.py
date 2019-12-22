#!/usr/bin/env python3

import solid as sp
import solid.utils as spu

from frame.assembly import axle_diameter
from frame.utils import entrypoint

from . import mount
from . import sprocket


def assembly():
    return sp.union()(
        sp.color('red')(mount.volume()),
        sp.color('green')(spu.down(sprocket.thickness)(sprocket.volume())),
    )


if __name__ == '__main__':
    entrypoint.main(assembly())
