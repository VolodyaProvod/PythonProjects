import requests
from datetime import datetime
import os

API_ID = os.environ.get("API_ID") #Security 😎
API_KEY = os.environ.get("API_KEY") #Security 😎
SHEETY_ENDPOINT = os.environ.get("SHEETY_ENDPOINT") #Security 😎
TOKEN = os.environ.get("TOKEN") #Security 😎
NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise/"

today = datetime.now().strftime('%d/%m/%Y')
time = datetime.now().time().strftime('%H:%M:%S')
text = input("Tell me which exercises you did: ").title()

nutritionix_header = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0",
}

params = {
    "query": text,
}

sheety_header = {
    "Authorization": TOKEN,
}

response = requests.post(url=NUTRITIONIX_ENDPOINT, headers=nutritionix_header, json=params)
response.raise_for_status()
exercises = response.json()["exercises"]

for index in range(len(exercises)):
    data_json = {
        "workout": {"date": today,
                    "time": time,
                    "exercise": exercises[index]["name"].title(),
                    "duration": exercises[index]["duration_min"],
                    "calories": exercises[index]["nf_calories"],
                    }
    }
    response = requests.post(url=SHEETY_ENDPOINT, json=data_json, headers=sheety_header)
    response.raise_for_status()
