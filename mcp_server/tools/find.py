import logging
from fastmcp.tools import tool
from typing import Union
from fastmcp import Context
from selenium.webdriver.common.by import By

# internal modules
from tools.web_driver import get_driver

logger = logging.getLogger(__name__)


@tool(
    description="Find the DOM element by text",
    tags={"find DOM element", "browser automation"},
)
async def find_element_by_text(text: str, ctx: Context) -> str:
    try:
        driver = get_driver()
        elements = driver.find_elements(By.XPATH, f"//*[contains(text(),'{text}')]")
        if len(elements) != 0:
            return f"Elements found for text {text}: {len(elements)}"
        return f"No element found for text {text}"
    except Exception as e:
        logger.error(f"Failed to find element for text {text}: {e}")
        return f"Failed to find the element for text {text}"


@tool(
    description="Find the DOM element by xpath",
    tags={"find DOM element", "browser automation"},
)
async def find_element_by_xpath(xpath: str, ctx: Context) -> str:
    try:
        driver = get_driver()
        elements = driver.find_elements(By.XPATH, xpath)
        return f"Elements found for xpath {xpath}: {len(elements)}"
    except Exception as e:
        logger.error(f"Failed to find element by xpath: {e}")
        return f"Failed to find the element for xpath {xpath}"


@tool(
    description="Find the DOM element by css selector",
    tags={"find DOM element", "browser automation"},
)
async def find_element_by_css_selector(css_selector: str, ctx: Context) -> str:
    try:
        driver = get_driver()
        elements = driver.find_elements(By.CSS_SELECTOR, css_selector)
        return f"Elements found for css selector {css_selector}: {len(elements)}"
    except Exception as e:
        logger.error(f"Failed to find element by css selector: {e}")
        return f"Failed to find the element for css selector {css_selector}"


@tool(
    description="Find the DOM element by tag name",
    tags={"find DOM element", "browser automation"},
)
async def find_element_by_tag_name(tag_name: str, ctx: Context) -> str:
    try:
        driver = get_driver()
        elements = driver.find_elements(By.TAG_NAME, tag_name)
        return f"Elements found for tag name {tag_name}: {len(elements)}"
    except Exception as e:
        logger.error(f"Failed to find element by tag name: {e}")
        return f"Failed to find the element for tag name {tag_name}"
