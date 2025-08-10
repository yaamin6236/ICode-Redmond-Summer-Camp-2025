from easytello import tello

my_drone = tello.Tello()

my_drone.takeoff()
my_drone.forward(100)
my_drone.right(70)
my_drone.forward(70)
my_drone.right(30)
my_drone.back(80)
my_drone.left(30)
my_drone.back(70)
my_drone.right(60)
my_drone.back(60)
my_drone.right(70)
my_drone.land()