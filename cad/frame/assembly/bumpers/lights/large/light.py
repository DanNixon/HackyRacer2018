import solid as sp
import solid.utils as spu

from frame.utils import entrypoint, place_at_centres
from frame.primitives import drilled_hole

diameter = 110.
thickness = 20.

mount_thickness = 12.
mount_width = 32.
mount_diameter = 6.


def holes():
    return spu.back(40.)(drilled_hole.projection(10.)),


def volume():
    body = spu.up(2.)(sp.cylinder(d=diameter, h=thickness))
    mount = spu.up(4.)(
        spu.back(diameter / 2.)(
            sp.rotate((-60., 0., 0.))(
                sp.rotate((0., 90., 0.))(
                    sp.hull()(
                        place_at_centres(
                            (20., 0.),
                            sp.cylinder(
                                d=mount_thickness, h=mount_width, center=True
                            )
                        )
                    ) - spu.right(10.)(
                        sp.cylinder(
                            d=mount_diameter, h=mount_width + 1., center=True
                        )
                    )
                )
            )
        )
    )
    return body + mount


if __name__ == '__main__':
    entrypoint.main(volume())
