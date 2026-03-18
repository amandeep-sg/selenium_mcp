import logging
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

logger = logging.getLogger(__name__)


def scroll_to_bottom(driver):
    try:
        element_text = [
            "Copyright",
            "©",
            "copyright",
            "footer",
            "All rights reserved",
            "(c)",
            "(C)",
        ]
        for text in element_text:
            elements = driver.find_elements(By.XPATH, f"//*[contains(text(),'{text}')]")
            if len(elements) != 0:
                ActionChains(driver).move_to_element(elements[0]).perform()
                break
        return True
    except Exception as e:
        logger.error(f"Failed to scroll to bottom: {e}")
        return False


def scroll_to_top(driver):
    try:
        driver.execute_script("window.scrollTo(0, 0)")
        logger.info("Scrolled to top")
        return True
    except Exception as e:
        logger.error(f"Failed to scroll to top: {e}")
        return False
