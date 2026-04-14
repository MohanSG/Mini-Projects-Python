import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
import os
import time

class InstaFollower:
    def __init__(self, target_account):
        self.target_account = target_account
        chrome_options = uc.ChromeOptions()
        user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
        chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

        self.driver = uc.Chrome(options=chrome_options, enable_cdp_events=True)

    def find_followers(self):
        self.driver.get(f"https://www.instagram.com/{self.target_account}/")
        wait = WebDriverWait(self.driver, 5, poll_frequency=0.2)

        account_data_selectors = self.format_selector("li","xl565be x11gldyt x1pwwqoy x1j53mea")
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, account_data_selectors)))
        account_data = self.driver.find_elements(By.CSS_SELECTOR, account_data_selectors)
        account_data[2].click()

        popup_selector = self.format_selector("div", "x6nl9eh x1a5l9x9 x7vuprf x1mg3h75 x1lliihq x1iyjqo2 xs83m0k xz65tgg x1rife3k x1n2onr6")

        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, popup_selector)))
        scroll = self.driver.find_element(By.CSS_SELECTOR, popup_selector)
        scroll_count = 10
        while scroll_count > 0:
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scroll)
            scroll_count -= 1
            time.sleep(1)

        self.driver.execute_script("arguments[0].scrollTop = -arguments[0].scrollHeight", scroll)

        followers_selector = self.format_selector("div", "x1qnrgzn x1cek8b2 xb10e19 x19rwo8q x1lliihq x193iq5w xh8yej3")
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, followers_selector)))
        followers = self.driver.find_elements(By.CSS_SELECTOR, followers_selector)

        self.follow(followers)

    def follow(self, followers):
        for follower in followers:
            follow_button = follower.find_element(By.CSS_SELECTOR, self.format_selector("div", "_ap3a _aaco _aacw _aad6 _aade"))
            follow_button.click()
            time.sleep(1)

    def format_selector(self, element_type:str, element_tags:str):
        new_tags = element_tags.replace(" ", ".")
        print(element_type + '.' + new_tags)
        return element_type + '.' + new_tags