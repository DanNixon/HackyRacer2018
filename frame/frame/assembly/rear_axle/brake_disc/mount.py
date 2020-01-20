import solid as sp
import solid.utils as spu

from frame.assembly.dimensions import axle_diameter
from frame.primitives import drilled_hole
from frame.utils import entrypoint

from . import disc

lip_width = 3
lip_diameter = 38

face_width = 12
face_diameter = 60

clamp_width = 28
clamp_diameter = 38


def volume():
    lip = spu.down(lip_width)(sp.cylinder(d=lip_diameter, h=lip_width))

    face_plate = sp.cylinder(d=face_diameter, h=face_width)

    # Drill and tap holes for axle key screws as appropriate
    axle_clamp = sp.cylinder(d=clamp_diameter, h=face_width + clamp_width)

    axle = spu.down(lip_width + 1)(
        sp.cylinder(
            d=axle_diameter, h=lip_width + face_width + clamp_width + 2
        )
    )

    # Drill and tap holes for brake disc mounting as appropriate
    mounting_holes = disc.place_mounting_holes(drilled_hole.volume(6))

    return sp.union()(lip, face_plate, axle_clamp) - axle - mounting_holes


if __name__ == '__main__':
    entrypoint.main(volume())
