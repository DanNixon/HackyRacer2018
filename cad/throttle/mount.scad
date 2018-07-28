include <config.scad>

module Mount()
{
  dim = 15;

  difference()
  {
    linear_extrude(lever_thickness + layer_spacing + mount_thickness, center=true)
    {
      hull()
      {
        circle(d=dim);

        translate([0, -10])
        {
          square([dim, 10], center=true);
        }
      }
    }

    cube([16, 18, lever_thickness + layer_spacing], center=true);

    cylinder(h=50, d=pot_mount_diameter, $fn=32);

    rotate([180, 0, 0])
    {
      cylinder(h=50, d=pot_shaft_diameter + 1, $fn=32);
    }

    rotate([90, 0, 0])
    {
      cylinder(h=50, d=mount_screw_diameter, $fn=16);
      cylinder(h=11, d=mount_screw_cutout_diameter, $fn=16);
    }
  }
}

Mount();
