use <Sprockets.scad>

$fn = 180;

module SquashedHemisphere(size)
{
  resize(size)
  {
    intersection()
    {
      base_dim = 10;
      minus_half_base_dim = -(base_dim / 2);

      translate([minus_half_base_dim, minus_half_base_dim, 0])
      {
        cube([base_dim, base_dim, base_dim]);
      }

      sphere(d=base_dim);
    }
  }
}

module RoundedSprocket(no, teeth, d)
{
  intersection()
  {
    sprocket(no, teeth, 0);

    translate([0, 0, inches2mm(get_thickness(no)) / 2])
    {
      for (m = [0, 1])
      {
        mirror([0, 0, m])
        {
          SquashedHemisphere([d, d, 3]);
        }
      }
    }
  }
}

module RacerSprocket(
    chain_type,
    teeth,
    sprocket_round_dim,
    key_screw_diameter,
    key_screw_offset,
    bore_diameter,
    shaft_height,
    shaft_height_outer,
    shaft_diameter_inner,
    shaft_diameter_outer)
{
  difference()
  {
    union()
    {
      RoundedSprocket(chain_type, teeth, sprocket_round_dim);

      hull()
      {
        cylinder(d=shaft_diameter_inner, h=shaft_height);

        translate([0, 0, shaft_height-shaft_height_outer])
        {
          cylinder(d=shaft_diameter_outer, h=shaft_height_outer);
        }
      }
    }

    translate([0, 0, -1])
    {
      cylinder(d=bore_diameter, h=shaft_height+2);
    }

    translate([0, 0, key_screw_offset])
    {
      rotate([90, 0, 0])
      {
        cylinder(d=key_screw_diameter, h=50);
      }
    }
  }
}

