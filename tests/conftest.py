import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep


@pytest.fixture(autouse=True, scope="function")
def set_up(request):
    print("Test starts")
    options = webdriver.ChromeOptions()
    options.page_load_strategy = 'eager'
    driver = webdriver.Chrome(options=options)
    driver.delete_all_cookies()
    driver.maximize_window()
    yield driver
    driver.quit()
    sleep(5)
    print("Test finishes")
