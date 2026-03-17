from selenium.webdriver.common.print_page_options import PrintOptions
import base64
import logging

logger = logging.getLogger(__name__)


def print_to_pdf(driver):
    try:
        print_options = PrintOptions()

        print_options.orientation = "portrait"
        print_options.scale = 0.8
        print_options.background = True

        base64_pdf = driver.print_page(print_options)

        with open("website.pdf", "wb") as f:
            f.write(base64.b64decode(base64_pdf))
        logger.info("Saved PDF to website.pdf")
        return True
    except Exception as e:
        logger.error(f"Failed to print to PDF: {e}")
        return False
