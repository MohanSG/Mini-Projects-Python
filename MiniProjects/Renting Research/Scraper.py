from bs4 import BeautifulSoup
import requests

class Scraper:
    def __init__(self, zillow_link):
        soup = None
        headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:142.0) Gecko/20100101 Firefox/142.0',
                   'Accept-Encoding' : 'gzip, deflate, br, zstd',
                   'Accept-Language' : 'en-US,en;q=0.5',
                   'Connection' : 'keep-alive',
                   'Content-Type' : 'application/json'}

        response = requests.get(zillow_link, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        self.listings = self.find_listings(soup)

    def find_listings(self, soup:BeautifulSoup):
        all_homes = []
        listings_classnames = "List-c11n-8-109-3__sc-1smrmqp-0 StyledSearchListWrapper-srp-8-109-3__sc-14brvob-0 ffjqkg kyEqXS photo-cards photo-cards_extra-attribution"
        homes_classnames = "ListItem-c11n-8-109-3__sc-13rwu5a-0 StyledListCardWrapper-srp-8-109-3__sc-r47yyl-0 gnrjeR exoArO"
        listings = soup.find(name="ul", class_=listings_classnames.split(" "))
        homes = listings.find_all(name="li", class_=homes_classnames.split(" "))

        for home in homes:
            if home.text != "LoadingLoading...":
                new_dict = {
                    "address" : home.find(name="a", class_="StyledPropertyCardDataArea-c11n-8-109-3__sc-10i1r6-0 jchoRr property-card-link".split(" ")).text,
                    "price" : f"${home.find(name="span", class_="PropertyCardWrapper__StyledPriceLine-srp-8-109-3__sc-16e8gqd-1 jCoXOF".split(" ")).text.split("$")[1]}",
                    "link" : home.find(name="a", class_="StyledPropertyCardDataArea-c11n-8-109-3__sc-10i1r6-0 jchoRr property-card-link".split(" "))['href']
                }

                all_homes.append(new_dict)

        print(all_homes)
        return all_homes
