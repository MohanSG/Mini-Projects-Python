from selenium import webdriver
from selenium.webdriver.common.by import By
from pprint import pprint

driver = webdriver.Firefox()
driver.get("https://www.python.org/")

events_section = driver.find_element(By.XPATH, "/html/body/div/div[3]/div/section/div[2]/div[2]/div/ul")
events = events_section.find_elements(By.TAG_NAME, "li")

events_list = {}

for n in range(len(events)):
    event_split = events[n].text.split("\n")
    events_list[n] = {
        "time":event_split[0],
        "event":event_split[1],
    }

pprint(events_list)