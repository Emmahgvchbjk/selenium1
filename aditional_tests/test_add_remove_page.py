import time
import selenium.webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

def test_add_button_functionality():
    driver = selenium.webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://the-internet.herokuapp.com/add_remove_elements/")
    add_element_button = driver.find_element(By.CSS_SELECTOR, "button[onclick='addElement()']")
    add_element_button.click()
    delete_button = driver.find_element(By.CSS_SELECTOR, "div button.added-manually")
    assert delete_button.is_displayed() == True, "delete button is not displayed"
    time.sleep(4.0)
    # delete_button = driver.find_element(By.CSS_SELECTOR, "div button.added-manually")
    # delete_button.click()
    # time.sleep(4.0)
    for i in range(0,10):
        add_element_button.click()
    list_delete_buttons = driver.find_elements(By.CSS_SELECTOR, "div button.added-manually")
    print(len(list_delete_buttons))
    assert len(list_delete_buttons) == 11, "the number of delete buttons is not ok"
    driver.quit()

def test_page():
    driver = selenium.webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://the-internet.herokuapp.com/add_remove_elements/")
    title_page = driver.find_element(By.CSS_SELECTOR, "h3")
    title_page_text = title_page.text
    assert title_page_text == "Add/Remove Elements", "the title is not the one we expected"
    driver.quit()
    add_element_button = driver.find_element(By.CSS_SELECTOR, "button[onclick='addElement()']")
    add_element_button.is_displayed() == True, "the button is not on the page"