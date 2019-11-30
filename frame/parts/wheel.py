import solid as sp

from frame.utils import bom

outer_diameter = 260
thickness = 90

@bom.part('Wheel')
def volume():
    big = 250

    outer = sp.cylinder(d=outer_diameter, h=thickness, center=True)

    wheel_cutouts = [
        sp.rotate([0, a, 0])(
            sp.translate([0, 0, -thickness / 2 - 0.1])(
                sp.cylinder(d=120, h=40),
            )
        ) for a in [0, 180]
    ]

    bolts = [
        sp.rotate([0, 0, a * 360 / 4])(
            sp.translate([0, 45, 0])(sp.cylinder(d=8, h=big, center=True))
        ) for a in range(4)
    ]

    shaft = sp.cylinder(d=16, h=big, center=True),

    bearing_mount = sp.cylinder(h=thickness / 2, d=40)

    return sp.color("darkgray")(
        sp.rotate([0, 90, 0])(
            sp.difference()(
                sp.union()(
                    outer - wheel_cutouts - bolts,
                    bearing_mount,
                ),
                shaft,
            )
        )
    )


if __name__ == '__main__':
    print(sp.scad_render(volume()))
