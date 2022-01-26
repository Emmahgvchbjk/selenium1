import time
import pytest
import selenium.webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = selenium.webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://the-internet.herokuapp.com/add_remove_elements/")
add_element_button = driver.find_element(By.CSS_SELECTOR, "button[onclick='addElement()']")
add_element_button.click()
time.sleep(4.0)
delete_button = driver.find_element(By.CSS_SELECTOR, "div button.added-manually")
delete_button.click()
time.sleep(4.0)
driver.quit()