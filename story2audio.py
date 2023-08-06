import os
import requests
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())

url = os.getenv('TEXT2SPEECH_URL')
key = os.getenv('HUGGINGFACEHUB_API_TOKEN')

headers = {"Authorization": f"Bearer {key}"}


def text2speech(payload):
    response = requests.post(url, headers=headers, json=payload)

    with open('output.flac', 'wb') as f:
        file = f.write(response.content)
