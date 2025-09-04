import os
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
            "content": "What is the capital of USA?"
        }
    ],
    "model": "microsoft/phi-4"
})

print(aicamp_day1.make_text((response["choices"][0]["message"]['content'])))