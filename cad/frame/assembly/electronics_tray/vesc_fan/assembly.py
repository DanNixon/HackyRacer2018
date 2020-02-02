import solid as sp
import solid.utils as spu

from frame.utils import entrypoint

from . import fan, shroud


def assembly():
    return sp.union()(
        sp.color('red')(shroud.volume()),
        sp.color('green')(fan.volume()),
    )


if __name__ == '__main__':
    entrypoint.main(assembly())
