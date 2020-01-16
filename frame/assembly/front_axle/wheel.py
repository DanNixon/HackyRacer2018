import solid as sp

from frame.utils import entrypoint, bom

outer_diameter = 260.
thickness = 80.
shaft_bore = 20.


@bom.part('Front Wheel')
def volume():
    outer = sp.cylinder(d=outer_diameter, h=thickness, center=True)
    shaft = sp.cylinder(d=shaft_bore, h=thickness + 1., center=True),

    return sp.color("darkgray")(sp.rotate([0, 90, 0])(outer - shaft))


if __name__ == '__main__':
    entrypoint.main(volume())
