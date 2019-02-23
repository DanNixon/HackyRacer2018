use <wheel.scad>;

main_width = 450;

rotate([0, 90, 0])
{
  /* Frame guide */
  color("white")
  {
    frame_width = 330;
    cube([50, 50, frame_width], center=true);
  }

  /* Square section of axle */
  color("blue")
  {
    cube([20, 20, main_width], center=true);
  }

  /* Round section of axle */
  color("red")
  {
    $fn = 64;
    cylinder(d=16, h=main_width+150, center=true);
  }

  /* Motor mounts */
  dz = (main_width / 2) - 50;
  for (z = [-dz, dz])
  {
    angle = 150;
    x = 50;

    rotate([0, 0, angle])
    {
      translate([-x/2, -x/2, z])
      {
        cube([x, 250, 5]);
      }
    }
  }
}

/* Wheels */
for (a = [0, 180])
{
  rotate([0, 0, a])
  {
    translate([-(main_width + 104) / 2, 0, 0])
    {
      color("darkgrey")
      {
        Wheel();
      }
    }
  }
}
