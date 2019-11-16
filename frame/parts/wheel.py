from solid import *


def wheel():
    big = 250
    thickness = 100

    outer = cylinder(d=290, h=thickness, center=True)

    _wheel_cutout = translate([0, 0, -thickness / 2 - 0.1])(
        cylinder(d=180, h=15),
        cylinder(d=130, h=45),
    )
    wheel_cutouts = [rotate([0, a, 0])(_wheel_cutout) for a in [0, 180]]

    _bolt = translate([0, 50, 0])(cylinder(d=8, h=big, center=True), )
    bolts = [rotate([0, 0, a * 360 / 5])(_bolt) for a in range(5)]

    shaft = cylinder(d=16, h=big, center=True),

    bearing_mount = cylinder(h=thickness / 2, d=38)

    return color("darkgray")(
        rotate([0, 90, 0])(
            difference()(
                union()(
                    outer - wheel_cutouts - bolts,
                    bearing_mount,
                ),
                shaft,
            )
        )
    )


print(scad_render(wheel()))
