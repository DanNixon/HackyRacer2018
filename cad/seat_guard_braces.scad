$fn=64;

mounting_hole_centres = 315;
mounting_hole_diamter = 5.5;

bar_dimensions = [330, 10];


difference()
{
  square(bar_dimensions, center=true);

  dx = mounting_hole_centres / 2;
  for(x=[-dx, dx])
  {
    translate([x, 0])
    {
      circle(d=mounting_hole_diamter);
    }
  }
}
