import logging
from fastmcp.tools import tool
from fastmcp import Context
from selenium.webdriver.common.by import By

# internal modules
from tools.web_driver import get_driver

logger = logging.getLogger(__name__)


@tool(
    description="Upload a file to an input element and submit",
    tags={"file", "browser automation"},
)
async def upload_file(
    file_path: str, input_element_xpath: str, submit_element_xpath: str, ctx: Context
) -> str:
    try:
        driver = get_driver()
        element = driver.find_element(By.XPATH, input_element_xpath)
        element.send_keys(file_path)
        logger.info(f"Uploaded file {file_path}")
        submit_element = driver.find_element(By.XPATH, submit_element_xpath)
        submit_element.click()
        logger.info(f"Submitted file {file_path}")
        return f"Uploaded file {file_path}"
    except Exception as e:
        logger.error(f"Failed to upload file {file_path}. Error: {e}")
        return f"Failed to upload file {file_path}. Error: {e}"
