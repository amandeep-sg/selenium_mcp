import logging
from fastmcp.tools import tool
from fastmcp import Context

from tools.web_driver import get_driver

logger = logging.getLogger(__name__)


@tool(description="open url", tags={"manage url", "browser automation"})
async def open_url(url: str, ctx: Context) -> bool:
    try:
        driver = get_driver()
        driver.get(url)
        logger.info(f"URL opened {driver.current_url}")
        return True
    except Exception as e:
        logger.error(e)
        return False


@tool(
    description="open url in new browser window",
    tags={"manage url", "browser automation"},
)
async def open_new_window(url: str, ctx: Context) -> bool:
    try:
        driver = get_driver()
        driver.switch_to.new_window(WindowTypes.WINDOW)
        driver.get(url)
        logger.info(f"New window opened {driver.current_url}")
        return True
    except Exception as e:
        logger.error(e)
        return False


@tool(
    description="close the current tab",
    tags={"manage url", "browser automation"},
)
async def close_current_tab(ctx: Context) -> bool:
    try:
        driver = get_driver()
        driver.close()
        logger.info(f"Current tab closed {driver.current_url}")
        return True
    except Exception as e:
        logger.error(e)
        return False


@tool(
    description="switch to the tab by tab index",
    tags={"manage url", "browser automation"},
)
async def switch_to_tab(tab_index: int, ctx: Context) -> bool:
    try:
        driver = get_driver()
        driver.switch_to.window(driver.window_handles[tab_index])
        logger.info(f"Switched to tab {tab_index}")
        return True
    except Exception as e:
        logger.error(e)
        return False


@tool(
    description="switch to the tab by url",
    tags={"manage url", "browser automation"},
)
async def switch_to_tab_by_url(url: str, ctx: Context) -> bool:
    try:
        driver = get_driver()
        original_handle = driver.current_window_handle
        for handle in driver.window_handles:  # iterate every open tab
            driver.switch_to.window(handle)  # switch to it
            current = driver.current_url  # read its URL
            if current.startswith(url) or url.startswith(current.rstrip("/")):
                logger.info(f"Switched to tab with URL: {current}")
                return True  # stay on this tab ✅
        # no tab matched — go back to where we started
        web_driver.driver.switch_to.window(original_handle)
        logger.error(f"Tab with URL '{url}' not found")
        return False
    except Exception as e:
        logger.error(e)
        return False


@tool(
    description="Refresh the current page",
    tags={"manage url", "browser automation"},
)
async def refresh_page(ctx: Context) -> bool:
    try:
        driver = get_driver()
        driver.refresh()
        logger.info(f"Page refreshed {driver.current_url}")
        return True
    except Exception as e:
        logger.error(e)
        return False


@tool(
    description="press forward button",
    tags={"manage url", "browser automation"},
)
async def press_forward(ctx: Context) -> bool:
    try:
        driver = get_driver()
        driver.forward()
        logger.info(f"Forward button pressed {driver.current_url}")
        return True
    except Exception as e:
        logger.error(e)
        return False


@tool(
    description="press back button",
    tags={"manage url", "browser automation"},
)
async def press_back(ctx: Context) -> bool:
    try:
        driver = get_driver()
        driver.back()
        logger.info(f"Back button pressed {driver.current_url}")
        return True
    except Exception as e:
        logger.error(e)
        return False
