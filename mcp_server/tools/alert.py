import logging
from fastmcp.tools import tool
from fastmcp import Context
from typing import Union, List, Dict, Any

# internal modules
from tools.web_driver import get_driver

logger = logging.getLogger(__name__)


@tool(
    description="accept alert on the webpage",
    tags={"alert", "browser automation"},
)
async def accept_alert(ctx: Context) -> str:
    try:
        driver = get_driver()
        alert = driver.switch_to.alert
        alert.accept()
        logger.info("Alert accepted")
        return "Alert accepted"
    except Exception as e:
        logger.error(f"Failed to accept alert: {e}")
        return f"Failed to accept alert: {e}"


@tool(
    description="dismiss alert on the webpage",
    tags={"alert", "browser automation"},
)
async def dismiss_alert(ctx: Context) -> str:
    try:
        driver = get_driver()
        alert = driver.switch_to.alert
        alert.dismiss()
        logger.info("Alert dismissed")
        return "Alert dismissed"
    except Exception as e:
        logger.error(f"Failed to dismiss alert: {e}")
        return f"Failed to dismiss alert: {e}"


@tool(
    description="get alert text on the webpage",
    tags={"alert", "browser automation"},
)
async def get_alert_text(ctx: Context) -> str:
    try:
        driver = get_driver()
        alert = driver.switch_to.alert
        alert_text = alert.text
        logger.info(f"Alert text: {alert_text}")
        return alert_text
    except Exception as e:
        logger.error(f"Failed to get alert text: {e}")
        return f"Failed to get alert text: {e}"
