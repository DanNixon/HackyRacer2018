import solid as sp
import solid.utils as spu

from frame.assembly.dimensions import outer
from frame.materials import plate
from frame.utils import entrypoint, place_at_centres
from frame.primitives import drilled_hole

from .dimensions import small_light_centres, small_light_y_offset, large_light_centres, large_light_y_offset
from .. import lights

width = 350.
height = 150.

thickness = 8.

below_frame = 20.

mounting_hole_centres = 180.


def projection():
    d = (height / 2.) - below_frame

    panel = spu.forward(d)(
        plate.projection(size=(width, height), radius=10, center=True)
    )

    mounting_holes = place_at_centres(
        [mounting_hole_centres, 0], drilled_hole.projection(8)
    )

    small_light_holes = spu.forward(small_light_y_offset)(
        place_at_centres([small_light_centres, 0], lights.small.holes())
    )

    large_light_holes = spu.forward(large_light_y_offset)(
        place_at_centres([large_light_centres, 0], lights.large.holes())
    )

    return panel - mounting_holes - small_light_holes - large_light_holes


def volume():
    return sp.linear_extrude(thickness)(projection())


if __name__ == '__main__':
    entrypoint.main(projection())
