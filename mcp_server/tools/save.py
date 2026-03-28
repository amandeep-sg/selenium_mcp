import logging
import base64
from typing import Union
from fastmcp.tools import tool
from fastmcp import Context
from selenium.webdriver.common.print_page_options import PrintOptions
from selenium.webdriver.common.by import By
from markdownify import markdownify as md

# internal modules
from tools.web_driver import get_driver

logger = logging.getLogger(__name__)


@tool(
    description="Save the current webpage as a markdown file",
    tags={"save webpage", "browser automation"},
)
async def get_markdown(ctx: Context) -> Union[str, bool]:
    try:
        driver = get_driver()
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
    description="Save the current webpage as a PDF file",
    tags={"save webpage", "browser automation"},
)
async def save_webpage_as_pdf(ctx: Context) -> bool:
    try:
        driver = get_driver()
        print_options = PrintOptions()

        print_options.orientation = "portrait"
        print_options.scale = 0.8
        print_options.background = True

        base64_pdf = driver.print_page(print_options)

        with open("website.pdf", "wb") as f:
            f.write(base64.b64decode(base64_pdf))
        logger.info("Saved PDF to website.pdf")
        return "Saved PDF to website.pdf"
    except Exception as e:
        logger.error(f"Failed to print to PDF: {e}")
        return f"Failed to print to PDF. Error: {e}"


@tool(
    description="Save the current webpage as a html file",
    tags={"save webpage", "browser automation"},
)
async def get_webpage_html(ctx: Context) -> Union[str, bool]:
    try:
        driver = get_driver()
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
    description="Save the current webpage screenshot",
    tags={"save webpage", "browser automation"},
)
async def get_screenshot(ctx: Context) -> Union[str, bool]:
    try:
        driver = get_driver()
        driver.save_screenshot("website.png")
        logger.info("Saved screenshot")
        return driver.get_screenshot_as_base64()
    except Exception as e:
        logger.error(f"Failed to get webpage screenshot: {e}")
        return f"Failed to get webpage screenshot. Error: {e}"


@tool(
    description="Get element screenshot",
    tags={"save webpage", "browser automation"},
)
async def get_element_screenshot(xpath: str, ctx: Context) -> Union[str, bool]:
    try:
        driver = get_driver()
        element = driver.find_element(By.XPATH, xpath)
        if element.is_displayed() and element.is_enabled():
            element.screenshot(f"{xpath}.png")
            logger.info(f"Saved screenshot {xpath}")
            return element.screenshot()
        logger.warn(
            f"Element enabled: {element.is_enabled()} and element displayed: {element.is_displayed()}"
        )
        return f"Element enabled: {element.is_enabled()} and element displayed: {element.is_displayed()}"
    except Exception as e:
        logger.error(f"Failed to get element's screenshot {xpath}. Error: {e}")
        return f"Failed to get element's screenshot {xpath}. Error: {e}"
