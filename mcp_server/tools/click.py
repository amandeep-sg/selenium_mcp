from tools.web_driver import get_driver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from fastmcp.tools import tool
from fastmcp import Context
from typing import Union, List, Dict, Any
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
        logger.info(f"Left clicked on the element {xpath}")
        return f"Left clicked on the element {xpath}"
    except Exception as e:
        logger.error(f"Failed to left click on the element {xpath}. Error: {e}")
        return f"Failed to left click on the element {xpath}. Error: {e}"


@tool(
    description="right click on an element on the webpage",
    tags={"click", "browser automation"},
)
async def right_click(xpath: str, ctx: Context) -> bool:
    try:
        driver = get_driver()
        element = driver.find_element(By.XPATH, xpath)
        ActionChains(driver).context_click(element).perform()
        logger.info(f"Right clicked on the element {xpath}")
        return f"Right clicked on the element {xpath}"
    except Exception as e:
        logger.error(f"Failed to right click on the element {xpath}. Error: {e}")
        return f"Failed to right click on the element {xpath}. Error: {e}"


@tool(
    description="double click on an element on the webpage",
    tags={"click", "browser automation"},
)
async def double_click(xpath: str, ctx: Context) -> bool:
    try:
        driver = get_driver()
        element = driver.find_element(By.XPATH, xpath)
        ActionChains(driver).double_click(element).perform()
        logger.info(f"Double clicked on the element {xpath}")
        return f"Double clicked on the element {xpath}"
    except Exception as e:
        logger.error(f"Failed to double click on the element {xpath}. Error: {e}")
        return f"Failed to double click on the element {xpath}. Error: {e}"


@tool(
    description="drag and drop element",
    tags={"click", "browser automation"},
)
async def drag_and_drop_element(
    source_xpath: str, target_xpath: str, ctx: Context
) -> str:
    try:
        driver = get_driver()
        source_element = driver.find_element(By.XPATH, source_xpath)
        target_element = driver.find_element(By.XPATH, target_xpath)
        ActionChains(driver).drag_and_drop(source_element, target_element).perform()
        logger.info(f"Dragged and dropped the element {source_xpath} to {target_xpath}")
        return f"Dragged and dropped the element {source_xpath} to {target_xpath}"
    except Exception as e:
        logger.error(f"Failed to drag and drop the element: {e}")
        return f"Failed to drag and drop the element: {e}"
