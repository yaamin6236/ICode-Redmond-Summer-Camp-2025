import aicamp_day1
import requests

API_URL = "https://router.huggingface.co/v1/chat/completions"
headers = {
    "Authorization": f"Bearer YOUR_HUGGING_FACE_TOKEN",  # Replace with your token
}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

response = query({
    "messages": [
        {
            "role": "user",
            "content": "How many countriees in the world?"
        }
    ],
    "model": "microsoft/phi-4"
})

print(response["choices"][0]["message"])

