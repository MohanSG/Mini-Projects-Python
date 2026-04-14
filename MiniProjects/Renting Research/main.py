from Scraper import Scraper
from SheetFiller import SheetFiller

GOOGLE_SHEET_LINK = "https://docs.google.com/forms/d/e/1FAIpQLScr7WoUeEAoMxa34pwe7W8Ap67Bk_9FZFR0TE7l_Om1v9srtQ/viewform?usp=dialog"
ZILLOW_LINK = "https://www.zillow.com/san-francisco-ca/houses/?category=SEMANTIC&searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22isMapVisible%22%3Atrue%2C%22listPriceActive%22%3Afalse%2C%22mapBounds%22%3A%7B%22west%22%3A-122.75289623563287%2C%22east%22%3A-122.21319286649225%2C%22south%22%3A37.578351443921555%2C%22north%22%3A37.90197587861192%7D%2C%22mapZoom%22%3A11%2C%22usersSearchTerm%22%3A%22San%20Francisco%20CA%22%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%7D%5D%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22beds%22%3A%7B%22min%22%3A1%2C%22max%22%3Anull%7D%2C%22tow%22%3A%7B%22value%22%3Afalse%7D%2C%22mf%22%3A%7B%22value%22%3Afalse%7D%2C%22con%22%3A%7B%22value%22%3Afalse%7D%2C%22land%22%3A%7B%22value%22%3Afalse%7D%2C%22apa%22%3A%7B%22value%22%3Afalse%7D%2C%22manu%22%3A%7B%22value%22%3Afalse%7D%2C%22apco%22%3A%7B%22value%22%3Afalse%7D%2C%22mcp%22%3A%7B%22min%22%3Anull%2C%22max%22%3A5000%7D%7D%2C%22isListVisible%22%3Atrue%7D"
SPREADSHEET_LINK = "https://docs.google.com/spreadsheets/d/19RN9F7NUK2Fizn3vLdBrqGQ4tbQy3_TOjnGDpnn_vjA/edit?usp=sharing"

def main():
    scraper = Scraper(ZILLOW_LINK)
    sheet_filler = SheetFiller(scraper.listings, GOOGLE_SHEET_LINK, SPREADSHEET_LINK)

if __name__ == "__main__":
    main()