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
        max_tokens=1024,
        n=1,
        top_p=1,
        stop=None               # to control response generation
    )

    # if print_output:
    #     print(completions)

    return completions.choices[0].text

topic = 'Virtualization'
query = 'Create a Linkedin post, based on,{} with line break'.format(topic)
response = generate_text(query)
# print(response)
response = "Hello LinkedIn Fam! Today we are going to deep dive in the topic {}".format(topic) + response
file_path = 'c2.txt'
with open(file_path, 'w', encoding='utf-8') as file:
        file.write(response)