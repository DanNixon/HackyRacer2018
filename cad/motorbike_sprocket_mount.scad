/* Alternative mounting part for motorbike sprockets. */
/* Needs dimensions correcting if this is actually going to be used. */

$fn = 64;

part_length = 30;
part_diameter = 16;

shaft_diameter = 8;

flange_diameter = 35;
flange_thickness = 5;

sprocket_mount_lip = 4;
sprocket_mount_screw_centres = 25;
sprocket_mount_screw_diameter = 5;

shaft_grub_screw_diameter = 6;
shaft_grub_screw_position = 20;

magic_number_1 = 20;


rotate([-90, 0, 0])
{
  difference()
  {
    union()
    {
      cylinder(h=part_length, d=part_diameter);

      translate([0, 0, sprocket_mount_lip])
      {
        cylinder(h=flange_thickness, d=flange_diameter);
      }
    }

    translate([0, 0, -1])
    {
      cylinder(h=part_length + 2, d=shaft_diameter);
    }

    for(x = [-sprocket_mount_screw_centres/2, sprocket_mount_screw_centres/2])
    {
      translate([x, 0, 0])
      {
        cylinder(h=magic_number_1, d=sprocket_mount_screw_diameter);
      }
    }

    translate([0, 0, shaft_grub_screw_position])
    {
      rotate([90, 0, 0])
      {
        cylinder(h=magic_number_1, d=shaft_grub_screw_diameter);
      }
    }
  }
}
