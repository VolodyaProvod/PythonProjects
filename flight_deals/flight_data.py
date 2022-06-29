import requests
import datetime

FLIGHT_ENDPOINT = "https://tequila-api.kiwi.com/v2/search"
API = "4JI9jpky0_XTMvKyvsJo4670FSfHIZPV"

header = {
    "apikey": API
}

class FlightData:

    def __init__(self):
        self.fly_from = "LON"
        self.date_from = (datetime.date.today() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
        self.date_to = (datetime.date.today() + datetime.timedelta(days=181)).strftime('%d/%m/%Y')

    def search_price(self, city_code):

        query = {
            "fly_from": self.fly_from,
            "fly_to": city_code,
            "date_from": self.date_from,
            "date_to": self.date_to,
            "curr": "GBP"
        }

        response = requests.get(
            url=FLIGHT_ENDPOINT,
            params=query,
            headers=header
        )
        result = response.json()
        return result