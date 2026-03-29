import logging
from fastmcp.tools import tool
from fastmcp import Context

from tools.web_driver import get_driver

logger = logging.getLogger(__name__)


@tool(description="open url", tags={"manage url", "browser automation"})
async def open_url(url: str, ctx: Context) -> str:
    try:
        driver = get_driver()
        driver.get(url)
        logger.info(f"URL opened {driver.current_url}")
        return f"URL opened {driver.current_url}"
    except Exception as e:
        logger.error(e)
        return f"Failed to open URL. Error: {e}"


@tool(
    description="open url in new browser window",
    tags={"manage url", "browser automation"},
)
async def open_new_window(url: str, ctx: Context) -> str:
    try:
        driver = get_driver()
        driver.switch_to.new_window(WindowTypes.WINDOW)
        driver.get(url)
        logger.info(f"New window opened {driver.current_url}")
        return f"New window opened {driver.current_url}"
    except Exception as e:
        logger.error(e)
        return f"Failed to open new window. Error: {e}"


@tool(
    description="close the current tab",
    tags={"manage url", "browser automation"},
)
async def close_current_tab(ctx: Context) -> str:
    try:
        driver = get_driver()
        driver.close()
        logger.info(f"Current tab closed {driver.current_url}")
        return f"Current tab closed {driver.current_url}"
    except Exception as e:
        logger.error(e)
        return f"Failed to close current tab. Error: {e}"


@tool(
    description="switch to the window by url",
    tags={"manage url", "browser automation"},
)
async def switch_to_window_by_url(url: str, ctx: Context) -> str:
    try:
        driver = get_driver()
        original_handle = driver.current_window_handle
        for handle in driver.window_handles:  # iterate every open tab
            driver.switch_to.window(handle)  # switch to it
            current = driver.current_url  # read its URL
            if current.startswith(url) or url.startswith(current.rstrip("/")):
                logger.info(f"Switched to tab with URL: {current}")
                return f"Switched to tab with URL: {current}"  # stay on this tab ✅
        # no tab matched — go back to where we started
        web_driver.driver.switch_to.window(original_handle)
        logger.error(f"Tab with URL '{url}' not found")
        return f"Tab with URL '{url}' not found"
    except Exception as e:
        logger.error(e)
        return False


@tool(
    description="Refresh the current page",
    tags={"manage url", "browser automation"},
)
async def refresh_page(ctx: Context) -> str:
    try:
        driver = get_driver()
        driver.refresh()
        logger.info(f"Page refreshed {driver.current_url}")
        return f"Page refreshed {driver.current_url}"
    except Exception as e:
        logger.error(e)
        return f"Failed to refresh page. Error: {e}"


@tool(
    description="press forward button",
    tags={"manage url", "browser automation"},
)
async def press_browser_forward_button(ctx: Context) -> str:
    try:
        driver = get_driver()
        driver.forward()
        logger.info(f"Forward button pressed {driver.current_url}")
        return f"Forward button pressed {driver.current_url}"
    except Exception as e:
        logger.error(e)
        return f"Failed to press forward button. Error: {e}"


@tool(
    description="press back button",
    tags={"manage url", "browser automation"},
)
async def press_browser_back_button(ctx: Context) -> str:
    try:
        driver = get_driver()
        driver.back()
        logger.info(f"Back button pressed {driver.current_url}")
        return f"Back button pressed {driver.current_url}"
    except Exception as e:
        logger.error(e)
        return f"Failed to press back button. Error: {e}"


@tool(
    description="Mange browser window size",
    tags={"manage browser", "browser automation"},
)
async def manage_browser_window_size(width: int, height: int, ctx: Context) -> str:
    try:
        driver = get_driver()
        driver.set_window_size(width, height)
        logger.info(f"Browser window size set to {width}x{height}")
        return f"Browser window size set to {width}x{height}"
    except Exception as e:
        logger.error(e)
        return f"Failed to set browser window size. Error: {e}"
