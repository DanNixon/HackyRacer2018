import solid as sp
import solid.utils as spu

from frame.materials import plate
from frame.utils import entrypoint, place_at_centres
from frame.primitives import drilled_hole
from frame.assembly.dimensions import outer

from .dimensions import light_centres, light_y_offset
from .. import lights

width = 2. * outer
height = 150

thickness = 8

magic_1 = 20

mounting_hole_centres = 300


def projection():
    d = (height / 2.) - magic_1

    panel = spu.forward(d)(
        plate.projection(size=(width, height), radius=10, center=True)
    )

    mounting_holes = place_at_centres(
        [mounting_hole_centres, 0], drilled_hole.projection(8)
    )

    rear_light_holes = spu.forward(light_y_offset)(
        [place_at_centres([x, 0], lights.small.holes()) for x in light_centres]
    )

    return panel - mounting_holes - rear_light_holes


def volume():
    return sp.linear_extrude(thickness)(projection())


if __name__ == '__main__':
    entrypoint.main(projection())
