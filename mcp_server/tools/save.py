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
        html_content = driver.find_element(By.TAG_NAME, "body").get_attribute(
            "innerHTML"
        )
        # with open("website.md", "w", encoding="utf-8") as f:
        #     f.write(md(html_content))
        logger.info("Returned markdown")
        return md(html_content)
    except Exception as e:
        logger.error(f"Failed to save markdown: {e}")
        return False


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
        return True
    except Exception as e:
        logger.error(f"Failed to print to PDF: {e}")
        return False


@tool(
    description="Save the current webpage as a html file",
    tags={"save webpage", "browser automation"},
)
async def get_webpage_html(ctx: Context) -> Union[str, bool]:
    try:
        driver = get_driver()
        html_content = driver.find_element(By.TAG_NAME, "body").get_attribute(
            "innerHTML"
        )
        logger.info("Returned html")
        return html_content
    except Exception as e:
        logger.error(f"Failed to save html: {e}")
        return False


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
        logger.error(f"Failed to save screenshot: {e}")
        return False
