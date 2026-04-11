import logging
from fastmcp.tools import tool
from typing import Union, List
from fastmcp import Context
from tools.web_driver import get_driver

logger = logging.getLogger(__name__)


@tool(
    description="Find the accept cookies button and clicks it to accept all cookies",
    tags={"manage browser cookies", "browser automation"},
)
async def accept_all_cookies(ctx: Context) -> str:
    try:
        driver = get_driver()
        element_texts = ["Accept", "accept", "ok", "yes", "OK", "Yes"]
        for text in element_texts:
            elements = driver.find_elements(
                By.XPATH, f"//*[contains(text(), '{text}')]"
            )
            if len(elements) != 0:
                elements[0].click()
                logger.info("Accepted all cookies")
                return f"accepted all cookies"
        return f"Did not find button to accept cookies"
    except Exception as e:
        logger.error(f"Failed to accept all cookies. Error: {e}")
        return f"Failed to accept all cookies. Error: {e}"


@tool(
    description="Get all the cookies from the chrome driver",
    tags={"manage browser cookies", "browser automation"},
)
async def get_all_cookies(ctx: Context) -> List:
    try:
        driver = await ctx.get_state("driver")
        logger.info("Got all cookies")
        return driver.get_cookies()
    except Exception as e:
        logger.error(f"Failed to get all cookies. Error: {e}")
        return f"Failed to get all cookies. Error: {e}"


@tool(
    description="delete cookie by name",
    tags={"manage browser cookies", "browser automation"},
)
async def delete_cookie_by_name(cookie_name: str, ctx: Context) -> Union[None, dict]:
    try:
        driver = get_driver()
        driver.delete_cookie(cookie_name)
        logger.info(f"Deleted cookie {cookie_name}")
        return f"Deleted cookie {cookie_name}"
    except Exception as e:
        logger.error(f"Failed to delete cookie {cookie_name}. Error: {e}")
        return f"Failed to delete cookie {cookie_name}. Error: {e}"


@tool(
    description="delete all cookies",
    tags={"manage browser cookies", "browser automation"},
)
async def delete_all_cookies(ctx: Context) -> str:
    try:
        driver = get_driver()
        driver.delete_all_cookies()
        logger.info("Deleted all cookies")
        return "Deleted all cookies"
    except Exception as e:
        logger.error(f"Failed to delete all cookies. Error: {e}")
        return f"Failed to delete all cookies. Error: {e}"


@tool(
    description="add cookie",
    tags={"manage browser cookies", "browser automation"},
)
async def add_cookie(cookie_name: str, cookie_value: str, ctx: Context) -> str:
    try:
        driver = get_driver()
        driver.add_cookie({"name": cookie_name, "value": cookie_value})
        logger.info(f"Added cookie {cookie_name}")
        return f"Added cookie {cookie_name}:{cookie_value}"
    except Exception as e:
        logger.error(f"Failed to add cookie {cookie_name}. Error: {e}")
        return f"Failed to add cookie {cookie_name}. Error: {e}"


@tool(
    description="set same-site cookie to 'Lax' or 'Strict' or 'None'",
    tags={"manage browser cookies", "browser automation"},
)
async def set_same_site_cookie(same_site: str, ctx: Context) -> str:
    try:
        driver = get_driver()
        driver.add_cookie({"sameSite": same_site})
        logger.info(f"Setted sameSite to {same_site}")
        return f"Setted sameSite to {same_site}"
    except Exception as e:
        logger.error(f"Failed to set sameSite to {same_site}. Error: {e}")
        return f"Failed to set sameSite to {same_site}. Error: {e}"
