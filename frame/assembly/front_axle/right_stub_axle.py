import solid as sp

from frame.utils import bom, entrypoint

from . import stub_axle


@bom.part('Right Hand Stub Axle')
def volume():
    return stub_axle.volume(-1.)


if __name__ == '__main__':
    entrypoint.main(volume())
