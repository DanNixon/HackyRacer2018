import solid as sp
import solid.utils as spu

from frame.assembly import wheel
from frame.utils import entrypoint

from . import left_stub_axle


def assembly():
    return sp.union()(
        sp.color('red')(spu.left(100)(wheel.volume())),
        sp.color('green')(left_stub_axle.volume()),
    )


if __name__ == '__main__':
    entrypoint.main(assembly())
