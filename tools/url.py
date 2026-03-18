from selenium.webdriver.common.window import WindowTypes
import logging

logger = logging.getLogger(__name__)


def open_new_tab(driver, url):
    try:
        driver.switch_to.new_window(WindowTypes.TAB)
        driver.get(url)
        logger.info(f"New tab opened {driver.current_url}")
        return True
    except Exception as e:
        logger.error(e)
        return False


def open_new_window(driver, url):
    try:
        driver.switch_to.new_window(WindowTypes.WINDOW)
        driver.get(url)
        logger.info(f"New window opened {driver.current_url}")
        return True
    except Exception as e:
        logger.error(e)
        return False


def close_current_tab(driver):
    try:
        driver.close()
        logger.info(f"Current tab closed {driver.current_url}")
        return True
    except Exception as e:
        logger.error(e)
        return False


def switch_to_tab(driver, tab_index):
    try:
        driver.switch_to.window(driver.window_handles[tab_index])
        logger.info(f"Switched to tab {tab_index}")
        return True
    except Exception as e:
        logger.error(e)
        return False


def switch_to_tab_by_url(driver, url):
    try:
        original_handle = driver.current_window_handle
        for handle in driver.window_handles:  # iterate every open tab
            driver.switch_to.window(handle)  # switch to it
            current = driver.current_url  # read its URL
            if current.startswith(url) or url.startswith(current.rstrip("/")):
                logger.info(f"Switched to tab with URL: {current}")
                return True  # stay on this tab ✅
        # no tab matched — go back to where we started
        driver.switch_to.window(original_handle)
        logger.error(f"Tab with URL '{url}' not found")
        return False
    except Exception as e:
        logger.error(e)
        return False
