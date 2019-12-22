import solid as sp


def test_grand():
    import frame.assembly.grand as grand
    thing = grand.assembly()
    print(sp.scad_render(thing))
    # assert len(thing._repr_png_()) > 1000
