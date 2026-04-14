import undetected_chromedriver as uc
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import os

class InternetSpeedTwitterBot:
    def __init__(self):
        self.actual_download_speed = None
        self.actual_upload_speed = None

        chrome_options = uc.ChromeOptions()
        user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
        chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

        self.driver = uc.Chrome(options=chrome_options, enable_cdp_events=True)

    def get_internet_speed(self):
        #Start up speed test website
        self.driver.get("https://www.speedtest.net/")

        #Wait for the mainpage to load
        mainpage_wait = WebDriverWait(self.driver, 10, poll_frequency=0.2)
        mainpage_wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "start-text")))
        print("CONFIRMED: speedtest.net main page loaded")

        #Find the GO button and click to start testing speed
        speed_test_button = self.driver.find_element(By.CLASS_NAME, "start-text")
        speed_test_button.click()
        print("Testing speed....")

        #Wait for speed test results to complete, then display and store results
        results_wait = WebDriverWait(self.driver, 60, poll_frequency=1)
        results_wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.result-area.result-area-nav.result-area-nav-right")))
        print("Getting download speeds....")
        self.actual_download_speed = self.driver.find_element(By.CSS_SELECTOR, "span.result-data-large.number.result-data-value.download-speed").text
        self.actual_upload_speed = self.driver.find_element(By.CSS_SELECTOR, "span.result-data-large.number.result-data-value.upload-speed").text
        print(f"Download speed is {self.actual_download_speed} Mbp/s")
        print(f"Upload speed is {self.actual_upload_speed} Mbp/s")

    def tweet_at_provider(self):
        #Start up twitter
        self.driver.get("https://x.com/home")

        #Wait for twitter to fully load
        twitter_wait = WebDriverWait(self.driver, 5, poll_frequency=0.2)
        twitter_wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.public-DraftStyleDefault-block.public-DraftStyleDefault-ltr")))

        #Find the textbox for posting content and fill with speed test data
        post_box = self.driver.find_element(By.CSS_SELECTOR, "div.public-DraftStyleDefault-block.public-DraftStyleDefault-ltr")
        post_box.send_keys(f"SPEEDTEST RESULTS:\nDownload Speed: {self.actual_download_speed}\nUpload Speed:  {self.actual_upload_speed}")

        #Use action keys to press CTRL+ENTER and post speed test data
        actions = ActionChains(self.driver)
        actions.key_down(Keys.CONTROL).send_keys(Keys.ENTER).key_up(Keys.CONTROL).perform()