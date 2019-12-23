import solid as sp
import solid.utils as spu

from frame.assembly import outer
from frame.materials import plate
from frame.utils import entrypoint, place_at_centres
from frame.primitives import drilled_hole

width = 2. * outer
height = 150

thickness = 8

magic_1 = 20
magic_2 = 80


def projection():
    d = (height / 2.) - magic_1

    panel = spu.forward(d)(
        plate.projection(size=(width, height), radius=10, center=True)
    )

    mounting_holes = place_at_centres(
        [width - magic_2, 0], drilled_hole.projection(8)
    )

    return panel - mounting_holes


def volume():
    return sp.linear_extrude(thickness)(projection())


if __name__ == '__main__':
    entrypoint.main(projection())
