from dotenv import load_dotenv
import os
import requests
from datetime import datetime

load_dotenv()
class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.client_id = os.environ["AMAD_CLIENT_ID"]
        self.client_secret = os.environ["AMAD_CLIENT_SECRET"]

    def get_access_token(self):
        auth_endpoint = "https://test.api.amadeus.com/v1/security/oauth2/token"
        params = {
            "grant_type": "client_credentials",
            "client_id": self.client_id,
            "client_secret": self.client_secret
        }
        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        response = requests.post(url=auth_endpoint, data=params, headers=headers)
        data = response.json()
        access_token = f"{data['token_type']} {data['access_token']}"
        return access_token

    def get_iata_data(self, city_name):
        location_endpoint = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
        access_token = self.get_access_token()

        params = {
            "keyword": city_name,
            "max": 1
        }

        headers = {
            "Authorization": access_token
        }

        try:
            response = requests.get(url=location_endpoint, params=params, headers=headers)
            r = response.json()
            data = r['data'][0]
        except KeyError:
            print(r)
        else:
            return data['iataCode']

    def get_cheapest_flight_data(self, destination):
        departure_date = datetime.today().strftime('%Y-%m-%d')
        cheapest_flights_endpoint = "https://test.api.amadeus.com/v2/shopping/flight-offers"
        access_token = self.get_access_token()

        params = {
            "originLocationCode" : "LHR",
            "destinationLocationCode" : destination,
            "departureDate" : departure_date, 
        }

        headers = {
            "Authorization": access_token
        }

        response = requests.get(url=cheapest_flights_endpoint, params=params, headers=headers)
        data = response.json()
        return data