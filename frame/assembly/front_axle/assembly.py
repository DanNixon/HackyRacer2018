import solid as sp
import solid.utils as spu

from frame.assembly import wheel
from frame.utils import entrypoint

from . import bar, left_wheel, right_wheel


def assembly():
    return sp.union()(
        sp.color('red')(bar.assembly()),
        sp.color('green')(spu.left(220)(left_wheel.assembly())),
        sp.color('blue')(spu.right(220)(right_wheel.assembly())),
    )


if __name__ == '__main__':
    entrypoint.main(assembly())
