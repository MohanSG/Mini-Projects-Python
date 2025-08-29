from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc
import time
import os

chrome_options = uc.ChromeOptions()
user_data_dir = os.path.join(os.getcwd(),"chrome_profile")
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

driver = uc.Chrome(options=chrome_options, enable_cdp_events=True)

driver.maximize_window()
driver.get("https://www.tinder.com")

wait = WebDriverWait(driver, timeout=5, poll_frequency=.2)
wait.until(EC.visibility_of_element_located((By.ID, "main-content")))
print("Main page loaded")

body = driver.find_element(By.TAG_NAME, "body")

has_likes = True
while has_likes:
    body.send_keys(Keys.ARROW_RIGHT)
    try:
        no_more_likes = driver.find_element(By.XPATH, '//*[@id="c1595655701"]/div/div/div[3]')
    except NoSuchElementException:
        print("1 like used")
        time.sleep(1)
    else:
        has_likes = False
        print("No more likes...")
#//*[@id="c1595655701"]/div/div/div[3]

