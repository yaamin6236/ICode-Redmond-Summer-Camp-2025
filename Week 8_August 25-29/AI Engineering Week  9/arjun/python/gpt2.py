from transformers import pipeline
import python.aicamp_day1 as aicamp_day1

generator = pipeline('text-generation', model='gpt2')

response = generator("What is a tree?", max_length=30, num_return_sequences=5)

text = aicamp_day1.make_text(response)

print(text)