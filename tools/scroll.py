import logging

logger = logging.getLogger(__name__)


def scroll_to_bottom(driver):
    try:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        logger.info("Scrolled to bottom of page")
        return True
    except Exception as e:
        logger.error(f"Failed to scroll to bottom: {e}")
        return False
