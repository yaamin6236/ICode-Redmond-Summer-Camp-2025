import time
import random
print("BOO")
print("Salut, je m'appelle Namit. J'ai quatorze ans et j'aime jouer au basketball avec mes amis tous les jours apres l'ecole. J'ai un chien blanc, et il s'appelle Puter. Ma famille comprise de quatre membres. Ma mere s'appelle Namrata, et elle est ingenieur. Son nourriture prefere estElle aime les joues de societe. Mon pere s'appelle Jijo, et il est ingenieur aussi. Il a des cheveux noir boucles. Mon petit frere Naman a douze ans, et il joue au soccer. ")
name = "Namit"
partner_age = 15
partner_name = "CactusJack"
partner_food = "Prickly Pear"
henry_age = 12
henry_name = "Henry" 
henry_food = "Sushi"
user_input = input("What is your favorite song?")    
print("Searching Spotify database for", user_input, "...")
time.sleep(2)
loading_msgs = [
    "Song Identified!",
    "Scanning Lyrics...",
    "Analyzing Music...",
    "Tracking Artist...",
    "Calculating Final Score..." 
]
for msg in loading_msgs:
    print(msg)
    time.sleep(random.uniform(0.4, 1.3))
time.sleep(2)
print("This song sucks. Final Score: Pathetic 😢. This")