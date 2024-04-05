import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from base.base_class import Base

from time import sleep

from utilities.logger import Logger


class SpecificProductPage(Base):

    # Locators
    select_size_m_loc = '//li[@class="  p-relative    "][3]'
    select_add_to_cart_btn_loc = '//div[@class="product-content_product_detail_btn_place_bt__LokUV"]/button'
    select_enter_cart_btn_loc = '//div[@class="sidebar-cart_sidebar_cart_content__bottom_content__zi3J_"]/button'

    # Getters
    def get_dress_title(self):
        return self.driver.find_element(By.TAG_NAME, "h1")

    def get_size_m_dress(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_size_m_loc)))

    def get_add_to_cart_btn(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_add_to_cart_btn_loc)))

    def get_enter_cart_btn(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_enter_cart_btn_loc)))

    # Actions
    def click_select_size_m(self):
        self.get_size_m_dress().click()
        print("The size M is selected")

    def click_add_to_cart_btn(self):
        self.get_add_to_cart_btn().click()
        print("The dress is added to cart")

    def click_enter_cart(self):
        self.get_enter_cart_btn().click()
        print("Enter the cart")

    # Methods
    def add_the_dress_to_cart(self):
        """Adding the selected dress to the cart"""
        with allure.step("Add the dress to cart"):
            Logger.add_start_step(method="add_the_dress_to_cart")
            self.assert_word(self.get_dress_title(), "Трикотажное платье макси с декором на бретелях")
            sleep(3)
            self.click_select_size_m()
            self.click_add_to_cart_btn()
            self.click_enter_cart()
            sleep(5)
            self.assert_url('https://lichi.com/ru/ru/cart')
            Logger.add_end_step(url=self.driver.current_url, method="add_the_dress_to_cart")
