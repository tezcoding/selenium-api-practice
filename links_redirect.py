from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait as WW
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome()
action_chains = ActionChains(driver)
driver.get("https://demoqa.com/links")

home_link = WW(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "#simpleLink"))
)

home_link.click()

active_tab = driver.current_window_handle
tabs = driver.window_handles


inactive_tabs = []
for tab in tabs:
    if tab != active_tab:
        inactive_tabs.append(tab)

print("Active tab ID: " + active_tab)
print("All tab IDs: " + str(tabs))
print("All inactive tab IDs: " + str(inactive_tabs))
WW(driver, 10).until(EC.number_of_windows_to_be(2))

driver.switch_to.window(inactive_tabs[0])
driver._switch_to.window()
time.sleep(99)
