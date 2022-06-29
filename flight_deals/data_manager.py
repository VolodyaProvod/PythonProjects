import requests


SHEETY_ENDPOINT = "https://api.sheety.co/acba35c1678e1d110faa708a67d3ca5e/flightDeals/prices"
TOKEN = "Bearer Lefrlf,rg,rognuenfe"
sheety_header = {
    "Authorization": TOKEN,
}

class DataManager:
    def __init__(self):
        self.destination_data = {}

    def get_data(self):
        response = requests.get(url=SHEETY_ENDPOINT, headers=sheety_header)
        self.destination_data = response.json()['prices']
        return self.destination_data

    def put_data(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_ENDPOINT}/{city['id']}",
                json=new_data,
                headers=sheety_header
            )
