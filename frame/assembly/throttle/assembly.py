import solid as sp

from frame.utils import entrypoint

from . import mount, lever


def assembly():
    return sp.union()(
        sp.color('red')(mount.volume()),
        sp.color('green')(lever.volume()),
    )


if __name__ == '__main__':
    entrypoint.main(assembly())
