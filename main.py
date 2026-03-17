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
from tools.cookies import accept_all_cookies
from tools.scroll import scroll_to_bottom
from tools.print import print_to_pdf
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import base64
from tools.markdown import save_markdown

options = Options()
# options.add_argument("--headless")

logger.info("in")

driver = webdriver.Chrome()
driver.get("https://jkb.bank.in/tenderNotice")
accept_all_cookies(driver)
scroll_to_bottom(driver)
print_to_pdf(driver)
save_markdown(driver)


driver.quit()
