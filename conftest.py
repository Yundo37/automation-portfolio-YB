import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="session")
def driver():
    opts = Options()
    opts.add_argument("--headless=new")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-dev-shm-usage")
    # Colab에 설치된 Chromium 경로
    opts.binary_location = os.environ.get("CHROME_BIN", "/usr/bin/chromium-browser")
    drv = webdriver.Chrome(options=opts)
    drv.set_page_load_timeout(30)
    yield drv
    drv.quit()
