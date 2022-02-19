import time
import selenium.webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

def test_check_search():
    driver = selenium.webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://duckduckgo.com/")
    autocomplete=driver.find_element(By.CSS_SELECTOR, 'input#search_form_input_homepage')
    autocomplete.send_keys('python')
    search = driver.find_element(By.CSS_SELECTOR, 'input#search_button_homepage')
    search.click()