import requests
import python.aicamp_day1 as aicamp_day1

API_URL = "https://api-inference.huggingface.co/models/google/gemma-1.1-7b-it"
headers = {"Authorization": "Bearer <token-here>"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
	
output = query({
	"inputs": "What is a tree? ",
})

result = aicamp_day1.make_text(output)
print(result)