from sys import exc_info

from easytello import tello

Drone = tello.Tello()

MOVE_CONST = 10
ROTATE_CONST = 90

def execute__command(cmd):

    global Drone, MOVE_CONST, ROTATE_CONST

    if cmd == "1":
        Drone.takeoff()
    elif cmd == "2":
        Drone.land()
    elif cmd == "w":
        Drone.up(MOVE_CONST)
    elif cmd == "a":
        Drone.left(ROTATE_CONST)
    elif cmd == "d":
        Drone.right(MOVE_CONST)
    elif cmd == "s":
        Drone.left(MOVE_CONST)
    elif cmd == "e":
        Drone.cw(ROTATE_CONST)
    elif cmd == "q":
        Drone.ccw(ROTATE_CONST)


def user_command():

    possible commands = ["1","2","w","s","a","d","q","p"]

    menu()
    u_input = input("please enter a command: ")
    while not (u_input in possible_commands):
        os.system('clear')
        u_input = input("please enter a command: ").lower()
    return u_input


def menu:
    global MOVE_CONST, ROTATE_CONST
    move MOVE_CONST
    rot = ROTATE_CONST
    print("user manual")
    print("1: take off")
    print("2: land")
    print("w: up").format(move)
    print("a: left")
    print("d: right")
    print("q: ccw")
    print("p: pause")
    print("e: cw")

def main():
    while True:
        Command = user_command()
        execute__command(Command)

if __name__ == "__main__":
    main()
