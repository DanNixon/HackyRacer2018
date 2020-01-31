import solid as sp
import solid.utils as spu

from frame.utils import entrypoint

from . import wheel, mount


def assembly():
    return sp.union()(
        sp.color('red')(wheel.volume()),
        spu.right(3.)(sp.color('green')(mount.volume()), )
    )


if __name__ == '__main__':
    entrypoint.main(assembly())
