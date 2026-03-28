from tools.web_driver import get_driver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from fastmcp.tools import tool
from fastmcp import Context
import logging


# internal modules
from tools.web_driver import get_driver

logger = logging.getLogger(__name__)


@tool(
    description="left click on an element on the webpage",
    tags={"click", "browser automation"},
)
async def left_click(xpath: str, ctx: Context) -> bool:
    try:
        driver = get_driver()
        element = driver.find_element(By.XPATH, xpath)
        element.click()
        logger.info("Clicked on the element")
        return True
    except Exception as e:
        logger.error(f"Failed to click on the element: {e}")
        return False


@tool(
    description="right click on an element on the webpage",
    tags={"click", "browser automation"},
)
async def right_click(xpath: str, ctx: Context) -> bool:
    try:
        driver = get_driver()
        element = driver.find_element(By.XPATH, xpath)
        ActionChains(driver).context_click(element).perform()
        logger.info("Clicked on the element")
        return True
    except Exception as e:
        logger.error(f"Failed to click on the element: {e}")
        return False


@tool(
    description="double click on an element on the webpage",
    tags={"click", "browser automation"},
)
async def double_click(xpath: str, ctx: Context) -> bool:
    try:
        driver = get_driver()
        element = driver.find_element(By.XPATH, xpath)
        ActionChains(driver).double_click(element).perform()
        logger.info("Double clicked on the element")
        return True
    except Exception as e:
        logger.error(f"Failed to double click on the element: {e}")
        return False
