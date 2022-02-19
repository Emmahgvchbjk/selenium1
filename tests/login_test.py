import selenium.webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from pages.herokuapp_elements import PageElements

def test_logare(browser):
    USERNAME = ("tomsmith")
    PASSWORD = ("SuperSecretPassword!")
    SUCCES_LOGIN = ("You logged into a secure area!")
    SUCCES_LOGOUT = ("You logged out of the secure area!")

# login
    page = PageElements(browser)
    page.login(USERNAME, PASSWORD)
#login check
    assert SUCCES_LOGIN in page.get_login_message(), "the login action was not successful"
#logout
    page.click_logout_button()
#logout check
    assert SUCCES_LOGOUT in page.get_logout_message(), "the logout action was not successful"




