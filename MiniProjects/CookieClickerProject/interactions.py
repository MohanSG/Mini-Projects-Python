from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://en.wikipedia.org/")

welcome_section = driver.find_elements(By.CSS_SELECTOR, "#articlecount li")
for section in welcome_section:
    print(section.text)