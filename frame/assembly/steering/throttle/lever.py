import solid as sp

from frame.utils import entrypoint

pot_shaft_diameter = 6.
thickness = 6.


def hull_part(pa, pb, da, db):
    return sp.hull()(
        sp.translate(pa)(sp.circle(d=da, segments=32)),
        sp.translate(pb)(sp.circle(d=db, segments=32)),
    )


def projection():
    pq = (-5., 20.)
    pa = (0., 0.)
    pb = (30., 3.)
    pc = (38., 6.)
    pd = (44., 12.)

    dq = 6.
    da = 15.
    db = 8.
    dc = 8.
    dd = 8.

    return sp.difference()(
        sp.union()(
            hull_part(pa, pq, da, dq),
            hull_part(pa, pb, da, db),
            hull_part(pb, pc, db, dc),
            hull_part(pc, pd, dc, dd),
        ),
        sp.translate(pa)(sp.circle(d=pot_shaft_diameter, segments=16)),
        sp.translate(pq)(sp.circle(d=3., segments=16)),
    )


def volume():
    return sp.linear_extrude(thickness, center=True)(projection())


if __name__ == '__main__':
    entrypoint.main(volume())
