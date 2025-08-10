import os

from easytello import tello
my_drone = tello.Tello()

MOVE_CONST = 10
ROTATE_CONST: int = 30

def execute_command(cmd):
    global my_drone , MOVE_CONST, ROTATE_CONST

    if cmd == "1":
        my_drone.takeoff()
    elif cmd == "2":
        my_drone.land()
    elif cmd == "w":
        my_drone.up(MOVE_CONST)
    elif cmd == "s":
        my_drone.down(MOVE_CONST)
    elif cmd == "a":
        my_drone.left(MOVE_CONST)
    elif cmd == "d":
        my_drone.right(MOVE_CONST)
    elif cmd == "e":
        my_drone.cw(ROTATE_CONST)
    elif cmd == "q":
        my_drone.ccw(ROTATE_CONST)

def user_command():
    possible_commands =[
        '1',
        '2',
        'w',
        's',
        'a',
        'd',
        'q',
        'o',
        'p',

    ]
    menu()
    u_input = input("Enter your command: ").lower()
    while not (u_input in possible_commands):
        os.system('clear')
        menu()
        u_input = input("Enter your command: ").lower()
    return u_input

def menu():
    move = MOVE_CONST
    rot = ROTATE_CONST
    print("User manual:")
    print("1: takeoff")
    print("2: land({})".format(move))
    print("w: up({})".format(move))
    print("s: down({})".format(move))
    print("a: left({})".format(move))
    print("d: right({})".format(move))
    print("e: cw({})".format(rot))
    print("q: ccw({})".format(rot))

def main():
    while True:
        command=user_command()
        execute_command(command)

if __name__ == '__main__':
    main()