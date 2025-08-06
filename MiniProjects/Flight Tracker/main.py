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

def display_prices(destination, cheapest_price, sheety_price, cheapest_flight):
    print(f"{destination}: ¥{cheapest_price}")
    time.sleep(2)
    if float(cheapest_price) < float(sheety_price):
        print("Sending sms....")
        #nm.send_sms(cheapest_flight)
        print("Sending emails...")
        emails = dm.get_user_emails()
        for email in emails:
            nm.send_email(email, cheapest_flight)

for destination in dm.sheet_data:
    print(f"Gathering flights for {destination['city']}...")
    flights = fs.get_cheapest_flight_data(destination['iataCode'])
    cheapest_flight = get_cheapest_flight(flights)
    if cheapest_flight.price is None:
        print("No flight data, checking indirect flights...")
        stopover_flights = fs.get_cheapest_flight_data(destination['iataCode'], is_direct=False)
        cheapest_flight = get_cheapest_flight(stopover_flights)
        if cheapest_flight.price is not None:
            display_prices(destination['city'], cheapest_flight.price, destination['lowestPrice'],
                           cheapest_flight=cheapest_flight)
        else:
            print(f"Couldn't find direct or indirect flights for {destination['city']}")

    else:
        display_prices(destination['city'], cheapest_flight.price, destination['lowestPrice'], cheapest_flight=cheapest_flight)