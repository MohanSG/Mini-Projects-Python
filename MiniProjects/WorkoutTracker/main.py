import requests
import os
from dotenv import load_dotenv
from datetime import datetime

WEIGHT=82
HEIGHT=173
AGE=30

load_dotenv()

todays_date =  datetime.today().strftime('%Y-%m-%d')
current_time = datetime.now().strftime('%H:%M:%S')

NTX_URL="https://trackapi.nutritionix.com/v2/natural/exercise"
SHEET_URL = "https://api.sheety.co/af5eaca2b4e146a454d214ca5577ad1d/workOuts/workouts"

exercise = input("What exercise did you do?\n")

ntx_params = {
    "query" : exercise,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE,
}
ntx_headers = {
    "x-app-id" : os.environ["NTX_APP_ID"],
    "x-app-key": os.environ["NTX_API_KEY"],
    "Content-Type": "application/json",
}

ntx_response = requests.post(url=NTX_URL, json=ntx_params, headers=ntx_headers)
data = ntx_response.json()
exercise_done = data["exercises"][0]["name"]
calories_burned = data["exercises"][0]["nf_calories"]
duration = round(data["exercises"][0]["duration_min"])

print(f"You burned {calories_burned}!")

sheety_params = {
    "workout" :
        {
            "date" : todays_date,
            "time" : current_time,
            "exercise" : exercise_done.title(),
            "duration" : duration,
            "calories" : calories_burned
        }
}

sheety_headers = {
    "Authorization" : os.environ["SHEETY_API_KEY"],
}

sheety_response = requests.post(url=SHEET_URL, json=sheety_params, headers=sheety_headers)
print(sheety_response.text)
