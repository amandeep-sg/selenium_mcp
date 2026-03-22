import logging
from fastmcp.tools import tool
from typing import Union
from fastmcp import Context

logger = logging.getLogger(__name__)


@tool(
    description="Find the DOM element by text",
    tags={"find DOM element", "browser automation"},
)
async def find_element_by_text(text: str, ctx: Context) -> Union[None, object]:
    try:
        driver = await ctx.get_state("driver")
        elements = driver.find_elements(By.XPATH, f"//*[contains(text(),'{text}')]")
        if len(elements) != 0:
            return elements[0]
        return None
    except Exception as e:
        logger.error(f"Failed to find element by text: {e}")
        return None


@tool(
    description="Find the DOM element by xpath",
    tags={"find DOM element", "browser automation"},
)
async def find_element_by_xpath(xpath: str, ctx: Context) -> Union[None, object]:
    try:
        driver = await ctx.get_state("driver")
        element = driver.find_element(By.XPATH, xpath)
        return element
    except Exception as e:
        logger.error(f"Failed to find element by xpath: {e}")
        return None


@tool(
    description="Find the DOM element by css selector",
    tags={"find DOM element", "browser automation"},
)
async def find_element_by_css_selector(
    css_selector: str, ctx: Context
) -> Union[None, object]:
    try:
        driver = await ctx.get_state("driver")
        element = driver.find_element(By.CSS_SELECTOR, css_selector)
        return element
    except Exception as e:
        logger.error(f"Failed to find element by css selector: {e}")
        return None


@tool(
    description="Find the DOM element by tag name",
    tags={"find DOM element", "browser automation"},
)
async def find_element_by_tag_name(tag_name: str, ctx: Context) -> Union[None, object]:
    try:
        driver = await ctx.get_state("driver")
        element = driver.find_element(By.TAG_NAME, tag_name)
        return element
    except Exception as e:
        logger.error(f"Failed to find element by tag name: {e}")
        return None
