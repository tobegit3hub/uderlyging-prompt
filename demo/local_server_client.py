#!/usr/bin/env python3

import requests
import os

# Set up OpenAI API credentials
openai_api_key = os.environ["OPENAI_API_KEY"]

# Define a prompt for the model to generate text from
prompt = "What is the meaning of life?"

session = requests.Session()
session.verify = False

# Generate text using the GPT language model
response = session.post(
    "http://127.0.0.1:8888/v1/engines/text-davinci-002/completions",
    headers={
        "Content-Type": "application/json",
        "Authorization": f"Bearer {openai_api_key}"
    },
    json={
        "prompt": prompt,
        "max_tokens": 50
    }
)

# Print the generated text
print(response.json()["choices"][0]["text"])
