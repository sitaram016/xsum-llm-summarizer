import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def summarize_text(text):
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=f"Summarize the following text concisely:\n{text}"
    )
    return response.output_text
