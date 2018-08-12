diameter_inner = 65;
diameter_outer = 80;

mount_thickness = 8;
guard_length = 60;

magic_offset_1 = 20;

mount_hole_diameter = 4.5;
mount_hole_offset = 4.5;


intersection()
{
  difference()
  {
    translate([0, 0, -magic_offset_1])
    {
      rotate([0, -90, 0])
      {
        difference()
        {
          cylinder(d=diameter_outer, h=guard_length+mount_thickness);

          translate([0, 0, -1])
          {
            cylinder(d=diameter_inner, h=guard_length+1);
          }

          for (a = [50, -35])
          {
            rotate([0, 0, a])
            {
              translate([-50, 0, 0])
              {
                cube([100, 200, 200], center=true);
              }
            }
          }
        }
      }
    }

    translate([0, 0, -50])
    {
      cube([200, 200, 100], center=true);
    }

    rotate([0, -90, 0])
    {
      translate([mount_hole_offset, 0, guard_length-1])
      {
        cylinder(d=mount_hole_diameter, h=mount_thickness+2, $fn=32);
      }
    }
  }
}
