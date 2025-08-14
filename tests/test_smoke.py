from selenium.webdriver.common.by import By

def test_title(driver):
    driver.get("https://example.org")
    assert "Example Domain" in driver.title

def test_link_text(driver):
    driver.get("https://example.org")
    link = driver.find_element(By.CSS_SELECTOR, "a")
    assert "More information" in link.text
