import time
import selenium.webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import datetime

def test_package():
    driver = selenium.webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.hotwire.com/")
    bundles_button = driver.find_element(By.CSS_SELECTOR, "span[class ='SVGIcon active icon small'] > svg[data-id ='SVG_HW_BRAND_CAR']")
    bundles_button.click()
    select_car_button = driver.find_element(By.CSS_SELECTOR, "button[data-bdd ='farefinder-package-bundleoption-car']")
    select_car_button.click()
    location_bar = driver.find_element(By.CSS_SELECTOR, "input[data-bdd='farefinder-package-origin-location-input']")
    location_bar.send_keys("SFO")
    destination_bar = driver.find_element(By.CSS_SELECTOR, "input[data-bdd='farefinder-package-destination-location-input']")
    destination_bar.send_keys("LAX")
    bundles_button.click()

    time.sleep(5)
    date_tomorrow = datetime.date.today() + datetime.timedelta(days=1)
    date_of_departure_selector = date_tomorrow.strftime("%B") + " " + date_tomorrow.strftime("%d") + ", " + date_tomorrow.strftime("%Y")
    data_from_departure_selector= 'td[aria-label=\"'+ date_of_departure_selector +'\"]'

    date_of_return = date_tomorrow + datetime.timedelta(days=20)
    date_of_return_selector = date_of_return.strftime("%B") + " " + date_of_return.strftime("%d") + ", " + date_tomorrow.strftime("%Y")

    departing_date = driver.find_element(By.CSS_SELECTOR, "div[data-bdd ='farefinder-package-startdate-input']")
    departing_date.click()
    destination_bar.send_keys(Keys.PAGE_DOWN)
    select_departing_date = driver.find_element(By.CSS_SELECTOR, data_from_departure_selector)
    select_departing_date.click()

    data_from_returning_selector ='td[aria-label=\"'+ date_of_return_selector +'\"]'
    select_returning_date = driver.find_element(By.CSS_SELECTOR, data_from_returning_selector)
    select_returning_date.click()
