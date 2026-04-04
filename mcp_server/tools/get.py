import logging
import base64
from typing import Union, Annotated, List
from fastmcp.tools import tool
from fastmcp import Context
from selenium.webdriver.common.print_page_options import PrintOptions
from selenium.webdriver.common.by import By
from markdownify import markdownify as md
import json

# internal modules
from tools.web_driver import get_driver

logger = logging.getLogger(__name__)


@tool(
    description="get the current webpage as a markdown",
    tags={"get webpage", "browser automation"},
)
async def get_webpage_markdown(ctx: Context) -> str:
    try:
        driver = get_driver()
        driver.fullscreen_window()
        element = driver.find_element(By.TAG_NAME, "body")
        if element.is_enabled() and element.is_displayed():
            html_content = element.get_attribute("innerHTML")
            logger.info("Returned markdown")
            return md(html_content)
        logger.warn(
            f"Element enabled: {element.is_enabled()} and element displayed: {element.is_displayed()}"
        )
        return f"Element enabled: {element.is_enabled()} and element displayed: {element.is_displayed()}"
    except Exception as e:
        logger.error(f"Failed to save markdown: {e}")
        return f"Failed to save markdown. Error: {e}"


@tool(
    description="get the html of the current webpage",
    tags={"get webpage", "browser automation"},
)
async def get_webpage_html(ctx: Context) -> str:
    try:
        driver = get_driver()
        driver.fullscreen_window()
        element = driver.find_element(By.TAG_NAME, "body")
        if element.is_displayed() and element.is_enabled():
            html_content = element.get_attribute("innerHTML")
            logger.info("Returned html")
            return html_content
        logger.warn(
            f"Element enabled: {element.is_enabled()} and element displayed: {element.is_displayed()}"
        )
        return f"Element enabled: {element.is_enabled()} and element displayed: {element.is_displayed()}"
    except Exception as e:
        logger.error(f"Failed to get webpage html: {e}")
        return f"Failed to get webpage html. Error: {e}"


@tool(
    description="get the screenshot of the current webpage",
    tags={"get webpage", "browser automation"},
)
async def get_webpage_screenshot(ctx: Context) -> str:
    try:
        driver = get_driver()
        logger.info("Saved full page screenshot")
        driver.fullscreen_window()
        return driver.get_screenshot_as_base64()
    except Exception as e:
        logger.error(f"Failed to get full page screenshot: {e}")
        return f"Failed to get full page screenshot. Error: {e}"


@tool(
    description="get the screenshot of an element",
    tags={"get webpage", "browser automation"},
)
async def get_element_screenshot(xpath: str, ctx: Context) -> str:
    try:
        driver = get_driver()
        element = driver.find_element(By.XPATH, xpath)
        if element.is_displayed() and element.is_enabled():
            element.screenshot(f"{xpath}.png")
            logger.info(f"Saved screenshot {xpath}")
            return element.get_screenshot_as_base64()
        logger.warn(
            f"Element enabled: {element.is_enabled()} and element displayed: {element.is_displayed()}"
        )
        return f"Element enabled: {element.is_enabled()} and element displayed: {element.is_displayed()}"
    except Exception as e:
        logger.error(f"Failed to get element's screenshot {xpath}. Error: {e}")
        return f"Failed to get element's screenshot {xpath}. Error: {e}"


@tool(
    description="get all urls from the current webpage",
    tags={"get webpage", "browser automation"},
)
async def get_list_of_urls(
    ctx: Context,
    type: Annotated[
        str, "filter to apply on urls using 'in' operator. By default none"
    ] = None,
) -> dict:
    try:
        driver = get_driver()
        links = driver.find_elements(By.TAG_NAME, "a")
        urls = []
        for link in links:
            urls.append(link.get_attribute("href"))
        if type:
            urls = [url for url in urls if type in url]
        logger.info(f"count of urls: {len(urls)}")
        logger.info({"links": urls})
        return {"links": urls}
    except Exception as e:
        logger.error(f"Failed to get list of urls: {e}")
        return f"Failed to get list of urls. Error: {e}"
