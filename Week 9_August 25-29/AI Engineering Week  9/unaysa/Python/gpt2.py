from transformers import pipeline
import aicamp_day1

generator = pipeline('text-generation', model='gpt2')

response = generator("What is roblox?,", max_length=30, num_return_sequences=5)

text = aicamp_day1.make_text(response)

print(text)

  
