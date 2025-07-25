from djitellopy import Tello

tello = Tello()
send_rc_control

def fly():
    tello.move_up(50)
    tello.rotate_cw(90)
    tello.move_down(30)

def main():
    tello.connect()
    tello.takeoff()
    tello.land()      