import solid as sp

from frame.utils import entrypoint


def volume():
    # TODO
    return sp.cube((10, 10, 10), center=True)


if __name__ == '__main__':
    entrypoint.main(volume())
