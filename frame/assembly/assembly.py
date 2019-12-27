import solid as sp
import solid.utils as spu

import frame.assembly.lower_frame as lower_frame
import frame.assembly.seat_mount as seat_mount
import frame.assembly.front_wheel as front_wheel
import frame.assembly.brake_pedal as brake_pedal
from frame.parts import rear_axle_bearing
from frame.materials import box_section
from frame.utils import entrypoint

from .dimensions import inner, inner_length, wheel_centre_distance, rear_axle_position, outer_length, front_bumper_depth
from . import bumpers, motor, rear_axle, steering


def assembly():
    magic_1 = outer_length + 150.

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
        sp.color('cyan')(
            sp.translate(
                (0, inner_length + box_section.default_size[0] / 2., 0)
            )(
                [
                    sp.rotate((0, 0, a))(
                        spu.right(wheel_centre_distance / 2. - 100)(
                            front_wheel.assembly()
                        )
                    ) for a in (0, 180)
                ]
            )
        ),
        sp.color('magenta')(
            sp.translate((inner + box_section.default_size[0] / 2., 300, 0))(
                sp.rotate((90, 0, -90))(motor.assembly())
            )
        ),
        sp.color('pink')(
            spu.forward(
                inner_length + front_bumper_depth + box_section.default_size[0]
            )(sp.rotate((90, 0, 180))(bumpers.front.assembly())),
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
            sp.translate((0, 950, 0))(
                sp.rotate((45, 0, 0))(steering.assembly())
            )
        ),
    )


if __name__ == '__main__':
    entrypoint.main(assembly())
