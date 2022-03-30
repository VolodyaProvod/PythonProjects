import requests
import os
from twilio.rest import Client

API_KEY = os.environ.get("OVM_API_KEY") #Security 😎
MY_LAT = 53.849730  # Minsk
MY_LONG = 27.481230  # Minsk
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
TWILIO_ACCOUNT_SID = "AC14b99efdc8175b69c736289dcce704b3"
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_TOKEN") #Security 😎
MY_NUMBER = os.environ.get("MY_PHONE") #Security 😎


parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": API_KEY,
    "exclude": "current,minutely,daily"
}

response = requests.get(url=OWM_Endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()["hourly"][3:15]
is_rain = False

for weather in weather_data:
    if int(weather["weather"][0]["id"]) < 700:
        description = weather["weather"][0]["description"]
        text = f"There will be {description} today, take an umbrella with you ☂️"
        is_rain = True

if is_rain:
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    message = client.messages \
        .create(
        body=text,
        from_='+15592457339',
        to=MY_NUMBER
    )
    print(message.status)
