import requests
from dotenv import load_dotenv
import os
load_dotenv()

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.sheet_data = self.get_flight_data()
        print(self.sheet_data)

    def get_flight_data(self):
        endpoint = "https://api.sheety.co/af5eaca2b4e146a454d214ca5577ad1d/flightDeals/prices"
        headers = {
            "Authorization": os.environ["SHEETY_API_KEY"]
        }
        response = requests.get(endpoint, headers=headers)
        return response.json()['prices']

    def populate_iata_field(self, city_codes, city_id):
        put_endpoint = f"https://api.sheety.co/af5eaca2b4e146a454d214ca5577ad1d/flightDeals/prices/{city_id}"
        params = {
            "price" :
            {
                "iataCode": city_codes
            }
        }

        headers = {
            "Authorization": os.environ["SHEETY_API_KEY"]
        }

        response = requests.put(url=put_endpoint, json=params, headers=headers)
        print(response.text)