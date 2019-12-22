import solid as sp
import solid.utils as spu

from frame.assembly import axle_diameter
from frame.utils import entrypoint
import frame.parts.brake_disc as brake_disc

disc_lip_width = 3
disc_lip_diameter = 38

disc_face_width = 12
disc_face_diameter = 60

axle_clamp_width = 28
axle_clamp_diameter = 38


def volume():
    lip = spu.down(disc_lip_width)(
        sp.cylinder(d=disc_lip_diameter, h=disc_lip_width)
    )

    face_plate = sp.cylinder(d=disc_face_diameter, h=disc_face_width)

    # Drill and tap holes for axle key screws as appropriate
    axle_clamp = sp.cylinder(
        d=axle_clamp_diameter, h=disc_face_width + axle_clamp_width
    )

    axle = sp.cylinder(d=axle_diameter, h=100, center=True)

    # Drill and tap holes for brake disc mounting as appropriate
    mounting_holes = brake_disc.place_mounting_holes(
        sp.cylinder(d=6, h=100, center=True)
    )

    return sp.union()(lip, face_plate, axle_clamp) - axle - mounting_holes


if __name__ == '__main__':
    entrypoint.main(assembly())
