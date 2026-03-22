import logging
from fastmcp.tools import tool
from typing import Union
from fastmcp import Context

logger = logging.getLogger(__name__)


@tool(
    description="Find the accept cookies button and clicks it to accept all cookies",
    tags={"manage browser cookies", "browser automation"},
)
async def accept_all_cookies(ctx: Context) -> Union[None, int]:
    try:
        driver = await ctx.get_state("driver")
        element_texts = ["Accept", "accept", "ok", "yes", "OK", "Yes"]
        for text in element_texts:
            elements = driver.find_elements(
                By.XPATH, f"//*[contains(text(), '{text}')]"
            )
            if len(elements) != 0:
                elements[0].click()
                logger.info("Accepted all cookies")
                return len(elements)
        return None
    except Exception as e:
        logger.error(e)
        return None


@tool(
    description="Get all the cookies from the chrome driver",
    tags={"manage browser cookies", "browser automation"},
)
async def get_all_cookies(ctx: Context) -> Union[None, list]:
    try:
        driver = await ctx.get_state("driver")
        return driver.get_cookies()
    except Exception as e:
        logger.error(e)
        return None
