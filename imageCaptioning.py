import requests
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

hf_key = os.getenv('HUGGINGFACEHUB_API_TOKEN')
url = os.getenv('IMAGE_CAPTIONING_URL')

headers = {"Authorization": f"Bearer {hf_key}"}


def imageCaptioning(path):
    with open(path, "rb") as f:
        data = f.read()
    response = requests.post(url=url, headers=headers, data=data)
    return response.json()[0]['generated_text']

# people wearing face masks walking down a long hallway with people wearing masks