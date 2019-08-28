module Motor()
{
  $fn=64;

  body_length = 140;
  body_diameter = 108;

  shaft_diameter = 12;
  shaft_length = 30;

  sprocket_diameter = 30;
  sprocket_pos = 16;

  mounting_hole_centres = 90;

  rotate([0, 90, 0])
  {
    /* Body */
    color("orange")
    {
      difference()
      {
        cylinder(d=body_diameter, h=body_length);

        /* Mounting holes */
        for(y = [-mounting_hole_centres/2, mounting_hole_centres/2])
        {
          translate([0, y, -1])
          {
            cylinder(d=5, h=body_length+2);
          }
        }
      }
    }
  }

  rotate([0, -90, 0])
  {
    /* Shaft */
    color("black")
    {
      cylinder(d=shaft_diameter, h=shaft_length);
    }

    translate([0, 0, sprocket_pos])
    {
      color("cyan")
      {
        cylinder(d=sprocket_diameter, h=5, center=true);
      }
    }
  }
}

Motor();
