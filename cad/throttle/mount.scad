include <config.scad>

module Mount()
{
  mount_length = 20;
  mount_width = 15;

  magic_1 = 10;
  magic_2 = 30;

  difference()
  {
    translate([0, 0, (lever_thickness / 2) - 0.1])
    {
      rotate([0, 180, 0])
      {
        linear_extrude(mount_thickness + lever_thickness + layer_spacing)
        {
          difference()
          {
            hull()
            {
              circle(d=mount_width);

              translate([0, -(mount_length - 1)])
              {
                square([mount_width, 1], center=true);
              }
            }

            circle(d=pot_mount_diameter, $fn=32);
          }
        }
      }
    }

    translate([0, 0, (lever_thickness - magic_1) / 2])
    {
      cube([mount_width + 1, magic_2, magic_1], center=true);

      rotate([90, 0, 0])
      {
        cylinder(h=50, d=mount_screw_diameter, $fn=16);
      }
    }
  }
}

Mount();
