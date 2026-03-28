import logging
from fastmcp.tools import tool
from fastmcp import Context

logger = logging.getLogger(__name__)


@tool(
    description="Scroll to the bottom of the webpage",
    tags={"scroll webpage", "browser automation"},
)
async def scroll_to_bottom(ctx: Context) -> bool:
    try:
        driver = await ctx.get_state("driver")
        element_text = [
            "Copyright",
            "©",
            "copyright",
            "footer",
            "All rights reserved",
            "(c)",
            "(C)",
        ]
        for text in element_text:
            elements = web_driver.driver.find_elements(
                By.XPATH, f"//*[contains(text(),'{text}')]"
            )
            if len(elements) != 0:
                ActionChains(web_driver.driver).move_to_element(elements[0]).perform()
                break
        return True
    except Exception as e:
        logger.error(f"Failed to scroll to bottom: {e}")
        return False


@tool(
    description="Scroll to the top of the webpage",
    tags={"scroll webpage", "browser automation"},
)
async def scroll_to_top(ctx: Context) -> bool:
    try:
        driver = await ctx.get_state("driver")
        driver.execute_script("window.scrollTo(0, 0)")
        logger.info("Scrolled to top")
        return True
    except Exception as e:
        logger.error(f"Failed to scroll to top: {e}")
        return False


@tool(
    description="Scroll to the specific element on the webpage",
    tags={"scroll webpage", "browser automation"},
)
async def scroll_to_element(xpath: str, ctx: Context) -> bool:
    try:
        driver = await ctx.get_state("driver")
        element = driver.find_element(By.XPATH, xpath)
        ActionChains(driver).move_to_element(element).perform()
        logger.info("Scrolled to element")
        return True
    except Exception as e:
        logger.error(f"Failed to scroll to element: {e}")
        return False
