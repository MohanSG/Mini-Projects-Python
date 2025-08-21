from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
driver.get("https://ozh.github.io/cookieclicker/")

def get_big_cookie():
    return driver.find_element(By.ID, "bigCookie")

def choose_product(number_of_cookies):#Loop through products and choose the most expensive one to buy. product(n)
    for n in range(10)[::-1]:
        print(f"product {n}")
        product = driver.find_element(By.CSS_SELECTOR, f"product{n} .price")
        if int(product.text) < number_of_cookies:
            return product
        else:
            time.sleep(1)

    return None

cookie_amount = 0
cursor = 0

time.sleep(5)#Wait for js message to go away
big_cookie = get_big_cookie()

timeout = 10*1

while cookie_amount < 1000000:
    timeout_start = time.time()
    while time.time() < timeout_start + timeout:
        big_cookie.click()

    cookie_amount = int(driver.find_element(By.ID, "cookies").text.split(" ")[0])
    cursor = choose_product(cookie_amount)
    print(f"Current cookies: {cookie_amount}\nCursor price: {cursor.text}")

    if int(cursor.text) < cookie_amount:
        cursor.click()
        time.sleep(1)