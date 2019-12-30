import solid as sp
import solid.utils as spu

from frame.utils import bom

# TODO
default_size = (10., 2.)


def projection(size=None, center=False):
    size = default_size if size is None else size

    return sp.square(size, center=True)


@bom.part('Flat Bar')
def volume(length, size=None, center=False):
    size = default_size if size is None else size

    material = sp.linear_extrude(length)(projection(size))
    return spu.down(length / 2.)(material) if center else material


if __name__ == '__main__':
    print(sp.scad_render(volume(length=100, size=(10, 20))))
