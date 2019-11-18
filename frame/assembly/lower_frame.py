import solid as sp
import solid.utils as spu

from frame.assembly import outer, outer_length, inner, inner_length, front_wheel_bar
from frame.materials import box_section, plate

plate_thickness = 3
front_bumper_depth = 150


def assembly():
    outer_bars = sp.rotate([-90, 0, 0])(
        [
            spu.left(d)(
                box_section.volume(outer_length, center=False, color=spu.Red)
            ) for d in [-outer, outer]
        ]
    )

    inner_bars = sp.rotate([-90, 0, 0])(
        [
            spu.left(d)(
                box_section.volume(inner_length, center=False, color=spu.Green)
            ) for d in [-inner, inner]
        ]
    )

    front_bumper = spu.forward(inner_length + box_section.default_size[0] / 2.)(
        [
            sp.translate([d, box_section.default_size[0] / 2., 0])(
                sp.rotate([-90, 0, 0])(
                    box_section.volume(
                        front_bumper_depth - box_section.default_size[0],
                        center=False,
                        color=spu.Blue
                    )
                )
            ) for d in [-inner, inner]
        ],
        spu.forward(front_bumper_depth)(
            sp.rotate([0, 90, 0])(
                box_section.volume(
                    inner * 2. + box_section.default_size[0],
                    center=True,
                    color='orange'
                )
            )
        ),
    )

    front_bar = spu.forward(inner_length + box_section.default_size[0] / 2.)(
        sp.color('purple')(front_wheel_bar.assembly())
    )

    mid_bars = spu.forward(outer_length + box_section.default_size[0] / 2.)(
        sp.rotate([0, 90, 0])(
            box_section.volume(
                inner * 2. - box_section.default_size[0],
                center=True,
                color=spu.Cyan
            ),
            [
                sp.rotate([0, a, 0])(
                    spu.up(inner + box_section.default_size[0] / 2.)(
                        box_section.volume(
                            outer - inner, center=False, color=spu.Cyan
                        )
                    )
                ) for a in [0, 180]
            ],
        ),
    )

    rear_bar = spu.back(box_section.default_size[0] / 2.)(
        sp.rotate([0, 90, 0])(
            box_section.volume(
                outer * 2. + box_section.default_size[0],
                center=True,
                color=spu.Magenta
            )
        )
    )

    # Clearence holes drilled into lower floor plate
    # Tap threads into lower frame box section
    floor_panel = sp.translate(
        [
            -inner - box_section.default_size[0] / 2.,
            -box_section.default_size[0],
            -(box_section.default_size[1] / 2.) - plate_thickness
        ]
    )(
        plate.volume(
            size=[
                inner * 2. + box_section.default_size[0],
                inner_length + 2. * box_section.default_size[0]
            ],
            thickness=plate_thickness,
            center=False
        )
    )

    return sp.union()(
        outer_bars,
        inner_bars,
        front_bumper,
        front_bar,
        mid_bars,
        rear_bar,
        floor_panel,
    )


if __name__ == '__main__':
    print(sp.scad_render(assembly()))
