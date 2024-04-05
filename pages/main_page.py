import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from base.base_class import Base

from time import sleep

from utilities.logger import Logger


class MainPage(Base):

    # Locators
    select_clothes_loc = '//a[@href="/ru/ru/category/clothes"]'
    select_dresses_loc = '//a[@href="/ru/ru/category/dresses"]'

    # Getters
    def get_select_clothes(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_clothes_loc)))

    def get_select_dresses(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_dresses_loc)))

    # Actions
    def click_select_clothes(self):
        self.get_select_clothes().click()
        print("Click Select Clothes")

    def click_select_dresses(self):
        self.get_select_dresses().click()
        print("Click Select Dresses")

    # Methods

    def select_dresses_category(self):
        """Moving to the dresses category"""
        with allure.step("Select dresses category"):
            Logger.add_start_step(method="select_dresses_category")
            self.get_current_url()
            self.click_select_clothes()
            sleep(3)
            self.click_select_dresses()
            sleep(3)
            self.assert_url("https://lichi.com/ru/ru/category/dresses")
            Logger.add_end_step(url=self.driver.current_url, method="select_dresses_category")
