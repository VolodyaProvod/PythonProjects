import requests
import os
from twilio.rest import Client
from datetime import date, timedelta
from newsapi import NewsApiClient


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
TWILIO_ACCOUNT_SID = "AC14b99efdc8175b69c736289dcce704b3"
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_TOKEN") #Security 😎
MY_NUMBER = os.environ.get("MY_NUMBER") #Security 😎
ALPHAVANTAGE_API_KEY = "RQZUOCDIA7BQEDOO"
ALPHAVANTAGE_ENDPOINT = "https://www.alphavantage.co/query?"
NEWS_API_KEY = "7349beaf4d7b4510bd21c1ae02e7f68e"


def past_date_in_string(days_ago):
    yesterday_date = date.today() - timedelta(days=days_ago)
    yesterday_date.strftime('%y-%m-%d')
    return str(yesterday_date)


def get_change(current, previous):
    if current == previous:
        return 0
    try:
        return ((current - previous) / previous) * 100.0
    except ZeroDivisionError:
        return float('inf')


stok_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": ALPHAVANTAGE_API_KEY,
    "outputsize": "compact",
}
response = requests.get(url=ALPHAVANTAGE_ENDPOINT, params=stok_parameters)
response.raise_for_status()


data_yestadray = float(response.json()["Time Series (Daily)"][past_date_in_string(1)]["4. close"])
data_before_yestadray = float(response.json()["Time Series (Daily)"][past_date_in_string(2)]["4. close"])
changes_on_the_exchange = round(get_change(data_yestadray, data_before_yestadray), 2)
text = f"{STOCK}: "
if changes_on_the_exchange > 0:
    text += f"🔺{abs(changes_on_the_exchange)}"
else:
    text += f"🔻{abs(changes_on_the_exchange)}"

newsapi = NewsApiClient(api_key=NEWS_API_KEY)
all_articles = newsapi.get_everything(q=COMPANY_NAME,
                                      from_param=past_date_in_string(1),
                                      language='en',
                                      sort_by='relevancy',
                                      page=1)
text += f"\n" \
        f"Headline: {all_articles['articles'][0]['title']}\n" \
        f"Brief: {all_articles['articles'][0]['content']}\n\n" \
        f"Headline: {all_articles['articles'][1]['title']}\n" \
        f"Brief: {all_articles['articles'][1]['content']}"

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
message = client.messages \
        .create(
        body=text,
        from_='+15592457339',
        to=MY_NUMBER
    )
print(message.status)
