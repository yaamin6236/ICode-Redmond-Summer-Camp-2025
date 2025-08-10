from easytello import tello
my_drone = tello.Tello()

for i in range(2):
    my_drone.takeoff()
    my_drone.forward(50)
    my_drone.land()