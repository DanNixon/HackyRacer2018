import solid as sp
import solid.utils as spu

from frame.assembly import outer, outer_length, inner, inner_length, front_wheel_bar
from frame.materials import box_section, plate

plate_thickness = 3
front_bumper_depth = 150

#   translate([0, outer_length + box_section_outer[0] / 2, 0])
#   {
#     rotate([0, 0, 90])
#     {
#       BoxSection(
#           name="lower_frame/inner_mid_x_bar",
#           col="cyan",
#           outer=box_section_outer,
#           length=inner * 2 - box_section_outer[0],
#           center=true);

#       for (a = [0, 180])
#       {
#         rotate([0, 0, a])
#         {
#           translate([0, -outer - box_section_outer[0] / 2, 0])
#           {
#             BoxSection(
#                 name="lower_frame/outer_mid_x_bar",
#                 col="yellow",
#                 outer=box_section_outer,
#                 length=outer - inner,
#                 center=false);
#           }
#         }
#       }
#     }
#   }

#   translate([0, -box_section_outer[0] / 2, 0])
#   {
#     rotate([0, 0, 90])
#     {
#       BoxSection(
#           name="lower_frame/rear_x_bar",
#           col="magenta",
#           outer=box_section_outer,
#           length=outer * 2 + box_section_outer[0],
#           center=true);
#     }
#   }

#   /* Floor panel */
#   translate([-inner-box_section_outer[0]/2, -box_section_outer[0], -(box_section_outer[1] + plate_thickness) / 2])
#   {
#     AssemblyInstruction(
#         "lower_frame/floor_panel",
#         "Clearence holes drilled into lower floor plate");

#     AssemblyInstruction(
#         "lower_frame/floor_panel",
#         "Tap threads into lower frame box section");

#     Plate(
#         name="lower_frame/floor_panel",
#         col="gray",
#         size=[inner * 2 + box_section_outer[0], inner_length + 2*box_section_outer[0], plate_thickness],
#         center=false);
#   }


def assembly():
    outer_bars = sp.rotate([90, 0, 0])(
        [
            spu.left(d)(
                box_section.volume(outer_length, center=False, color=spu.Red)
            ) for d in [-outer, outer]
        ]
    )

    inner_bars = sp.rotate([90, 0, 0])(
        [
            spu.left(d)(
                box_section.volume(inner_length, center=False, color=spu.Green)
            ) for d in [-inner, inner]
        ]
    )

    front_bumper = spu.back(inner_length + box_section.default_size[0] / 2.)(
        [
            sp.translate([d, -box_section.default_size[0] / 2., 0])(
                sp.rotate([90, 0, 0])(
                    box_section.volume(
                        front_bumper_depth - box_section.default_size[0],
                        center=False,
                        color=spu.Blue
                    )
                )
            ) for d in [-inner, inner]
        ],
        spu.back(front_bumper_depth)(
            sp.rotate([0, 90, 0])(
                box_section.volume(
                    inner * 2. + box_section.default_size[0],
                    center=True,
                    color='orange'
                )
            )
        ),
    )

    front_bar = spu.back(inner_length + box_section.default_size[0] / 2.)(
        sp.color('purple')(front_wheel_bar.assembly())
    )

    return sp.union()(
        outer_bars,
        inner_bars,
        front_bumper,
        front_bar,
    )


if __name__ == '__main__':
    print(sp.scad_render(assembly()))
