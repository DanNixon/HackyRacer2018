use <common.scad>

module NumberPlate()
{
  Board()
  {
    for(x=[-70, 70])
    {
      translate([x, 18])
      {
        circle(d=4, $fn=32);
      }
    }

    translate([-22, 10])
    {
      TitleText("200");
    }

    translate([-75, -10])
    {
      TitleText("CARTRIDGES");
    }
  }
}

NumberPlate();
