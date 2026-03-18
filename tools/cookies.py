from selenium.webdriver.common.by import By
import logging

logger = logging.getLogger(__name__)
logger.propagate = True


def accept_all_cookies(driver):
    try:
        elements = driver.find_elements(By.XPATH, "//*[starts-with(text(), 'Accept')]")
        elements[0].click()
        logger.info("Accepted all cookies")
        return len(elements)
    except Exception as e:
        logger.error(e)
        return 0


def get_all_cookies(driver):
    try:
        return driver.get_cookies()
    except Exception as e:
        logger.error(e)
        return []
