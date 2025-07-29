import os
import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient



account_sid = "ACc1355eb238611ba7d34dff0039898116"
auth_token = "2d0ada8f3cffafc72ed8a90fd9c61a0b"

API_URL="http://api.openweathermap.org/data/2.5/forecast"
API_KEY = "90aa2fd2df073b9c94becc456fed4f4e"
parameters = {
    "lon" : 116.407394,
    "lat": 39.904202,
    "appid": API_KEY,
    "cnt": 4
}

response = requests.get(API_URL, params=parameters)
response.raise_for_status()

will_rain = False

data = response.json()
print(data)
for forecast in data["list"]:
    for w in forecast["weather"]:
        if w["id"] < 700:
            will_rain = True

if will_rain:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}

    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages.create(
        body="It's going to rain today, bring an umbrella",
        from_="+447427813105",
        to="+447432088793",
    )
    print(message.status)