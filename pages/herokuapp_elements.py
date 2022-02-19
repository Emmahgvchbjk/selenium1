import selenium.webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains


class PageElements:
    URL = "http://the-internet.herokuapp.com/login"
    USERNAME_INPUT =(By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type = 'submit']")
    LOGOUT_BUTTON = (By.CSS_SELECTOR, "a.secondary.radius")
    LOGIN_TEXT = (By.ID, "flash")
    LOGOUT_TEXT = (By.ID, "flash")

    def __init__(self, browser):
        self.browser = browser

    def load_page(self):
        return self.browser.get(self.URL)

    def input_username(self, username):
        return self.browser.find_element(*self.USERNAME_INPUT).send_keys(username)

    def input_password(self, password):
        return self.browser.find_element(*self.PASSWORD_INPUT).send_keys(password)

    def click_login_button(self):
        return self.browser.find_element(*self.LOGIN_BUTTON).click()

    def click_logout_button(self):
        return self.browser.find_element(*self.LOGOUT_BUTTON).click()

    def get_login_message(self):
        return self.browser.find_element(*self.LOGIN_TEXT).text

    def get_logout_message(self):
        return self.browser.find_element(*self.LOGIN_TEXT).text

    def login(self, username, password):
        self.input_username(username)
        self.input_password(password)
        self.click_login_button()

