#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from flight_search import FlightSearch
from data_manager import DataManager

fs = FlightSearch()
#dm = DataManager()

# for data in dm.sheet_data:
#     if data['iataCode'] == '':
#         city = data['city']
#         iata_code = fs.get_iata_data(city)
#         data['iataCode'] = iata_code
#         dm.populate_iata_field(iata_code, data['id'])
#     else:
#         print(f"IATA code exists for {data['city']}")

cheap_flights = fs.get_cheapest_flight_data("PAR")
print(cheap_flights)