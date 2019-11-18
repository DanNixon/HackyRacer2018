import solid as sp
import solid.utils as spu

from frame.assembly import wheel_centre_distance

bar_thickness = 5

bar_length = wheel_centre_distance - (100 * 2) - 70

inner_height = 35
inner_depth = 40

# rotate([0, 0, 90])
# {
#   BoxSection(
#       name="lower_frame/front_wheel_x_bar",
#       col="red",
#       outer=box_section_outer,
#       length=bar_length,
#       center=true);
# }

# color("green")
# {
#   for(a = [0, 180])
#   {
#     rotate([0, 0, a])
#     {
#       translate([(bar_length + bar_thickness) / 2, 0, 0])
#       {
#         cube([bar_thickness, box_section_outer[0], inner_height + (2 * bar_thickness)], center=true);

#         for (z = [-inner_height/2 - bar_thickness, inner_height/2])
#         {
#           translate([0, -box_section_outer[0] / 2, z])
#           {
#             cube([inner_depth + bar_thickness, box_section_outer[0], bar_thickness]);
#           }
#         }
#       }
#     }
#   }
# }


def assembly():
    return sp.union()()


if __name__ == '__main__':
    print(sp.scad_render(assembly()))
