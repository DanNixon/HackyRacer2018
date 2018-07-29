module SteeringSpacer(h)
{
  difference()
  {
    cylinder(h=h, d=13);

    translate([0, 0, -1])
    {
      cylinder(h=h+2, d=9);
    }
  }
}
