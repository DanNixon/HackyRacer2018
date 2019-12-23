#!/usr/bin/env python3

import solid as sp
import solid.utils as spu

from frame.utils import place_at_centres
from frame.utils import entrypoint
import frame.parts.wheel as wheel
from frame.assembly.dimensions import axle_diameter, wheel_centre_distance

from . import brake_disc
from . import drive_sprocket

sprocket_pos = 145
brake_disc_pos = 145

axle_length = wheel_centre_distance + 120


def assembly():
    axle = sp.color('red')(
        sp.cylinder(d=axle_diameter, h=axle_length, center=True)
    )

    sprocket_assy = spu.up(sprocket_pos)(
        sp.color('green')(drive_sprocket.assembly())
    )

    brake_disc_assy = spu.down(brake_disc_pos)(
        sp.color('blue')(
            sp.rotate([180, 0, 0])(brake_disc.assembly())
        )
    )

    wheels = [
        sp.rotate([0, a,
                   0])(spu.right(wheel_centre_distance / 2.)(wheel.volume()))
        for a in [0, 180]
    ]

    return sp.union()(
        sp.rotate([0, 90,
                   0])(sp.union()(
                       axle,
                       sprocket_assy,
                       brake_disc_assy,
                   )),
        wheels,
    )


if __name__ == '__main__':
    entrypoint.main(assembly())
