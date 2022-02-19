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
    driver.find_element(By.CSS_SELECTOR, "div.farefinder-container").click()

    # time.sleep(5)
    # date_tomorrow = datetime.date.today() + datetime.timedelta(days=1)
    # # date_of_departure_selector = date_tomorrow.strftime("%B") + " " + date_tomorrow.strftime("%d") + ", " + date_tomorrow.strftime("%Y")
    # data_from_departure_selector= 'td[aria-label='+ date_of_departure_selector +']'
    #
    # date_of_return = date_tomorrow + datetime.timedelta(days=20)
    # # date_of_return_selector = date_of_return.strftime("%B") + " " + date_of_return.strftime("%d") + ", " + date_tomorrow.strftime("%Y")
    # data_from_returning_selector ='td[aria-label='+ date_of_return_selector +']'
    #
    # next_day_detailed = date_tomorrow.strftime('%B %d, %Y')
    # if next_day_detailed[-8] == "0":
    #     next_day_detailed = next_day_detailed.replace(next_day_detailed[-8], "", 1)
    # print("conversion of next day", next_day_detailed)
    # next_day20_detailed = date_of_return.strftime('%B %d, %Y')
    # if next_day20_detailed[-8] == "0":
    #     next_day20_detailed = next_day20_detailed.replace(next_day20_detailed[-8], "", 1)
    #
    # departing_date = driver.find_element(By.CSS_SELECTOR, "div[data-bdd ='farefinder-package-startdate-input']")
    # departing_date.click()
    # destination_bar.send_keys(Keys.PAGE_DOWN)
    # select_departing_date = driver.find_element(By.CSS_SELECTOR, data_from_departure_selector)
    # select_departing_date.click()
    #
    # select_returning_date = driver.find_element(By.CSS_SELECTOR, data_from_returning_selector)
    # select_returning_date.click()
    next_day = datetime.datetime.today() + datetime.timedelta(days=1)
    next_day20 = datetime.datetime.today() + datetime.timedelta(days=20)
    next_day_detailed = next_day.strftime('%B %d, %Y')
    if next_day_detailed[-8] == "0":
        next_day_detailed = next_day_detailed.replace(next_day_detailed[-8], "", 1)
    print("conversion of next day", next_day_detailed)
    next_day20_detailed = next_day20.strftime('%B %d, %Y')
    if next_day20_detailed[-8] == "0":
        next_day20_detailed = next_day20_detailed.replace(next_day20_detailed[-8], "", 1)
    print("conversion of 20+ day", next_day20_detailed)
    date_from_selector = "td[aria-label*=\""+next_day_detailed+"\"]"
    date_to_selector = "td[aria-label*=\""+next_day20_detailed+"\"]"
    departing_date = driver.find_element(By.CSS_SELECTOR, '[data-bdd="farefinder-package-startdate-input"]')
    departing_date.click()
    date_from = driver.find_element(By.CSS_SELECTOR, date_from_selector)
    date_from.click()
    date_to = driver.find_element(By.CSS_SELECTOR, date_to_selector)
    date_to.click()
    time.sleep(5)
    find_deals_button = driver.find_element(By.CSS_SELECTOR, "[data-bdd='farefinder-package-search-button']")
    find_deals_button.click()
    time.sleep(5)