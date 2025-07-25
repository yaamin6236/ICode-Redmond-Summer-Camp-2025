from djitellopy import Tello
tello = Tello()
# custom function
def fly():
    tello.flip("f")

def main():
    #create instance of drone, this is how we interact with our drone
    

    # Connect to drone
    tello.connect()

    # Tells the drone to land
    tello.takeoff()
    tello.flip("f")
    tello.move_left(50)
    tello.move_up(100)
    tello.flip("f")
    tello.move_forward(100)
    tello.rotate_clockwise(720)
    tello.move_left(50)
    tello.move_right(50)
    tello.rotate_counter_clockwise(90)
    tello.flip("b") 
    tello.flip("f")
    tello.land()