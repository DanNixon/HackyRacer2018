import solid as sp
import solid.utils as spu

from frame.assembly.dimensions import axle_diameter
from frame.materials import round_bar
from frame.utils import entrypoint

from . import instrument_panel, throttle, lower_mount, lower_mount_arm, mount, wheel
from .dimensions import column_length


def assembly():
    column = round_bar.volume(diameter=axle_diameter, length=column_length)

    return sp.union()(
        spu.up(column_length)(
            spu.up(wheel.plate_thickness / 2.)(
                sp.color('red')(wheel.volume()),
                spu.up(wheel.plate_thickness / 2.)(
                    sp.color('green')(instrument_panel.assembly())
                ),
                sp.translate((150, 80))(
                    sp.rotate((0., 60., 0.))(
                        sp.color('blue')(throttle.assembly())
                    )
                ),
            ),
            sp.rotate((0, 180, 0))(sp.color('cyan')(mount.volume())),
        ),
        sp.color('magenta')(column),
        sp.rotate((0, 0, 180))(
            sp.color('orange')(lower_mount.volume()),
            sp.color('pink')(
                spu.down(lower_mount_arm.thickness)(lower_mount_arm.volume())
            ),
        ),
    )


if __name__ == '__main__':
    entrypoint.main(assembly())
