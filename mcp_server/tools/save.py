import logging
import base64
from fastmcp.tools import tool
from fastmcp import Context
from selenium.webdriver.common.print_page_options import PrintOptions

# internal modules
from tools.web_driver import get_driver

logger = logging.getLogger(__name__)


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
