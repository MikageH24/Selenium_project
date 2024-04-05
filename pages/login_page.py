import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from base.base_class import Base
from time import sleep
from utilities.logger import Logger


class LoginPage(Base):

    tel = '9786123098'
    password = 'StrongPassword1'

    # Locators
    login_btn_loc = '//div[@class="navbar-large_xs__navigation_box__item__r7bhm"][3]'
    login_input_loc = '//input[@id="user_login"]'
    password_input_loc = '//input[@id="user_password"]'
    submit_btn_loc = '//button[@type="submit"][1]'
    profile_title_loc = '//a[@href="/ru/ru/my/profile"]/div/div/div'
    cookies_alert_close_btn = '//div[@class="message_message_cookies__close_event__vdFyS"]'

    # Getters
    def get_login_btn(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_btn_loc)))

    def get_login_input_loc(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_input_loc)))

    def get_password_input_loc(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password_input_loc)))

    def get_login_submit_btn(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.submit_btn_loc)))

    def get_profile_title(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.profile_title_loc)))

    def get_close_cookies_alert(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cookies_alert_close_btn)))

    # Actions
    def click_login_btn(self):
        self.get_login_btn().click()

    def input_login(self):
        self.get_login_input_loc().send_keys(self.tel)

    def input_password(self):
        self.get_password_input_loc().send_keys(self.password)

    def click_login_submit_btn(self):
        self.get_login_submit_btn().click()

    def click_close_cookies_alert(self):
        self.get_close_cookies_alert().click()

    # Methods
    def authorize(self):
        """Authorizing on the website"""
        with allure.step("Authorization"):
            Logger.add_start_step(method="authorize")
            self.click_login_btn()
            print("Click Login button")
            self.input_login()
            print("Input Login")
            self.input_password()
            print("Input Password")
            self.click_login_submit_btn()
            print("Click Login Submit button")
            sleep(6)
            self.assert_word(self.get_profile_title(), "ПРОФИЛЬ")
            self.click_close_cookies_alert()
            print("Cookies alert is closed")
            print("Authorization is successful")
            Logger.add_end_step(url=self.driver.current_url, method="authorize")

