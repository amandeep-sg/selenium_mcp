from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from fastmcp.tools import tool
from fastmcp import Context
import logging
from typing import List

# internal modules
from tools.web_driver import get_driver

logger = logging.getLogger(__name__)


@tool(
    description="Type text into an element on the webpage",
    tags={"input", "browser automation"},
)
async def input_text_by_xpath(xpath: str, text: str, ctx: Context) -> bool:
    try:
        driver = get_driver()
        element = driver.find_element(By.XPATH, xpath)
        if element.is_enabled() and element.is_displayed():
            element.send_keys(text)
            logger.info("Typed text into the element")
            return f"Typed text '{text}' into the element"
        logger.warn(
            f"Element enabled: {element.is_enabled()}, displayed: {element.is_displayed()}"
        )
        return f"Element enabled: {element.is_enabled()}, displayed: {element.is_displayed()}"
    except Exception as e:
        logger.error(f"Failed to type text into the element. Error: {e}")
        return f"Failed to type text into the element. Error: {e}"


@tool(
    description="Click checkbox on a webpage by xPath",
    tags={"input", "browser automation"},
)
async def click_checkbox_by_xpath(xpath: str, ctx: Context) -> bool:
    try:
        driver = get_driver()
        element = driver.find_element(By.XPATH, xpath)
        if element.is_enabled() and element.is_displayed():
            element.click()
            logger.info(f"Checkbox is selected: {element.is_selected()}")
            return f"Checkbox is selected: {element.is_selected()}"
        logger.warn(
            f"Checkbox enabled: {element.is_enabled()}, displayed: {element.is_displayed()}"
        )
        return f"Checkbox enabled: {element.is_enabled()}, displayed: {element.is_displayed()}"
    except Exception as e:
        logger.error(f"Failed to click checkbox. Error: {e}")
        return f"Failed to click checkbox. Error: {e}"


@tool(
    description="Click radio button on a webpage by xPath",
    tags={"input", "browser automation"},
)
async def click_radio_button_by_xpath(xpath: str, ctx: Context) -> bool:
    try:
        driver = get_driver()
        element = driver.find_element(By.XPATH, xpath)
        if element.is_enabled() and element.is_displayed():
            element.click()
            logger.info(f"Radio button is selected: {element.is_selected()}")
            return f"Radio button is selected: {element.is_selected()}"
        logger.warn(
            f"Radio button enabled: {element.is_enabled()}, displayed: {element.is_displayed()}"
        )
        return f"Radio button enabled: {element.is_enabled()}, displayed: {element.is_displayed()}"
    except Exception as e:
        logger.error(f"Failed to click radio button. Error: {e}")
        return f"Failed to click radio button. Error: {e}"


@tool(
    description="Get all select tag option from a dropdown on a webpage",
    tags={"input", "browser automation"},
)
async def get_all_options_by_xpath(xpath: str, ctx: Context) -> list[str]:
    try:
        driver = get_driver()
        element = driver.find_element(By.XPATH, xpath)
        if element.is_enabled() and element.is_displayed():
            select = Select(element)
            logger.info("Got all options from dropdown")
            return f"All options from the dropdown are: {[option.text for option in select.options]}"
        logger.warn(
            f"Element enabled: {element.is_enabled()}, displayed: {element.is_displayed()}"
        )
        return f"Element enabled: {element.is_enabled()}, displayed: {element.is_displayed()}"
    except Exception as e:
        logger.error(f"Failed to get all options from dropdown. Error: {e}")
        return f"Failed to get all options from dropdown. Error: {e}"


@tool(
    description="Select option from a dropdown (select tag) on a webpage",
    tags={"input", "browser automation"},
)
async def select_option_by_xpath(xpath: str, option_text: str, ctx: Context) -> bool:
    try:
        driver = get_driver()
        element = driver.find_element(By.XPATH, xpath)
        if element.is_enabled() and element.is_displayed():
            select = Select(element)
            select.select_by_visible_text(option_text)
            logger.info(
                f"Selected option from dropdown {[option.text for option in select.all_selected_options]}"
            )
            return f"Selected option from the dropdown is {[option.text for option in select.all_selected_options]}"
        logger.warn(
            f"Element enabled: {element.is_enabled()} and element displayed: {element.is_displayed()}"
        )
        return f"Element enabled: {element.is_enabled()}, displayed: {element.is_displayed()}"
    except Exception as e:
        logger.error(
            f"Failed to select option: {option_text} from dropdown. Error: {e}"
        )
        return f"Failed to select option: {option_text} from dropdown. Error: {e}"
