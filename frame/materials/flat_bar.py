import solid as sp
import solid.utils as spu

from frame.utils import bom


def projection(size, center=False):
    return sp.square(size, center=True)


@bom.part('Flat Bar')
def volume(length, size, center=False):
    material = sp.linear_extrude(length)(projection(size))
    return spu.down(length / 2.)(material) if center else material


if __name__ == '__main__':
    print(sp.scad_render(volume(length=100, size=(10, 20))))
