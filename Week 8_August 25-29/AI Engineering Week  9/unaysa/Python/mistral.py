import requests
import aicamp_day1

API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2"
headers = {"Authorization": "Bearer YOUR_HUGGING_FACE_TOKEN"}  # Replace with your token

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
	
output = query({
	"inputs": "What is at tree? ",
})

result = aicamp_day1.make_text(output)
print(result)