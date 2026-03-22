import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from fastmcp.tools import tool
from fastmcp import Context

logger = logging.getLogger(__name__)

global _driver

options = Options()
# options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")


@tool(
    description="create instance of chrome webdriver",
    tags={"manage webdriver", "chrome"},
)
async def initialize_driver(ctx: Context):
    global _driver
    try:
        _driver = webdriver.Chrome(options=options)
        logger.info("Driver initialized")
        return True
    except Exception as e:
        logger.error(f"Failed to initialize driver: {e}")
        return False


@tool(description="close the browser", tags={"manage browser", "browser automation"})
async def close_driver(ctx: Context):
    try:
        _driver.quit()
        logger.info("Driver closed")
        return True
    except Exception as e:
        logger.error(f"Failed to close driver: {e}")
        return False


def get_driver():
    return _driver
