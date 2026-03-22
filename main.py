from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import base64
import time

options = Options()
options.add_argument("--headless")

driver = webdriver.Chrome(options=options)
driver.get("https://rfpnotification.com")
element = driver.find_element(By.XPATH, "//*[contains(text(),'submit')]")
print(element.get_attribute("tag"))
time.sleep(5)
driver.quit()
