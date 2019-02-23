module MotorMount()
{
  circle(d=12);

  for(a = [0 : 90 : 359])
  {
    rotate([0, 0, a])
    {
      translate([45/2, 0])
      {
        circle(d=4);
      }
    }
  }
}

difference()
{
  square([100, 100], center=true);
  MotorMount();
}
