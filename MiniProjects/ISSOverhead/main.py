import requests
from datetime import datetime
import smtplib

MY_LAT = 39.930840 # Your latitude
MY_LONG = 116.386337 # Your longitude
PASS=''

def check_distance():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if iss_latitude == MY_LAT+5 and iss_longitude == MY_LONG+5 or iss_latitude == MY_LAT-5 and iss_longitude == MY_LONG-5:
        return True
    else:
        return False

def send_email():
    my_email = "mohansg12@gmail.com"
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
        connection.starttls()
        connection.login(user=my_email, password=PASS)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"Subject: Look up!\nThe ISS should be overhead"
        )

#Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

if check_distance():
    if datetime.now().hour > sunset or datetime.now().hour < sunrise:
        send_email()

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



