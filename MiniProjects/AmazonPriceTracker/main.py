from bs4 import BeautifulSoup
import requests
import smtplib
from dotenv import load_dotenv
import os

load_dotenv()
def send_email(product_name, product_price, url):
    try:
        with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=os.environ['EMAIL'], password="APP_PASS")
            connection.sendmail(from_addr=os.environ['EMAIL'],
                                to_addrs=os.environ['EMAIL'],
                                msg=f"Subject: Amazon Price Tracker\n\nPrice of {product_name} is now {product_price}\nLink: {url}")
    except TimeoutError:
        print("TIMEOUT ERROR: Seems you have a connection issue. Please try again later.")
    else:
        print("Email sent!")

product_link = input("Enter an amazon link:\n")
header = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:141.0) Gecko/20100101 Firefox/141.0"
}
print("Scraping page...")
response = requests.get(product_link, headers=header)
amazon_listing = response.text

soup = BeautifulSoup(amazon_listing, "html.parser")
listing_title = soup.find("span", id="productTitle").get_text()
listing_price = soup.find("span", class_="a-price-whole").get_text()+soup.find("span", class_="a-price-fraction").get_text()

if float(listing_price) < 400.00:
    print("DEAL FOUND! Sending email...")
    send_email(listing_title, listing_price, product_link)