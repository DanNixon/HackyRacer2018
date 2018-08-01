include <config.scad>

module HullPart(pa, pb, da, db)
{
  hull()
  {
    translate(pa)
    {
      circle(d=da, $fn=32);
    }

    translate(pb)
    {
      circle(d=db, $fn=32);
    }
  }
}

module Lever()
{
  pq = [-5, 20];
  pa = [0, 0];
  pb = [30, 3];
  pc = [38, 6];
  pd = [44, 12];

  dq = 6;
  da = 15;
  db = 8;
  dc = 8;
  dd = 8;

  difference()
  {
    union()
    {
      HullPart(pa, pq, da, dq);
      HullPart(pa, pb, da, db);
      HullPart(pb, pc, db, dc);
      HullPart(pc, pd, dc, dd);
    }

    translate(pa)
    {
      circle(d=pot_shaft_diameter, $fn=16);
    }

    translate(pq)
    {
      circle(d=3, $fn=16);
    }
  }
}

Lever();
