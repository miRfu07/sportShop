from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
import pytest

from base.base_class import Base


class login_pass(Base):
    url = 'https://lactomin.ru/'

    def __init__(self, driver):
        super().__init__(driver)  # указываем, что это потомок
        self.driver = driver

    # Locators

    account_btn = '//a[contains(text(), "Войти")]'
    mail = '//input[@name="USER_LOGIN"]'
    password = '//input[@name="USER_PASSWORD"]'
    login_btn = '//input[@name="Login"]'

    # Getters

    def get_account_btn(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.account_btn)))

    def get_mail(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.mail)))

    def get_password(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_login_btn(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.login_btn)))

    # Actions

    def click_account_btn(self):
        self.get_account_btn().click()
        print('cliked account button')

    def input_mail(self, mail):
        self.get_mail().send_keys(mail)
        print('mail sent')

    def input_password(self, password):
        self.get_password().send_keys(password)
        print('pass sent')

    def click_login_btn(self):
        self.get_login_btn().click()
        print('cliked login button')

    # Methods

    def authorization(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.click_account_btn()
        self.input_mail('ternovia123@mail.ru')
        self.input_password('NFC-Srp-Nfj-6Eg')  # 4m7-aHa-hAP-Z9B
        self.click_login_btn()
