from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait as WW
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome()
action_chains = ActionChains(driver)
driver.get("https://demoqa.com/buttons")

double_click_button = WW(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "#doubleClickBtn"))
)

double_click_action = action_chains.double_click(double_click_button)

double_click_action.perform()

right_click_button = WW(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "#rightClickBtn"))
)

right_click_action = action_chains.context_click(right_click_button)

right_click_action.perform()

time.sleep(5)
