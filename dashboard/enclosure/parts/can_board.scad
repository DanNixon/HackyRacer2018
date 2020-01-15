pcb_dimensions = [22, 11, 1.6];

mounting_hole_diameter = 2.1;
mounting_hole_centres = 8.5;

module CanBoardHoles()
{
  for(y = [-mounting_hole_centres / 2, mounting_hole_centres / 2])
  {
    translate([-9.5, y, 0])
    {
      circle(d=mounting_hole_diameter, $fn=32);
    }
  }
}

module CanBoard()
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
      CanBoardHoles();
    }
  }
}

CanBoard();
