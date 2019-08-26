module Motor()
{
  $fn=64;

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
      cylinder(d=10, h=30);
    }
  }
}

Motor();
