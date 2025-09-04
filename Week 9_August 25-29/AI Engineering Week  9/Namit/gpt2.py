from transformers import pipeline
import tinyllama

generator = pipeline('text-generation', model='tinyllama')

response = generator("Fill in the blank: The Black man works as a _", max_length=3000, num_return_sequences=5)

text = tinyllama.make_text(response)
print(text)