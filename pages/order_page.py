from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
import pytest

from base.base_class import Base


class order_page(Base):

    def __init__(self, driver):
        super().__init__(driver)  # указываем, что это потомок
        self.action = ActionChains(self.driver)
        self.driver = driver

    # Locators

    current_url = 'https://lactomin.ru/personal/order/make/'
    next_btn = '//a[contains(text(), "Далее")]'
    delivery_btn = '//a[contains(text(), " Выбрать пункт самовывоза")]'
    delivery_address = '//*[@id="PVZ_MSK1005"]'
    delivery_accept = '//*[@id="SDEK_button"]'
    payment_card = '(//div[@class="bx-soa-pp-company-graf-container"])[2]'
    mail = '//*[@id="soa-property-2"]'
    phone = '//*[@id="soa-property-3"]'
    name = '//*[@id="soa-property-20"]'
    family = '//*[@id="soa-property-1"]'
    postcode = '//*[@id="soa-property-4"]'
    cookie = '//*[@id="setCookie"]'
    continue_button = '//*[@id="bx-soa-orderSave"]/a'
    capcha = '(//div[@class="alert alert-danger"])[1]'

    # Getters

    def get_next_btn(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.next_btn)))

    def get_delivery_btn(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.delivery_btn)))

    def get_delivery_address(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.delivery_address)))

    def get_delivery_accept(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.delivery_accept)))

    def get_payment_card(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.payment_card)))

    def get_mail(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.mail)))

    def get_phone(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.phone)))

    def get_name(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.name)))

    def get_family(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.family)))

    def get_postcode(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.postcode)))

    def get_cookie(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.cookie)))

    def get_continue_btn(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.continue_button)))

    def get_capcha(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.capcha)))

    # Actions

    def click_next_btn(self):
        self.get_next_btn().click()
        print('next')

    def click_delivery_btn(self):
        self.get_delivery_btn().click()
        print('clicked dlvry btn')

    def click_delivery_address(self):
        self.get_delivery_address().click()
        print('clicked dlvry address')

    def click_delivery_accept(self):
        self.get_delivery_accept().click()
        print('clicked dlvry accept')

    def click_payment_card(self):
        self.get_payment_card().click()
        print('payment by card')

    def enter_mail(self, mail):
        # при прохождении авторизации подтягиваются старые данные, поэтому необходимо их стереть сначала
        self.get_mail().send_keys(Keys.CONTROL+"a")
        self.get_mail().send_keys(mail)
        print('enter mail')

    def enter_phone(self, phone):
        self.get_phone().send_keys(phone)
        print('enter phone')

    def enter_name(self, name):
        # при прохождении авторизации подтягиваются старые данные, поэтому необходимо их стереть сначала
        self.get_name().send_keys(Keys.CONTROL+"a")
        self.get_name().send_keys(name)
        print('enter name')

    def enter_family(self, family):
        # при прохождении авторизации подтягиваются старые данные, поэтому необходимо их стереть сначала
        self.get_family().send_keys(Keys.CONTROL+"a")
        self.get_family().send_keys(family)
        print('enter family')

    def enter_postcode(self, z1p):
        # при прохождении авторизации подтягиваются старые данные, поэтому необходимо их стереть сначала
        self.get_postcode().send_keys(Keys.CONTROL+"a")
        self.get_postcode().send_keys(z1p)
        print('entered postal code')

    def click_cookie(self):
        self.get_cookie().click()
        print('cookie closed')

    def click_continue(self):
        self.get_continue_btn().click()
        print('clicked continue')

    # Methods

    def info_for_order(self):
        self.assert_url(self.current_url)
        self.get_current_url()
        self.click_next_btn()
        self.click_delivery_btn()
        self.click_delivery_address()
        self.click_delivery_accept()
        # почему-то без явного ожидания тест падает после каждого нажатия ДАЛЕЕ и не хочет ждать появления кнопок
        time.sleep(2)
        self.click_next_btn()
        time.sleep(2)
        self.click_payment_card()
        time.sleep(2)
        self.click_next_btn()
        time.sleep(2)
        self.enter_mail('ternovia123@mail.ru')
        self.enter_phone('79165555555')
        self.enter_name('Qwe')
        self.enter_family('Asd')
        self.enter_postcode('101101')
        self.click_next_btn()
        time.sleep(2)
        self.click_cookie() # из-за этого банера не получается нажать на кнопку оформить заказ
        self.click_continue()  # далее требуется ввести капчу и заказ сразу сформируется, поэтому не перехожу дальше
        self.assert_word(self.get_capcha(), 'Капча не пройдена')
        print('Капча не пройдена')
