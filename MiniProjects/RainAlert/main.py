import os
import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient



account_sid = "ACCOUNT_SID_GOES_HERE"
auth_token = "AUTH_TOKEN_GOES_HERE"

API_URL="http://api.openweathermap.org/data/2.5/forecast"
API_KEY = "API_KEY_GOES_HERE"
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