import solid as sp

# TODO


def test_brake_disc_projection():
    import frame.parts.brake_disc as brake_disc
    print(sp.scad_render(brake_disc.projection()))


def test_brake_disc_volume():
    import frame.parts.brake_disc as brake_disc
    print(sp.scad_render(brake_disc.volume()))


def test_drive_sprocket_projection():
    import frame.parts.drive_sprocket as drive_sprocket
    print(sp.scad_render(drive_sprocket.projection()))


def test_drive_sprocket_volume():
    import frame.parts.drive_sprocket as drive_sprocket
    print(sp.scad_render(drive_sprocket.volume()))


def test_motor_volume():
    import frame.parts.motor as motor
    print(sp.scad_render(motor.volume()))


def test_rear_axle_bearing_volume():
    import frame.parts.rear_axle_bearing as rear_axle_bearing
    thing = rear_axle_bearing.volume()
    print(sp.scad_render(thing))


def test_motor_mountable_face():
    import frame.parts.motor as motor
    print(sp.scad_render(motor.mountable_face()))


def test_vesc_volume():
    import frame.parts.vesc as vesc
    print(sp.scad_render(vesc.volume()))


def test_wheel_volume():
    import frame.parts.wheel as wheel
    print(sp.scad_render(wheel.volume()))
