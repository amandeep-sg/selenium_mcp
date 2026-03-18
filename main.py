import logging

logging.basicConfig(
    filename="test.log",
    filemode="w",
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.DEBUG,
    force=True,
)

logger = logging.getLogger(__name__)

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from tools.cookies import accept_all_cookies, get_all_cookies
from tools.scroll import scroll_to_bottom, scroll_to_top
from tools.print import print_to_pdf
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from tools.url import open_new_tab, switch_to_tab_by_url, close_current_tab
import base64
from tools.markdown import save_markdown
import time

options = Options()
# options.add_argument("--headless")

logger.info("in")

driver = webdriver.Chrome()
driver.get("https://jkb.bank.in/tenderNotice")
open_new_tab(driver, "https://rfpnotification.com")
switch_to_tab_by_url(driver, "https://jkb.bank.in/tenderNotice")
accept_all_cookies(driver)
scroll_to_bottom(driver)
scroll_to_top(driver)
print_to_pdf(driver)
save_markdown(driver)
cookies = get_all_cookies(driver)
print(cookies)
time.sleep(5)
driver.quit()
