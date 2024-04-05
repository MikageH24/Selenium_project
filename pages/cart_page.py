import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from base.base_class import Base
from faker import Faker
from time import sleep

from utilities.logger import Logger

fake = Faker('en_US')


class CartPage(Base):

    # Locators
    select_first_name_loc = "//input[@id='u_firstname']"
    select_middle_name_loc = "//input[@id='u_middlename']"
    select_last_name_loc = "//input[@id='u_lastname']"
    select_submit_btn_loc = "//button[@type='submit']"

    select_city_loc = "//div[@id='city']"
    select_city_listbox_loc = "//div[@id='react-select-4-listbox']"
    select_moscow_loc = "//*[text()='Москва, Москва']"

    select_zip_code_loc = "//input[@id='zip_code']"
    select_address_line_loc = "//input[@id='address_line']"
    select_house_num_loc = "//input[@id='house_number']"
    select_flat_num_loc = "//input[@id='flat_number']"

    select_delivery_loc = "//label[@for='2']"
    select_card_payment_loc = "//label[@for='5']"
    select_finish_order_btn_loc = "//span[text()='Перейти к оплате']/.."

    # Getters
    def get_first_name(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.select_first_name_loc)))

    def get_middle_name(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.select_middle_name_loc)))

    def get_last_name(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.select_last_name_loc)))

    def get_submit_btn(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.select_submit_btn_loc)))

    def get_city_input(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.select_city_loc)))

    def get_city_listbox(self):
        return WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.select_city_listbox_loc)))

    def get_moscow_in_list(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.select_moscow_loc)))

    def get_zip_code(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.select_zip_code_loc)))

    def get_address_line(self):
        return WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.select_address_line_loc)))

    def get_house_number(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.select_house_num_loc)))

    def get_flat_number(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.select_flat_num_loc)))

    def get_delivery(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.select_delivery_loc)))

    def get_card_payment(self):
        return WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.select_card_payment_loc)))

    def get_finish_order_btn(self):
        return WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, self.select_finish_order_btn_loc)))

    # Actions
    def input_personal_info(self):
        self.get_first_name().send_keys(fake.first_name())
        self.get_middle_name().send_keys(fake.first_name())
        self.get_last_name().send_keys(fake.last_name())
        self.get_submit_btn().click()
        print("Input personal information")

    def select_city(self):
        self.get_city_input().click()
        sleep(1)
        listbox = self.get_city_listbox()
        action = ActionChains(self.driver)
        action.move_to_element(listbox).perform()
        sleep(1)
        self.get_moscow_in_list().click()
        print("Select city")

    def input_address_info(self):
        self.get_zip_code().send_keys(fake.postcode())
        self.get_address_line().send_keys(fake.street_name())
        self.get_house_number().send_keys(fake.pyint())
        self.get_flat_number().send_keys(fake.pyint())
        self.get_submit_btn().click()
        print("Input address information")

    def select_delivery_type(self):
        self.get_delivery().click()
        print("Select delivery type")

    def select_card_payment(self):
        self.get_card_payment().click()
        print("Select card payment")

    def click_finish_order_btn(self):
        self.get_finish_order_btn().click()
        print("Click finish ordering button")

    # Methods
    def input_client_info(self):
        with allure.step("Input client information"):
            Logger.add_start_step(method="input_client_info")
            self.input_personal_info()
            self.select_city()
            self.input_address_info()
            self.select_delivery_type()
            self.select_card_payment()
            sleep(1)
            self.click_finish_order_btn()
            sleep(3)
            self.assert_url('https://securecardpayment.ru/payment/')
            self.make_screenshot()
            print("Ordering is completed")
            Logger.add_end_step(url=self.driver.current_url, method="input_client_info")
