import solid as sp
import solid.utils as spu

import frame.assembly.lower_frame as lower_frame
import frame.assembly.seat_mount as seat_mount
import frame.assembly.rear_axle as rear_axle
import frame.assembly.front_wheel as front_wheel
import frame.parts.motor as motor
from frame.materials import box_section
from frame.assembly import inner_length, wheel_centre_distance


def assembly():
    return sp.union()(
        sp.color(spu.Red)(lower_frame.assembly()),
        sp.color(spu.Green)(sp.translate([0, 180, 160])(seat_mount.assembly())),
        sp.color(spu.Blue)(sp.translate([0, 180, 25])(rear_axle.assembly())),
        sp.color(spu.Cyan)(
            sp.translate(
                [0, inner_length + box_section.default_size[0] / 2., 0]
            )(
                [
                    sp.rotate([0, 0, a])(
                        spu.right(wheel_centre_distance / 2. - 100)(
                            front_wheel.assembly()
                        )
                    ) for a in [0, 180]
                ]
            )
        ),
        sp.color(spu.Magenta)(
            sp.translate([130, 300, 75])(sp.rotate([0, 90, 0])(motor.volume()))
        ),
    )


if __name__ == '__main__':
    print(sp.scad_render(assembly()))
