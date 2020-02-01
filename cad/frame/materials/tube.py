import solid as sp
import solid.utils as spu

from frame.utils import bom


def projection(diameter, wall_thickness):
    outer = sp.circle(d=diameter)
    inner = sp.circle(d=diameter - (2. * wall_thickness))
    return outer - inner


@bom.part('Tube')
def volume(diameter, length, wall_thickness, center=False):
    material = sp.linear_extrude(length)(projection(diameter, wall_thickness))
    return spu.down(length / 2)(material) if center else material


if __name__ == '__main__':
    print(sp.scad_render(volume(diameter=100., wall_thickness=2.)))
