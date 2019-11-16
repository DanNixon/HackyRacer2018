import solid as sp
import solid.utils as spu

from frame.utils import place_at_centres
from frame.assembly import axle_diameter, wheel_centre_distance, brake_disc_mount, drive_sprocket_mount
from frame.parts.brake_disc import brake_disc
from frame.parts.wheel import wheel

plate_thickness = 1

seat_depth = 280

seat_mount_centres = [300, 200]
seat_mount_hole_diameter = 8


def assembly():
    return sp.union()()

# module SeatMountAssembly()
# {
#   difference()
#   {
#     union()
#     {
#       for (y = [-seat_depth/2, seat_depth/2])
#       {
#         translate([0, y, 0])
#         {
#           rotate([0, 0, 90])
#           {
#             BoxSection(
#                 name="seat_mount/x_bar",
#                 col="red",
#                 outer=box_section_outer,
#                 length=outer * 2 + box_section_outer[0],
#                 center=true);
#           }
#         }
#       }

#       DisplaceFromCentre(
#           name="seat_mount/y_bar",
#           x_positions = [-outer, outer, -seat_mount_centres[0]/2, seat_mount_centres[0]/2])
#       {
#         BoxSection(
#             name="seat_mount/y_bar",
#             col="green",
#             outer=box_section_outer,
#             length=seat_depth - box_section_outer[0],
#             center=true);
#       }

#       translate([0, 0, (box_section_outer[1] + plate_thickness) / 2])
#       {
#         AssemblyInstruction(
#             "seat_mount/guard_plate",
#             "Clearence holes drilled into plate");

#         AssemblyInstruction(
#             "seat_mount/guard_plate",
#             "Tap threads into seat mount box section");

#         Plate(
#             name="seat_mount/guard_plate",
#             col="blue",
#             size=[outer * 2 + box_section_outer[0], 280 + box_section_outer[0], plate_thickness],
#             center=true);
#       }
#     }

#     DisplaceFromCentre(
#         name="seat_mount/seat_mount_holes",
#         x_positions = [-seat_mount_centres[0]/2, seat_mount_centres[0]/2],
#         y_positions = [-seat_mount_centres[1]/2, seat_mount_centres[1]/2])
#     {
#       DrilledHole(
#           name="seat_mount/seat_mount_holes",
#           d=seat_mount_hole_diameter);
#     }
#   }
# }


if __name__ == '__main__':
    print(sp.scad_render(assembly()))
