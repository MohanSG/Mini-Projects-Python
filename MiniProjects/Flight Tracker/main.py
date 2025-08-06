#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from flight_search import FlightSearch
from flight_data import get_cheapest_flight, FlightData
from data_manager import DataManager
from notification_manager import NotificationManager
import time

fs = FlightSearch()
dm = DataManager()
nm = NotificationManager()

for data in dm.sheet_data:
    if data['iataCode'] == '':
        city = data['city']
        iata_code = fs.get_iata_data(city)
        data['iataCode'] = iata_code
        dm.populate_iata_field(iata_code, data['id'])


for destination in dm.sheet_data:
    print(f"Gathering flights for {destination['city']}...")
    flights = fs.get_cheapest_flight_data(destination['iataCode'])
    cheapest_flight = get_cheapest_flight(flights)
    if cheapest_flight.price is None:
        print("No flight data")
    else:
        print(f"{destination['city']}: ¥{cheapest_flight.price}")
        time.sleep(2)
        if float(cheapest_flight.price) < float(destination['lowestPrice']):
            nm.send_sms(cheapest_flight)
