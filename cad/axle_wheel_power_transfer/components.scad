$fn = 128;

module WheelInterface(
    diameter_inner,
    diameter_mid,
    diameter_outer,
    depth,
    depth_lower,
    depth_upper,
    fin_thickness,
    fin_offset
    )
{
  translate([0, 0, -depth])
  {
    difference()
    {
      union()
      {
        cylinder(d=diameter_mid, h=depth);

        hull()
        {
          translate([0, 0, depth-depth_upper])
          {
            cylinder(d=diameter_outer, h=depth_upper);
          }

          translate([0, 0, depth_lower])
          {
            cylinder(d=diameter_mid, h=1);
          }
        }
      }

      translate([0, 0, -1])
      {
        cylinder(d=diameter_inner, h=depth+2);
      }

      for (a = [0 : 360/8 : 360])
      {
        rotate([0, 0, a])
        {
          cube([diameter_outer + 10, fin_thickness, (depth - fin_offset) * 2], center=true);
        }
      }
    }
  }
}

module KeyScrewHole(
    key_screw_diameter,
    key_screw_thread_length,
    key_screw_head_diameter
    )
{
  rotate([90, 0, 360/16])
  {
    cylinder(d=key_screw_diameter, h=100);

    translate([0, 0, key_screw_thread_length])
    {
      cylinder(d=key_screw_head_diameter, h=100);
    }
  }
}

module AxleMount(
    diameter_outer,
    diameter_inner,
    depth,
    depth_mid,
    axle_bore
    )
{
  difference()
  {
    hull()
    {
      cylinder(d=diameter_outer, h=depth_mid);
      cylinder(d=diameter_inner, h=depth);
    }

    translate([0, 0, -1])
    {
      cylinder(d=axle_bore, h=depth+2);
    }
  }
}
