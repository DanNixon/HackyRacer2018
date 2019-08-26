module Motor()
{
  $fn=64;

  shaft_diameter = 10;
  shaft_length = 30;

  sprocket_diameter = 30;

  rotate([0, 90, 0])
  {
    /* Body */
    color("orange")
    {
      /* TODO */
      cylinder(d=100, h=140);
    }
  }

  rotate([0, -90, 0])
  {
    /* Shaft */
    color("black")
    {
      cylinder(d=shaft_diameter, h=shaft_length);
    }

    translate([0, 0, shaft_length])
    {
      color("cyan")
      {
        cylinder(d=sprocket_diameter, h=5, center=true);
      }
    }
  }
}

Motor();
