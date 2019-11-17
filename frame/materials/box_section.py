import solid as sp
import solid.utils as spu

default_size = [25., 25.]


def projection(size=None, wall_thickness=2., center=False):
    size = default_size if size is None else size

    outer = sp.square(size, center=center)
    inner = sp.square([a - 2. * wall_thickness for a in size], center=center)

    outer -= inner if center else sp.translate(
        [wall_thickness, wall_thickness]
    )(inner)

    return outer


def volume(
    length,
    size=None,
    wall_thickness=2.,
    center=False,
):
    size = default_size if size is None else size

    material = sp.linear_extrude(length)(
        projection(size, wall_thickness, center)
    )
    return spu.down(length / 2.)(material) if center else material


if __name__ == '__main__':
    print(sp.scad_render(volume(100, size=[10, 20])))
