import requests

def getDuck():
    response = requests.get("https://random-d.uk/api/v2/random")
    response = response.json()
    print(response) 

getDuck()



def getRandom():
    response = requests.get("https://uselessfacts.jsph.pl/api/v2/facts/random.")
    response = response.json()
    print(response) 

getRandom()