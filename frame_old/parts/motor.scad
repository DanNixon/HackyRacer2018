body_diameter = 108;

mounting_hole_centres = 90;
mounting_hole_diameter = 5;

module Motor()
{
  $fn=64;

  body_length = 140;

  shaft_diameter = 12;
  shaft_length = 30;

  sprocket_diameter = 30;
  sprocket_pos = 16;

  rotate([0, 180, 0])
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
            cylinder(d=mounting_hole_diameter, h=body_length+2);
          }
        }
      }
    }
  }

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

module Motor2D()
{
  shaft_surround_diam = 22;

  vent_holes_centres = 65;
  vent_holes_diameter = 10;

  difference()
  {
    circle(d=body_diameter);

    circle(d=shaft_surround_diam);

    for(y = [-mounting_hole_centres/2, mounting_hole_centres/2])
    {
      translate([0, y, -1])
      {
        circle(d=mounting_hole_diameter);
      }
    }

    for (a = [0 : 360/8 : 359])
    {
      rotate([0, 0, a])
      {
        translate([vent_holes_centres / 2, 0])
        {
          circle(d=vent_holes_diameter);
        }
      }
    }
  }
}

Motor();

translate([0, 0, 50])
{
  Motor2D();
}
