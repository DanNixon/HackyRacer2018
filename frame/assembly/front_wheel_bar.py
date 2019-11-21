import solid as sp
import solid.utils as spu

from frame.assembly import wheel_centre_distance
from frame.materials import box_section
from frame.utils import entrypoint

bar_thickness = 5

bar_length = wheel_centre_distance - (100 * 2) - 70

inner_height = 35
inner_depth = 40


def assembly():
    bar = sp.rotate([0, 90,
                     0])(box_section.volume(length=bar_length, center=True))

    # TODO: design this in 2D and extrude
    _mount = spu.right((bar_length + bar_thickness) / 2.)(
        sp.union()(
            sp.cube(
                [
                    bar_thickness, box_section.default_size[0], inner_height +
                    (2. * bar_thickness)
                ],
                center=True
            ),
            [
                sp.translate([0, -box_section.default_size[0] / 2., d])(
                    sp.cube(
                        [
                            inner_depth + bar_thickness,
                            box_section.default_size[0], bar_thickness
                        ]
                    )
                )
                for d in [-inner_height / 2 - bar_thickness, inner_height / 2.]
            ],
        )
    )
    _mounts = [sp.rotate([0, 0, a])(_mount) for a in [0, 180]]

    return sp.union()(
        sp.color(spu.Red)(bar),
        sp.color(spu.Green)(_mounts),
    )


if __name__ == '__main__':
    entrypoint.main(assembly())
