import requests
import aicamp_day1

API_URL = "https://api-inference.huggingface.co/models/TinyLlama/TinyLlama-1.1B-Chat-v1.0"
headers = {"Authorization": "Bearer <token-here>"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
	
output = query({
	"inputs": "What is a car? ",
})

result = aicamp_day1.make_text(output)
print(result)