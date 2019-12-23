import solid as sp
import solid.utils as spu

from frame.utils import entrypoint
import frame.parts.wheel as wheel


def assembly():
    return sp.union()(sp.color('red')(spu.right(100)(wheel.volume())), )


if __name__ == '__main__':
    entrypoint.main(assembly())
