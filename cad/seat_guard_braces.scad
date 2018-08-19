$fn=64;

mounting_hole_centres = [318, 320, 322];
mounting_hole_diamter = 5.5;

bar_width = 10;

for(i=[0:2])
{
  centre = mounting_hole_centres[i];

  translate([0, i*15])
  {
    difference()
    {
      square([centre + 15, bar_width], center=true);

      dx = centre / 2;
      for(x=[-dx, dx])
      {
        translate([x, 0])
        {
          circle(d=mounting_hole_diamter);
        }
      }
    }
  }
}
