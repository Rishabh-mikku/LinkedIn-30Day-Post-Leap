import openai
from dotenv import load_dotenv
import os
import requests

# openai.api_key=os.getenv("OPENAI_API_KEY")

from openai import OpenAI
client = OpenAI(api_key = "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")

response = client.images.generate(
  model="dall-e-2",
  prompt="Generate an image on data structures and algorithm",
  size="256x256",
  quality="standard",
  n=1,
)

image_url = response.data[0].url

print("Generated image URL: ", image_url)

from IPython.display import Image, display

# display(Image(url=image_url))

# Download the image
image_content = requests.get(image_url).content

file_path = "img_gen.jpg"

# Save the image to the specified file path
with open(file_path, 'wb') as file:
    file.write(image_content)

display(Image(filename=file_path))

