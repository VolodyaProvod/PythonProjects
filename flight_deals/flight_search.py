import requests


FLIGHT_ENDPOINT = "https://tequila-api.kiwi.com/locations/query"
API = "4JI9jpky0_XTMvKyvsJo4670FSfHIZPV"
Flight = "nzL-8ju-JDe-8Yz"



class FlightSearch:


    def get_destination_code(self, city_name):
        query = {
            "term": city_name,
            "location_types": "city",
        }
        header = {
            "apikey": API,
        }
        response = requests.get(
            url=FLIGHT_ENDPOINT,
            params=query,
            headers=header
        )
        result = response.json()["locations"][0]["code"]
        return result


