from djitellopy import Tello
def fly():
    tello = Tello()
    tello.connect()
    tello.takeoff()
    tello.move_up(150)
    tello.move_left(85)
    tello.move_right(85)
    tello.flip_forward(360)
    tello.flip_back(360)
    tello.land
    tello.connect
    tello.takeoff()
    tello.move_up(150)
    tello.land