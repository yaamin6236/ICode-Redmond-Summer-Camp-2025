from easytello import tello

Drone = tello.Tello()

for i in range(2):
    Drone.takeoff()
    Drone.forward(80)
    Drone.land()