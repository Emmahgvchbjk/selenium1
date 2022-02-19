import pytest
import time
import selenium.webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def browser():
    # initializam instanta de Chromedriver, se deschide tabul de chrome
    driver = selenium.webdriver.Chrome(service = Service(ChromeDriverManager().install()))
    driver.get("http://the-internet.herokuapp.com/login")
    driver.implicitly_wait(10)
    #return the webdriver instance
    yield driver
    #close the driver
    time.sleep(5)
    # driver.quit()