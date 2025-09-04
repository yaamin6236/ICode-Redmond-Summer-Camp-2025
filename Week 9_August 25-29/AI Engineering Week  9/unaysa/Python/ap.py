import requests

def getDuck():
    response = requests.get("https://random-d.uk/api/v2/random")
    response = response.json()
    print(response)


getDuck()


def getRandomfact():
    response = requests.get("https://uselessfacts.jsph.pl/api/v2/facts/random")
    response = response.json()
    print(response)


getRandomfact()


# YOUR_HUGGING_FACE_TOKEN_1
# YOUR_HUGGING_FACE_TOKEN_2