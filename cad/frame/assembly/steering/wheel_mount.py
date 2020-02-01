import solid as sp
import solid.utils as spu

from frame.primitives import drilled_hole
from frame.utils import entrypoint

from .dimensions import column_diameter
from . import wheel

face_width = 15
face_diameter = 60

clamp_width = 36
clamp_diameter = 32

length = face_width + clamp_width


def volume():
    face_plate = sp.cylinder(d=face_diameter, h=face_width)

    # Drill and tap holes for column key screws as appropriate
    column_clamp = sp.cylinder(d=clamp_diameter, h=length)

    column = spu.down(1)(sp.cylinder(d=column_diameter, h=length + 2))

    # Drill and tap holes for steering wheel mounting as appropriate
    mounting_holes = wheel.place_mounting_holes(drilled_hole.volume(5))

    return sp.union()(face_plate, column_clamp) - column - mounting_holes


if __name__ == '__main__':
    entrypoint.main(volume())
