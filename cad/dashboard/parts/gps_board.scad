pcb_dimensions = [36, 26, 1.6];

mounting_hole_diameter = 3.1;
mounting_hole_centres = [31, 21];

module GpsBoardHoles()
{
  for(x = [-mounting_hole_centres[0] / 2, mounting_hole_centres[0] / 2])
  {
    for(y = [-mounting_hole_centres[1] / 2, mounting_hole_centres[1] / 2])
    {
      translate([x, y, 0])
      {
        circle(d=mounting_hole_diameter, $fn=32);
      }
    }
  }
}

module GpsBoard()
{
  difference()
  {
    /* PCB */
    translate([0, 0, pcb_dimensions[2] / 2])
    {
      color("green")
      {
        cube(pcb_dimensions, center=true);
      }
    }

    linear_extrude(20, center=true)
    {
      GpsBoardHoles();
    }
  }
}

GpsBoard();
