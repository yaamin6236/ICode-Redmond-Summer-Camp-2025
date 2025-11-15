import requests

def getduck():
    response = requests.get("https://random-d.uk/api/v2/random")
    response = requests.json()
    print(response)


    getduck()