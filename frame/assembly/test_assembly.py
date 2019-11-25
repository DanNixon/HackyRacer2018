import solid as sp


def test_brake_disc_mount():
    import frame.assembly.brake_disc_mount as brake_disc_mount
    thing = brake_disc_mount.assembly()
    print(sp.scad_render(thing))
    # assert len(thing._repr_png_()) > 1000


def test_drive_sprocket_mount():
    import frame.assembly.drive_sprocket_mount as drive_sprocket_mount
    thing = drive_sprocket_mount.assembly()
    print(sp.scad_render(thing))
    # assert len(thing._repr_png_()) > 1000


def test_front_wheel():
    import frame.assembly.front_wheel as front_wheel
    thing = front_wheel.assembly()
    print(sp.scad_render(thing))
    # assert len(thing._repr_png_()) > 1000


def test_front_wheel_bar():
    import frame.assembly.front_wheel_bar as front_wheel_bar
    thing = front_wheel_bar.assembly()
    print(sp.scad_render(thing))
    # assert len(thing._repr_png_()) > 1000


def test_grand():
    import frame.assembly.grand as grand
    thing = grand.assembly()
    print(sp.scad_render(thing))
    # assert len(thing._repr_png_()) > 1000


def test_lower_frame():
    import frame.assembly.lower_frame as lower_frame
    thing = lower_frame.assembly()
    print(sp.scad_render(thing))
    # assert len(thing._repr_png_()) > 1000


def test_motor_mount():
    import frame.assembly.motor_mount as motor_mount
    thing = motor_mount.assembly()
    print(sp.scad_render(thing))
    # assert len(thing._repr_png_()) > 1000


def test_rear_axle():
    import frame.assembly.rear_axle as rear_axle
    thing = rear_axle.assembly()
    print(sp.scad_render(thing))
    # assert len(thing._repr_png_()) > 1000


def test_rear_bumper():
    import frame.assembly.rear_bumper as rear_bumper
    thing = rear_bumper.assembly()
    print(sp.scad_render(thing))
    # assert len(thing._repr_png_()) > 1000


def test_seat_mount():
    import frame.assembly.seat_mount as seat_mount
    thing = seat_mount.assembly()
    print(sp.scad_render(thing))
    # assert len(thing._repr_png_()) > 1000
