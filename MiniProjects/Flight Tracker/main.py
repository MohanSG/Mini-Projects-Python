#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from flight_search import FlightSearch
from data_manager import DataManager

fs = FlightSearch()
dm = DataManager()

for data in dm.sheet_data:
    if data['iataCode'] == '':
        fs.get_iata_data(data['iataCode'])

print(fs.city_codes)