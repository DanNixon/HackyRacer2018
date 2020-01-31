import solid as sp
import solid.utils as spu

import frame.assembly.lower_frame as lower_frame
import frame.assembly.seat_mount as seat_mount
import frame.assembly.brake_pedal as brake_pedal
from frame.materials import box_section
from frame.utils import entrypoint

from .dimensions import inner, inner_length, rear_axle_position, outer_length, max_outer_dimensions
from . import bumpers, electronics_tray, motor, rear_axle, rear_axle_bearing, steering


def assembly():
    magic_1 = inner_length - 100.

    return sp.union()(
        sp.color('red')(lower_frame.assembly()),
        sp.color('green')(sp.translate((0, 180, 160))(seat_mount.assembly())),
        sp.color('blue')(
            sp.translate(
                (
                    0, rear_axle_position, -(box_section.default_size[0] / 2.) -
                    rear_axle_bearing.shaft_height
                )
            )(rear_axle.assembly())
        ),
        sp.color('magenta')(
            sp.translate((inner + (box_section.default_size[0] / 2.), 300, 0))(
                sp.rotate((90, 0, -90))(motor.assembly())
            )
        ),
        sp.color('pink')(
            spu.forward(inner_length + box_section.default_size[0])(
                sp.rotate((90, 0, 180))(bumpers.front.assembly())
            ),
            spu.back(box_section.default_size[1])(
                sp.rotate((90, 0, 0))(bumpers.rear.assembly())
            ),
        ),
        sp.color('lime')(
            sp.translate(
                (-inner + (box_section.default_size[0] / 2.) + 1., magic_1, 0)
            )(brake_pedal.assembly())
        ),
        sp.color('orange')(
            sp.translate((0, 1000, 0))(
                sp.rotate((45, 0, 0))(steering.assembly())
            )
        ),
        sp.color('brown')(
            sp.translate((0, 75, box_section.default_size[0] / 2.))(
                electronics_tray.assembly()
            )
        ),
    )


def size_check():
    return sp.union()(
        assembly(),
        sp.translate((0., 600., 100.))(
            sp.color((1., 1., 1., 0.4))(
                sp.cube(max_outer_dimensions, center=True)
            )
        ),
    )


if __name__ == '__main__':
    # entrypoint.main(assembly())
    entrypoint.main(size_check())
