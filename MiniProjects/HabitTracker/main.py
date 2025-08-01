import requests
from datetime import datetime

ENDPOINT = "https://pixe.la/v1/users"
USERNAME = "sparda"
TOKEN = "fdsflsdjfsldflskf"
PIXEL_URL = "https://pixe.la/v1/users/sparda/graphs/stepsgraph"

user_params= {
    "token" : TOKEN,
    "username" : USERNAME,
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes"
}

#response = requests.post(url=ENDPOINT, json=user_params)
#print(response.json())

graph_params = {
    "id" : "stepsgraph",
    "name": "My Steps!",
    "unit": "steps",
    "type": "int",
    "color": "sora"
}

headers  = {
    "X-USER-TOKEN": TOKEN
}

#response = requests.post(url=f"{ENDPOINT}/{USERNAME}/graphs", json=graph_params, headers=headers)
#print(response.text)

todays_date = datetime.today().strftime("%Y%m%d")
pixel_params = {
    "date": todays_date,
    "quantity": "10285",
}

pixel_headers = {
    "X-USER-TOKEN": TOKEN
}

#response = requests.post(url=PIXEL_URL, json=pixel_params, headers=pixel_headers)
#print(response.text)

pixel_update_params = {
    "quantity" : "13589"
}

pixel_update_headers = {
    "X-USER-TOKEN" : TOKEN
}

response = requests.put(url=f"{PIXEL_URL}/{todays_date}", json=pixel_update_params, headers=pixel_update_headers)
print(response.text)