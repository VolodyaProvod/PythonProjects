#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from flight_data import FlightData
from data_manager import DataManager
from flight_search import FlightSearch

data_manager = DataManager()
flight_search = FlightSearch()

sheet_data = data_manager.get_data()
if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        if row["iataCode"] == '':
            row["iataCode"] = flight_search.get_destination_code(row["city"])

    data_manager.destination_data = sheet_data
    data_manager.put_data()

flight_data = FlightData()
print(flight_data.search_price("MOW"))