import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


# def parser_addoption(parser):
#     parser.addoption(
#         "--browser_name", action="store", default="chrome"
#     )


@pytest.fixture(scope="class")
def setup(request):
    global driver
    #
    # browser = request.config.getoption("browser_name")
    #
    # if browser == "chrome":

    driver = webdriver.Chrome(service=Service(ChromeDriverManager.install()))

    driver.get("https://demowebshop.tricentis.com/")
    request.cls.driver = driver

    yield
    driver.close()


def capture_screenshot(name):
    driver.get_screenshot_as_file(name)
