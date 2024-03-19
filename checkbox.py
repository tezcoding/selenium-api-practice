from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait as WW
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://demoqa.com/checkbox")

checkbox = WW(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, ".rct-icon.rct-icon-uncheck"))
)
checkbox.click()
time.sleep(1)
