from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait as WW
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome()
action_chains = ActionChains(driver)
driver.get("https://demoqa.com/upload-download")

upload_button = WW(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "#uploadFile"))
)


file_path = "/home/seluser/file_to_uplod.txt"
upload_button.send_keys(file_path)

time.sleep(100)
