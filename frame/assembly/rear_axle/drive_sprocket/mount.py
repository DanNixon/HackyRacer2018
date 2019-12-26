import solid as sp
import solid.utils as spu

from frame.assembly.dimensions import axle_diameter
from frame.primitives import drilled_hole
from frame.utils import entrypoint

from . import sprocket

lip_width = 4
lip_diameter = 25

face_width = 12
face_diameter = 55

clamp_width = 28
clamp_diameter = 33


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
    mounting_holes = sprocket.place_mounting_holes(drilled_hole.volume(6))

    return sp.union()(lip, face_plate, axle_clamp) - axle - mounting_holes


if __name__ == '__main__':
    entrypoint.main(volume())
