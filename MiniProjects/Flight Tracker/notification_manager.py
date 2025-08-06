import os
from flight_data import FlightData
from dotenv import load_dotenv
from twilio.rest import Client
import smtplib

load_dotenv()
class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.account_sid = os.environ["TW_ACC_SID"]
        self.auth_token = os.environ["TW_AUTH_TOKEN"]

    def send_sms(self, flight: FlightData):

        client = Client(self.account_sid, self.auth_token)
        message = client.messages.create(
            body=f"Low price alert! Only ¥{flight.price} to fly from {flight.origin} to {flight.destination}, on "
                 f"{flight.out_date} until {flight.return_date}",
            from_=os.environ["TW_NUMBER"],
            to=os.environ["MOB_NUMBER"],
        )

        print(message.status)

    def send_email(self, email, flight: FlightData):
        try:
            with (smtplib.SMTP("smtp.gmail.com", 587)) as connection:
                connection.starttls()
                connection.login(user=os.environ['MY_EMAIL'], password=os.environ['SMTP_PASS'])
                connection.sendmail(
                    from_addr=os.environ['MY_EMAIL'],
                    to_addrs=email,
                    msg=f"Low price alert! Only CNY{flight.price} from {flight.origin} to {flight.destination}, "
                        f"with {flight.stops} stop(s) on {flight.out_date} and returning on {flight.return_date}"
                )
        except TimeoutError:
            print(f"Connection timed out, couldn't send email to {email}")
