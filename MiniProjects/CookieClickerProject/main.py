from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
import time

geckodriver_path = "C:/WebDriver/bin/geckodriver.exe"
service = Service(executable_path = geckodriver_path)
driver = webdriver.Firefox(service=service)
driver.get("https://ozh.github.io/cookieclicker/")

def get_big_cookie():
    return driver.find_element(By.ID, "bigCookie")

def choose_product(number_of_cookies): #Loop through products and choose the most expensive one to buy. product(n)
    for n in range(11)[::-1]:
        product_name = driver.find_element(By.CSS_SELECTOR, f"#product{n} .content .title")
        product = driver.find_element(By.CSS_SELECTOR, f"#product{n} .price")
        price = product.text.replace(",", "")
        if int(price) < number_of_cookies:
            print(f"Buying: {product_name.text}")
            return product

    return None

def choose_upgrade():
    try:
        cookie_upgrades = driver.find_element(By.ID, "upgrades")
        cookie = cookie_upgrades.find_element(By.ID, "upgrade0")
    except Exception:
        print("No upgrades available")
        return None
    else:
        return cookie

def change_number_format(number_text):
    if ',' in number_text:
        new_number = int(number_text.replace(",", ""))
    else:
        new_number = int(cookie_amount_str)
    return new_number

cookie_amount = 0

time.sleep(5)#Wait for js message to go away
big_cookie = get_big_cookie()

timeout = 5

while cookie_amount < 1000000:
    timeout_start = time.time()
    while time.time() < timeout_start + timeout:
        big_cookie.click()

    upgrade = choose_upgrade()
    if upgrade is not None:
        print("Buying upgrade")
        upgrade.click()

    cookie_amount_info = driver.find_element(By.ID, "cookies")
    cookie_amount_str = cookie_amount_info.text.split(" ")[0]
    cookies_per_second = cookie_amount_info.text.split("\n")[1].split(" : ")[1]
    print(f"cookies/second {cookies_per_second}")

    cookie_amount_int = change_number_format(cookie_amount_str)

    product = choose_product(cookie_amount_int)
    if product is not None:
        product_number = change_number_format(product.text)
        product.click()
        time.sleep(1)
    else:
        print("Nothing to buy")