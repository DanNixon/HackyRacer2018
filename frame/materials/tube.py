import solid as sp
import solid.utils as spu


def projection(diameter, wall_thickness):
    outer = sp.circle(d=diameter)
    inner = sp.circle(d=diameter - 2 * wall_thickness)
    return outer - inner


def volume(
        length, diameter=25, wall_thickness=2, center=False,
        material='mild_steel'
):
    material = sp.linear_extrude(length)(projection(diameter, wall_thickness))
    return spu.down(length / 2)(material) if center else material


if __name__ == '__main__':
    print(sp.scad_render(volume(100)))