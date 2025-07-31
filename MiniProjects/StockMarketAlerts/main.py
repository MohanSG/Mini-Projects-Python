import os
from datetime import datetime, timedelta
import requests
from dotenv import load_dotenv
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
load_dotenv()

def send_sms(message_to_send):
    account_sid = os.environ["TW_ACC_SID"]
    auth_token = os.environ["TW_AUTH_TOKEN"]

    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}

    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages.create(
        body=message_to_send,
        from_="+447427813105",
        to="+447432088793",
    )
    print(message.status)

def get_news(company, from_date, to_date):
    news_url = "https://newsapi.org/v2/everything"
    response = requests.get(news_url, params={
        "apikey": os.environ["NEWS_API_KEY"],
        "language": "en",
        "q": company,
        "sortBy": "popularity",
        "from": from_date,
        "to": to_date,
    })
    data = response.json()
    return data

def calculate_percentage_change(num1, num2):
    perc_change = ((num2 - num1) / num1) * 100
    return perc_change

def get_stocks(stock):
    stocks_url = 'https://www.alphavantage.co/query'
    response = requests.get(stocks_url, params={
        "apikey": os.environ["AA_API_KEY"],
        "function": "TIME_SERIES_DAILY",
        "symbol": stock
    })
    data = response.json()
    return data

stocks_data = get_stocks(STOCK)

date_today = (datetime.today() - timedelta(days=1)).strftime("%Y-%m-%d")#Adjusted for current timezone
date_yesterday = (datetime.today() - timedelta(days=2)).strftime("%Y-%m-%d")

todays_close = float(stocks_data["Time Series (Daily)"][date_today]["4. close"])
yester_close = float(stocks_data["Time Series (Daily)"][date_yesterday]["4. close"])

# perc_diff = calculate_percentage_change(todays_close, yester_close)
perc_diff = 9.3432344
if perc_diff > 5 or perc_diff < -5:
    message_body = None
    news = get_news(COMPANY_NAME, date_today, date_yesterday)
    top_news = {}
    for i in range(3):
        news_title = news["articles"][i]["title"]
        news_description = news["articles"][i]["description"]
        top_news.update({news_title: news_description})

        if perc_diff < 0:
            message_body = f"{STOCK}: 🔻{round(perc_diff)}%\n"
        elif perc_diff > 0:
            message_body = f"{STOCK}: 🔺{round(perc_diff)}%\n"
        for key, value in top_news.items():
            message_body += f"Headline: {key}\nBrief:{value}\n\n"
    send_sms(message_body)
## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

