import solid as sp


def volume():
    big = 250
    thickness = 100

    outer = sp.cylinder(d=290, h=thickness, center=True)

    _wheel_cutout = sp.translate([0, 0, -thickness / 2 - 0.1])(
        sp.cylinder(d=180, h=15),
        sp.cylinder(d=130, h=45),
    )
    wheel_cutouts = [sp.rotate([0, a, 0])(_wheel_cutout) for a in [0, 180]]

    _bolt = sp.translate([0, 50, 0])(sp.cylinder(d=8, h=big, center=True), )
    bolts = [sp.rotate([0, 0, a * 360 / 5])(_bolt) for a in range(5)]

    shaft = sp.cylinder(d=16, h=big, center=True),

    bearing_mount = sp.cylinder(h=thickness / 2, d=38)

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
