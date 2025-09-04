import time
import random
nameis = input("What's your name?")
ageis = int(input("How old are you? (Type a single number, in years old.)"))
favfoodis = input("Nice! What's your favorite food?")
print("Your name is", nameis, ".")
print("You're", ageis, "years old.")
print("And your favorite food is", favfoodis, ".")
if ageis > 13:
    print("you are old")
else:
    print("you are young")
bonusis = input("Bonus Question! Do you like this survey? Y or N")

if bonusis.upper() == "Y":
    print("Gooood boy 😍")
else:
    print("I'm coming for you😁")
    time.sleep(1)

loading_msgs = [
    "Tracking IP Address",
    "Accessing Digital Footprint",
    "Decrypting Passwords",
    "Hacking Into Mainframe",
    "Accessing Social Security Information",
    "Storing all info onto offline database"
]
for msg in loading_msgs:
    print(msg)
    time.sleep(random.uniform(0.4, 0.9))

time.sleep(2)
    
print("Done! See you soon...")


