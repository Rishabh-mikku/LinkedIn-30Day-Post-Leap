import openai
from dotenv import load_dotenv
import os

# openai.api_key=os.getenv("OPEN_API_KEY")

from openai import OpenAI
client = OpenAI(api_key = "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")

def generate_text(query):
    completions = client.completions.create(
        model='gpt-3.5-turbo-instruct',
        temperature=0.5,
        prompt=query,
        max_tokens=500,
        n=1,
        stop=None              
    )



    return completions.choices[0].text

def save_subtopics_to_file(subtopics, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write("\n".join(subtopics))

topic = 'DSA'
query = f'Generate 30 subtopics related to {topic}'
response = generate_text(query)


subtopics = response.strip().split("\n")


file_path = 'subtopics.txt'
save_subtopics_to_file(subtopics, file_path)

print(f"Subtopics saved to: {file_path}")