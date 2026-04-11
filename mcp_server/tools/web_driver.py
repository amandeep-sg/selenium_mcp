import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from fastmcp.tools import tool
from fastmcp import Context

logger = logging.getLogger(__name__)

global _driver


# options
options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")
options.add_argument("--start-maximized")
options.add_argument("--accept-insecure-certs")
options.enable_bidi = True

# services
service = Service()
service = webdriver.ChromeService(
    service_args=["--log-level=DEBUG"], log_output="webdriver_logs.log"
)


@tool(
    description="create instance of chrome webdriver",
    tags={"manage webdriver", "chrome"},
)
async def initialize_driver(ctx: Context):
    global _driver
    try:
        _driver = webdriver.Chrome(options=options, service=service)
        logger.info("Driver initialized")
        return "Driver initialized"
    except Exception as e:
        logger.error(f"Failed to initialize driver. Error: {e}")
        return f"Failed to initialize driver. Error: {e}"


@tool(description="close the browser", tags={"manage browser", "browser automation"})
async def close_driver(ctx: Context):
    try:
        _driver.quit()
        logger.info("Driver closed")
        return "Driver closed"
    except Exception as e:
        logger.error(f"Failed to close driver. Error: {e}")
        return f"Failed to close driver. Error: {e}"


def get_driver():
    return _driver
