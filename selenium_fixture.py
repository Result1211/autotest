from selenium import webdriver
import pytest
from model.application import Application


@pytest.fixture(scope="module")
def app(request, browser_type, base_url):
    if browser_type == "Chrome":
        driver = webdriver.Chrome()
    elif browser_type == "firefox"
        driver == webdriver.FireFox ("C:\FF_driver\geckodriver.exe")
   # driver.implicitly_wait(30)
    request.addfinalizer(driver.quit)
    return Application(driver, base_url)

