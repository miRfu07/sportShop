from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
import pytest

from base.base_class import Base
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)

class main_page(Base):

    def __init__(self, driver):
        super().__init__(driver)  # указываем, что это потомок
        self.action = ActionChains(self.driver)
        self.driver = driver

    # Locators

    catalog = '//a[contains(text(), "Каталог товаров")]'
    protein = '//a[contains(text(), "Протеины")]'
    price = '//*[@id="right_slider_8f14e45fceea167a5a36dedd4bea2543"]'
    watch_btn = '//*[@id="modef"]/a'
    sivorotka = '//*[@id="arrFilter_794_4071888190"]'
    chocolate = '//*[@id="arrFilter_609_1233273162"]'
    sort = '//a[@class="section_sort-param active "]'
    sort_expensive = '//span[contains(text(),"по убыванию цены")]'
    plus_btn = '(//span[@class="product-item-amount-field-btn-plus no-select"])[1]'
    add_to_cart = '(//a[@class="scu_var_buy"])[1]'
    go_to_cart = '//span[@class="btn btn-default btn-buy btn-sm"][1]'

    # Getters

    def get_catalog(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.catalog)))

    def get_protein(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.protein)))

    def get_price(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.price)))

    def get_watch_btn(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.watch_btn)))

    def get_sivorotka(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.sivorotka)))

    def get_chocolate(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.chocolate)))

    def get_sort(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.sort)))

    def get_sort_expensive(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.sort_expensive)))

    def get_plus_btn(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.plus_btn)))

    def get_add_to_cart(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.add_to_cart)))

    def get_go_to_cart(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.go_to_cart)))

    # Actions

    def click_catalog(self):
        self.get_catalog().click()
        print('clicked catalog')

    def click_protein(self):
        self.get_protein().click()
        print('clicked protein')

    def click_and_hold_price(self):
        self.action.click_and_hold(self.get_price()).move_by_offset(-100, 0).release().perform()
        print('edit price dimension')

    def click_watch_btn(self):
        self.get_watch_btn().click()
        print('watch edit')

    def click_sivorotka(self):
        self.get_sivorotka().click()
        print('sorted protein')

    def click_chocolate(self):
        # по какой-то причине просто чекбокс не кликается, а через вызов скрипта - кликается
        self.driver.execute_script("arguments[0].click();",  self.get_chocolate())
        print('taste choco')

    def click_sort(self):
        self.get_sort().click()
        print('open sort menu')

    def click_sort_expensive(self):
        self.get_sort_expensive().click()
        print('sort by expensive')

    def click_plus_btn(self):
        # по какой-то причине просто чекбокс не кликается, а через вызов скрипта - кликается
        self.driver.execute_script("arguments[0].click();", self.get_plus_btn())
        print('add +1 prod')

    def click_add_to_cart(self):
        # по какой-то причине просто чекбокс не кликается, а через вызов скрипта - кликается
        self.driver.execute_script("arguments[0].click();", self.get_add_to_cart())
        print('added tea to cart')

    def click_btn_go_to(self):
        self.get_go_to_cart().click()
        print('clicked go to cart button')


    # Methods

    def select_prod(self):
        # здесь приходилось каждый раз тыкать кнопку ПОКАЗАТЬ, чтобы обновить ассортимент
        # и один раз явно посмотреть на "ПОКАЗАТЬ", иначе система не понимала на что нажимать
        self.click_catalog()
        self.click_protein()
        self.click_and_hold_price()
        self.click_watch_btn()
        self.click_sivorotka()
        self.click_watch_btn()
        self.action.move_to_element(self.get_chocolate()).perform()
        self.click_chocolate()
        self.click_watch_btn()
        self.click_sort()
        self.click_sort_expensive()
        self.click_plus_btn()
        self.click_add_to_cart()
        self.click_btn_go_to()
