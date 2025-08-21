from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("https://secure-retreat-92358.herokuapp.com/")

first_name_textbox = driver.find_element(By.NAME, "fName")
first_name_textbox.send_keys("Mohan")

second_name_textbox = driver.find_element(By.NAME, "lName")
second_name_textbox.send_keys("Singh")

email_textbox = driver.find_element(By.NAME, "email")
email_textbox.send_keys("mohansg12@gmail.com")

email_textbox.send_keys(Keys.ENTER)
