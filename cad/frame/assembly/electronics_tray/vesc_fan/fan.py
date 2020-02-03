import solid as sp

from frame.utils import bom, entrypoint, place_at_centres

size = (60., 60.)
thickness = 25.


def mounting_holes():
    return place_at_centres((51., 51.), sp.circle(d=4.))


def main_vent():
    return sp.intersection()(
        sp.square([d - 2. for d in size], center=True),
        sp.circle(d=64.),
    )


def projection():
    outer = sp.square(size, center=True)
    return outer - main_vent() - mounting_holes()


@bom.part('60mm PC fan')
def volume():
    return sp.linear_extrude(thickness)(projection())


if __name__ == '__main__':
    entrypoint.main(volume())
