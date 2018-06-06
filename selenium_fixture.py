from selenium import webdriver
import pytest
from model.application import Application

<<<<<<< HEAD

@pytest.fixture(scope="module")
def app(request, browser_type, base_url):
    if browser_type == "Chrome":
        driver = webdriver.Chrome()
    elif browser_type == "firefox"
        driver == webdriver.FireFox ("C:\FF_driver\geckodriver.exe")
   # driver.implicitly_wait(30)
   
@pytest.fixture
def app(request):
    driver = webdriver.Chrome()
    driver.implicitly_wait(30)

def app(request):
    driver = webdriver.Chrome()
    driver.implicitly_wait(30)

=======
@pytest.fixture
>>>>>>> parent of 0d28f7e... add asserts (login, logout)
def app(request):
    driver = webdriver.Chrome()
    driver.implicitly_wait(30)
    request.addfinalizer(driver.quit)
    return Application(driver)

