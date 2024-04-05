import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from base.base_class import Base

from time import sleep

from utilities.logger import Logger


class ProductPage(Base):

    # Locators
    select_color_loc = '//label[@for="Черный"]'
    select_size_loc = '//label[@for="M"]'
    select_material_loc = '//label[@for="Вискоза"]'
    select_price_loc = '//label[@for="7499"]'
    select_specific_dress_loc = '//div[contains(@class, "catalog-card_grid_3__FVgai")]'
    select_filter_loc = '//button[@class="filter-miu_filter_btn__g0HBJ"]'

    # Getters
    def get_filter_button(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.select_filter_loc)))

    def get_select_black_color(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.select_color_loc)))

    def get_select_m_size(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.select_size_loc)))

    def get_select_viscose_material(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.select_material_loc)))

    def get_select_up_to_7499_price(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.select_price_loc)))

    def get_select_specific_dress(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.select_specific_dress_loc)))

    # Actions
    def click_filter_btn(self):
        self.get_filter_button().click()

    def click_select_black_color(self):
        self.click_filter_btn()
        self.get_select_black_color().click()
        print("Click Select Color")

    def click_select_m_size(self):
        self.click_filter_btn()
        self.get_select_m_size().click()
        print("Click Select Size")

    def click_select_viscose_material(self):
        self.click_filter_btn()
        self.get_select_viscose_material().click()
        print("Click Select Material")

    def click_select_up_to_7499_price(self):
        self.click_filter_btn()
        self.get_select_up_to_7499_price().click()
        print("Click Select Price")

    def click_select_specific_dress(self):
        self.get_select_specific_dress().click()
        print("Click dress with specific parameters")

    # Methods

    def select_specific_product(self):
        """Selecting a dress with specific parameters"""
        with allure.step("Select specific product"):
            Logger.add_start_step(method="select_specific_product")
            self.get_current_url()
            self.click_select_black_color()
            self.click_select_m_size()
            self.click_select_viscose_material()
            self.click_select_up_to_7499_price()
            sleep(1)
            self.click_select_specific_dress()
            sleep(3)
            self.assert_url("https://lichi.com/ru/ru/product/46549")
            Logger.add_end_step(url=self.driver.current_url, method="select_specific_product")
