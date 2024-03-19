from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait as WW
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome()
action_chains = ActionChains(driver)
driver.get("https://demoqa.com/dynamic-properties")

enabled_in_n_seconds_button = WW(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "#enableAfter"))
)
visible_in_n_seconds_button = WW(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "#enableAfter"))
)

enabled_in_n_seconds_button.click()


visible_in_n_seconds_button.click()

time.sleep(5)
