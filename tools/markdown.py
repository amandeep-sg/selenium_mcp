from markdownify import markdownify as md
from selenium.webdriver.common.by import By
import logging

logger = logging.getLogger(__name__)


def save_markdown(driver):
    try:
        html_content = driver.find_element(By.TAG_NAME, "body").get_attribute(
            "innerHTML"
        )
        with open("website.md", "w", encoding="utf-8") as f:
            f.write(md(html_content))
            logger.info("Saved markdown to website.md")
            return True
    except Exception as e:
        logger.error(f"Failed to save markdown: {e}")
        return False
