import requests

def getDuck():
	response = requests.get("https://random-d.uk/api/v2/random")
	response = response.json()
	print(response)

def getUselessFact():
	response = requests.get("https://uselessfacts.jsph.pl/api/v2/facts/random")
	response = response.json()
	print(response)

def getRecipe():
	response = requests.get("https://themealdb.com/api/json/v1/1/search.php?s=Pancakes")
	response = response.json()
	print(response)

getUselessFact()
getRecipe()	
getDuck()