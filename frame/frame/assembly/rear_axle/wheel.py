import solid as sp
import solid.utils as spu

from frame.utils import bom, entrypoint, place_n_at_x_around

outer_diameter = 260
thickness = 80
bolt_hole_diameter = 8.
inner_hole_diameter = 32.


def mounting_holes():
    bolt = place_n_at_x_around(
        4, 35.,
        sp.cylinder(d=bolt_hole_diameter, h=thickness + 1., center=True)
    )

    inner = sp.cylinder(d=inner_hole_diameter, h=thickness + 1., center=True),

    return sp.union()(
        bolt,
        inner,
    )


@bom.part('Rear Wheel')
def volume():
    outer = sp.cylinder(d=outer_diameter, h=thickness, center=True)

    magic_1 = (thickness - 5.) / 2.
    hub = [
        sp.rotate((0, a, 0))(
            spu.down((thickness / 2.) + 0.1)(
                sp.cylinder(d=85., h=magic_1),
                sp.cylinder(d=120., h=15.),
            )
        ) for a in [0, 180]
    ]

    return sp.color("darkgray")(
        sp.rotate((0, 90, 0))(sp.difference()(
            outer,
            hub,
            mounting_holes(),
        ))
    )


if __name__ == '__main__':
    entrypoint.main(volume())
