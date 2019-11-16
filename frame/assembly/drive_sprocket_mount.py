import solid as sp
import solid.utils as spu

from frame.assembly import axle_diameter
from frame.parts.drive_sprocket import drive_sprocket

disc_lip_width = 5
disc_lip_diameter = 25

disc_face_width = 10
disc_face_diameter = 55

axle_clamp_width = 40
axle_clamp_diameter = 30


def drive_sprocket_mount():
    a = spu.down(disc_lip_width)(
        sp.cylinder(d=disc_lip_diameter, h=disc_lip_width)
    )

    # Drill and tap holes for brake disc mounting as appropriate
    b = sp.cylinder(d=disc_face_diameter, h=disc_face_width)

    # Drill and tap holes for axle key screws as appropriate
    c = sp.cylinder(d=axle_clamp_diameter, h=axle_clamp_width)

    axle = sp.cylinder(d=axle_diameter, h=100, center=True)

    return sp.union()(a, b, c) - axle


def assembly():
    return sp.union()(
        sp.color(spu.Red)(drive_sprocket_mount()),
        sp.color(spu.Green)(sp.rotate([180, 0, 0])(drive_sprocket())),
    )


if __name__ == '__main__':
    # print(sp.scad_render(drive_sprocket_mount()))
    print(sp.scad_render(assembly()))
