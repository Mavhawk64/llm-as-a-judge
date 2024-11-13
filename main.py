from openai import OpenAI
import openai
import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Replace with your actual API key
openai.api_key = os.getenv("OPENAI_API_KEY")


client = OpenAI()

with open("sample-dataset.json", "r") as f:
    logs = f.read()

with open("sample-metadata.json", "r") as f:
    metadata = f.read()

completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[{
        "role": "system",
        "content": "You are designed to only respond with correlations you find in user's input. The user's input consists of logs and metadata. The logs consist of simple set of json data of an output and expected output (with other relevant information). The metadata is a json array of agents and what they are good for."
    }, {
        "role": "user",
        "content": f"Logs: {logs}\nMetadata: {metadata}"
    }])

content = completion.choices[0].message.content
with open("output.md", "w") as f:
    f.write(content)
