import solid as sp
import solid.utils as spu

from frame.utils import entrypoint

from . import light

height = 15.
thickness = 20.


def holes():
    return [sp.translate((x, 0., 0.))(sp.circle(d=3.)) for x in (-21., 0., 21.)]


def volume():
    width = light.mount_width + 20.

    body = sp.hull()(
        spu.up(1.)(sp.cube((width, thickness, 2.), center=True)),
        spu.up(height)(
            sp.rotate((0., 90., 0.))(
                sp.cylinder(d=thickness, h=width, center=True)
            )
        ),
    )

    cutout = spu.up(height)(
        sp.rotate((0., 90., 0.))(
            sp.union()(
                sp.cylinder(
                    d=thickness + 1., h=light.mount_width + 1., center=True
                ),
                sp.cylinder(d=light.mount_diameter, h=width + 1., center=True),
            )
        )
    )

    mounting_holes = sp.linear_extrude(15.)(holes())

    return body - cutout - mounting_holes()


if __name__ == '__main__':
    entrypoint.main(volume())
