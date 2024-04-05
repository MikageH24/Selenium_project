import datetime
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

class Base:

    def __init__(self, driver):
        self.driver = driver

    """Method to get current url"""
    def get_current_url(self):
        get_url = self.driver.current_url
        print(f"Current url: {get_url}")

    """Method to assert a word"""

    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result, f"{value_word} is not {result}"
        print("Word assertion passed")

    """Method to make a screenshot"""

    def make_screenshot(self):
        now_date = datetime.datetime.now().strftime("%Y.%m.%d.%H.%M.%S")
        screenshot_name = "screenshot" + now_date + ".png"
        self.driver.save_screenshot(f'..\\screen\\{screenshot_name}')
        print("Screenshot is made")

    """Method to assert an url"""

    def assert_url(self, result):
        get_url = self.driver.current_url
        assert result in get_url, f"{get_url} is not {result}"
        print("URL assertion passed")
