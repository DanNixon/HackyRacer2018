use <../../parts/wheel.scad>;

module FrontWheelAssembly()
{
  translate([100, 0, 0])
  {
    color("red")
    {
      Wheel();
    }
  }

  magic_1 = 30;
  magic_2 = 25;
  magic_3 = 20;
  magic_4 = 40;

  color("green")
  {
    hull()
    {
      cylinder(h=magic_1, r=magic_2, center=true, $fn=64);

      translate([magic_4, 0, 0])
      {
        cylinder(h=magic_1, r=magic_3, center=true, $fn=64);
      }
    }
  }

  color("blue")
  {
    rotate([0, 90, 0])
    {
      cylinder(d=17, h=160);
    }
  }
}

FrontWheelAssembly();
