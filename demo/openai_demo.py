#!/usr/bin/env python3

import openai
import os

# Set up OpenAI API credentials
openai.api_key = os.environ["OPENAI_API_KEY"]

# Define a prompt for the model to generate text from
prompt = "What is the meaning of life?"

# Generate text using the GPT language model
response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=prompt,
    max_tokens=50
)

# Print the generated text
print(response.choices[0].text)
