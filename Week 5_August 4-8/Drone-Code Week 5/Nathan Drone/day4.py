from easytello import tello


drone = tello.Tello()
drone.takeoff()
drone.up(20)
drone.forward(70)
drone.land()
drone.takeoff()
drone.up(50)
drone.forward(80)
drone.land()

