import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC


def format_selector(element_type: str, element_tags: str):
    new_tags = element_tags.replace(" ", ".")
    return element_type + '.' + new_tags


class SheetFiller:

    def __init__(self, listings, sheet_link, spreadsheet_link):
        self.driver = uc.Chrome(enable_cdp_events=True)
        self.fill_sheet(listings, sheet_link, spreadsheet_link)

    def fill_sheet(self, listings, sheet_link, spreadsheet_link):
        self.driver.get(sheet_link)
        wait = WebDriverWait(self.driver, timeout=5, poll_frequency=0.2)

        for home in listings:
            questions = self.driver.find_elements(By.CSS_SELECTOR, format_selector("input", "whsOnd zHQkBf"))

            questions[0].send_keys(home['address'])
            questions[1].send_keys(home['price'])
            questions[2].send_keys(home['link'])
            self.driver.find_element(By.CSS_SELECTOR, format_selector("span", "NPEfkd RveJvd snByac")).click()

            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, format_selector("div", "c2gzEf"))))
            self.driver.find_element(By.CSS_SELECTOR, format_selector("div", "c2gzEf")).find_element(By.TAG_NAME, "a").click()
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, format_selector("input", "whsOnd zHQkBf"))))

        self.driver.get(spreadsheet_link)



