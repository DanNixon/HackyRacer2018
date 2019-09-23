use <../../parts/box_section.scad>;

include <../../dimensions.scad>;

include <dimensions.scad>;

module SeatMountAssembly()
{
  difference()
  {
    union()
    {
      for (y = [-seat_depth/2, seat_depth/2])
      {
        translate([0, y, 0])
        {
          rotate([0, 0, 90])
          {
            BoxSection(
                name="seat_mount/section_a",
                col="red",
                outer=box_section_outer,
                length=outer * 2 + box_section_outer[0],
                center=true);
          }
        }
      }

      for (x = [-outer, outer, -seat_mount_centres[0]/2, seat_mount_centres[0]/2])
      {
        translate([x, 0, 0])
        {
          BoxSection(
              name="seat_mount/section_b",
              col="green",
              outer=box_section_outer,
              length=seat_depth - box_section_outer[0],
              center=true);
        }
      }

      translate([0, 0, (box_section_outer[1] + plate_thickness) / 2])
      {
        color("blue")
        {
          cube([outer * 2 + box_section_outer[0], 280 + box_section_outer[0], plate_thickness], center=true);
        }
      }
    }

    for (x = [-seat_mount_centres[0]/2, seat_mount_centres[0]/2])
    {
      for (y = [-seat_mount_centres[1]/2, seat_mount_centres[1]/2])
      {
        translate([x, y])
        {
          cylinder(h=100, d=seat_mount_hole_diameter, center=true);
        }
      }
    }
  }
}

SeatMountAssembly();
