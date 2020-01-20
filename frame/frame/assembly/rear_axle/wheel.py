import solid as sp
import solid.utils as spu

from frame.utils import bom, entrypoint

outer_diameter = 260
thickness = 80
bolt_hole_diameter = 8.


@bom.part('Rear Wheel')
def volume():
    outer = sp.cylinder(d=outer_diameter, h=thickness, center=True)

    wheel_cutouts = [
        sp.rotate((0, a, 0))(
            spu.down((thickness / 2.) + 0.1)(
                sp.cylinder(d=120, h=15),
                sp.cylinder(d=90, h=40),
            )
        ) for a in [0, 180]
    ]

    bolts = [
        sp.rotate([0, 0, a * (360. / 4.)])(
            spu.forward(35.)
            (sp.cylinder(d=bolt_hole_diameter, h=thickness + 1., center=True))
        ) for a in range(4)
    ]

    # TODO: measure hole diameter
    shaft = sp.cylinder(d=30., h=thickness + 1., center=True),

    return sp.color("darkgray")(
        sp.rotate((0, 90, 0))(
            sp.difference()(
                sp.union()(outer - wheel_cutouts - bolts, ),
                shaft,
            )
        )
    )


if __name__ == '__main__':
    entrypoint.main(volume())
