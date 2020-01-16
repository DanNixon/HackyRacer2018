import solid as sp
import solid.utils as spu

from frame.utils import entrypoint

from . import right_stub_axle, wheel, wheel_bushing


def assembly():
    return sp.union()(
        sp.color('red')(spu.right(100.)(wheel.volume())),
        sp.color('green')(right_stub_axle.volume()),
        sp.color('blue')(
            spu.right(58.)(sp.rotate((0., 90., 0.))(wheel_bushing.volume()))
        ),
    )


if __name__ == '__main__':
    entrypoint.main(assembly())
