import pytest
from selenium import webdriver
import allure
from pages.cart_page import CartPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.products_page import ProductPage
from pages.specific_product_page import SpecificProductPage


@allure.description("Test buy product")
def test_buy_product(set_up):
    """Login on a website and buying a specific dress"""
    driver = set_up
    driver.get("https://lichi.com/ru/ru")

    lp = LoginPage(driver)
    lp.authorize()

    mp = MainPage(driver)
    mp.select_dresses_category()

    pp = ProductPage(driver)
    pp.select_specific_product()

    spp = SpecificProductPage(driver)
    spp.add_the_dress_to_cart()

    cp = CartPage(driver)
    cp.input_client_info()


