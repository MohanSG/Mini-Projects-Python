from dotenv import load_dotenv
import os
import requests

load_dotenv()
class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.client_id = os.environ["AMAD_CLIENT_ID"]
        self.client_secret = os.environ["AMAD_CLIENT_SECRET"]
        self.auth_endpoint = "https://test.api.amadeus.com/v1/security/oauth2/token"
        self.location_endpoint = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
        self.city_codes = {}

    def get_access_token(self):
        params = {
            "grant_type": "client_credentials",
            "client_id": self.client_id,
            "client_secret": self.client_secret
        }
        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        response = requests.post(url=self.auth_endpoint, data=params, headers=headers)
        data = response.json()
        access_token = f"{data['token_type']} {data['access_token']}"
        return access_token

    def get_iata_data(self, city_name):
        access_token = self.get_access_token()

        params = {
            "keyword": city_name,
            "max": 1
        }

        headers = {
            "Authorization": access_token
        }

        response = requests.get(url=self.location_endpoint, params=params, headers=headers)
        r = response.json()
        data = r['data'][0]
        self.city_codes.update({data['name']: data['iataCode']})
        print(self.city_codes)