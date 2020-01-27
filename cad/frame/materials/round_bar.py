import solid as sp
import solid.utils as spu

from frame.utils import bom


def projection(diameter):
    return sp.circle(d=diameter)


@bom.part('Round Bar')
def volume(diameter, length, center=False):
    material = sp.linear_extrude(length)(projection(diameter))
    return spu.down(length / 2)(material) if center else material


if __name__ == '__main__':
    print(sp.scad_render(volume(diameter=100)))
