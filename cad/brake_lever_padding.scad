module BrakeLeverPadding(height, inner, padding, split=5)
{
  outer = inner + padding;
  extended_height = height + 2;

  difference()
  {
    cylinder(h=height, d=outer);

    translate([0, 0, -1])
    {
      cylinder(h=extended_height, d=inner);

      translate([0, -split/2, 0])
      {
        cube([outer+5, split, extended_height]);
      }
    }
  }
}

BrakeLeverPadding(30, 19.5, 3.5);
