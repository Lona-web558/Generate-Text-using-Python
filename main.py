#Generate Text using Python
from transformers import pipeline
model = pipeline("text-generation", model="gpt2")

sentence = model("Hello, my name is Lona , I love God and I believe in freedom of expression as long as you're not harming the other person. do_sample=True, top_k=50, temperature=0.9, max_length=100, num_return_sentences=2")

for i in sentence:
    print(i["genetrated_text"])
