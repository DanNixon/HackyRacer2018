import solid as sp


def test_assembly():
    from .assembly import assembly
    thing = assembly()
    print(sp.scad_render(thing))
    # assert len(thing._repr_png_()) > 1000
