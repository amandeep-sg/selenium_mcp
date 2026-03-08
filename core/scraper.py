from selenium import webdriver
import logging

driver = webdriver.Chrome()
driver.get("https://www.perfios.ai")
logging.info(driver.title)
driver.quit()
