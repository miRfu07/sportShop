from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
import pytest

from base.base_class import Base
from utilities import logger


class Cart_page(Base):

    def __init__(self, driver):
        super().__init__(driver)  # указываем, что это потомок
        self.driver = driver

    # Locators

    discount = '//*[@id="basket-root"]/div[3]/div/div/div[2]/div/div[2]/div/div[3]/span'
    total_price = '//div[@class="basket-coupon-block-total-price-current"]'
    order_btn = '//button[@class="btn btn-lg btn-default basket-btn-checkout"]'
    cancel = '//span[@class="basket-item-actions-remove"]'

    # Getters

    def get_discount(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.discount)))

    def get_total_price(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.total_price)))

    def get_order_btn(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.order_btn)))

    def get_cancel_btn(self):
        return self.driver.find_element(By.XPATH, self.cancel)  # здесь применяется явный поиск элемента, т.к. элемент невидимый

    # Actions

    def click_order_btn(self):
        self.get_order_btn().click()
        print('clicked order')

    def click_cancel_btn(self):
        time.sleep(2)
        self.get_cancel_btn().click()
        print('clicked cancel' + '\nЗаказ пуст')

    # Methods

    def order(self):
        logger.Logger.add_start_step(method='order')
        self.get_current_url()
        # выполнение скриншота корзины с указанием текущей даты
        self.get_screenshot()
        # сравнение суммы скидки
        self.assert_word(self.get_discount(), '210 руб.')
        print('discount checked')
        # сравнение итоговой суммы
        self.assert_word(self.get_total_price(), '3 990 руб.')
        print('total price checked')
        self.click_order_btn()
        logger.Logger.add_end_step(url=self.driver.current_url, method='order')
