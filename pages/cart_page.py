from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
import pytest

from base.base_class import Base


class cart_page(Base):

    def __init__(self, driver):
        super().__init__(driver)  # указываем, что это потомок
        self.driver = driver

    # Locators

    discount = '//*[@id="basket-root"]/div[3]/div/div/div[2]/div/div[2]/div/div[3]/span'  #'//div[@class="basket-coupon-block-total-price-difference"]'
    total_price = '//div[@class="basket-coupon-block-total-price-current"]'
    order_btn = '//button[@class="btn btn-lg btn-default basket-btn-checkout"]'

    # Getters

    def get_discount(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.discount)))

    def get_total_price(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.total_price)))

    def get_order_btn(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.order_btn)))

    # Actions

    def click_order_btn(self):
        self.get_order_btn().click()
        print('clicked order')

    # Methods

    def order(self):
        self.get_current_url()
        self.get_screenshot()
        self.assert_word(self.get_discount(), '210 руб.')
        print('discount checked')
        self.assert_word(self.get_total_price(), '3 990 руб.')
        print('total price checked')
        self.click_order_btn()
