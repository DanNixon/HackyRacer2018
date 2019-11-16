include <../../../../../dimensions.scad>;

use <../../../../../primitives/assembly_instruction.scad>;

disc_lip_width = 5;
disc_lip_diameter = 25;

disc_face_width = 10;
disc_face_diameter = 55;

axle_clamp_width = 40;
axle_clamp_diameter = 30;

module AxleMount()
{
  difference()
  {
    union()
    {
      translate([0, 0, -disc_lip_width])
      {
        cylinder(d=disc_lip_diameter, h=disc_lip_width);
      }

      AssemblyInstruction(
          "disc_face_plate",
          "drill and tap holes for brake disc mounting as appropriate");
      cylinder(d=disc_face_diameter, h=disc_face_width);

      AssemblyInstruction(
          "axle_clamp",
          "drill and tap holes for axle key screws as appropriate");
      cylinder(d=axle_clamp_diameter, h=axle_clamp_width);
    }

    /* Axle hole */
    cylinder(d=axle_diameter, h=100, center=true);
  }
}

AxleMount();
