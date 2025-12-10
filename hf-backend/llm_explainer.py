import requests
import os

# Read token from environment variable
HF_TOKEN = os.getenv("HF_TOKEN")

API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2"

def explain_prediction(fruit, info):
    prompt = f"""
    Explain the following fruit in a simple, friendly way:

    Fruit: {fruit}
    Info: {info}

    Provide a short, student-friendly explanation (3–4 lines).
    """

    headers = {"Authorization": f"Bearer {HF_TOKEN}"}
    payload = {"inputs": prompt}

    response = requests.post(API_URL, headers=headers, json=payload)

    try:
        return response.json()[0]["generated_text"]
    except:
        return "The model was unable to generate an explanation at this time."
