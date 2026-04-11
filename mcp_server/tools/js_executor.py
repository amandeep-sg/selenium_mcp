import logging
from fastmcp.tools import tool
from fastmcp import Context
from typing import Union, List, Dict, Any

# internal modules
from tools.web_driver import get_driver

logger = logging.getLogger(__name__)


@tool(
    description="execute the javascript code for interacting with the webpage",
    tags={"javascript", "browser automation", "advance level"},
)
async def execute_javascript(script: str, ctx: Context, sync: bool = True) -> Any:
    try:
        driver = get_driver()
        if sync:
            result = driver.execute_script(script)
        else:
            result = driver.execute_async_script(script)
        logger.info(f"Executed javascript code: {script}")
        return result
    except Exception as e:
        logger.error(f"Failed to execute javascript code. Error: {e}")
        return f"Failed to execute javascript code. Error: {e}"
