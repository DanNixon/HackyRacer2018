import solid as sp
import solid.utils as spu

from frame.utils import entrypoint

from . import lever, mount


def assembly():
    return sp.union()(
        sp.color('red')(
            # TODO
            spu.down(20)
            (sp.rotate((0, 90, 0))(sp.rotate((0, 0, -90))(lever.volume())))
        ),
        sp.color('green')(mount.volume()),
    )


if __name__ == '__main__':
    entrypoint.main(assembly())
