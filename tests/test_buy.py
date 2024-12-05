import datetime
import time
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import pytest

from pages.cart_page import cart_page
from pages.order_page import order_page
from pages.login_page import login_pass
from pages.main_page import main_page


options = webdriver.ChromeOptions()  # твой путь браузера-
options.add_experimental_option('detach', True)  # без неё браузер закрывается
# options.add_argument('--headless') # позволяет запускать бросер в фоновом режиме
# options.add_argument('--disable-webrtc')
# options.add_argument('--ignore-certificate-errors')
# options.add_argument('--ignore-ssl-errors')
options.add_experimental_option('excludeSwitches', ['enable-logging'])

# для запуска теста необходимо написать в терминале python -m pytest -s -v
# -v - описывается какие тесты прошли успешно\упали
# -s - вывод результата внутри самого теста
# pytest -v -s test_mail - запустит конкретный тест, а не все из папки
# -k test_select_product_3 - запустит конкретный метод, тест из файла.


def test_sport_prod(set_up):
    driver = webdriver.Chrome(options=options)

    print('Starting')

    login = login_pass(driver)
    login.authorization()

    mp = main_page(driver)
    mp.select_prod()

    cp = cart_page(driver)
    cp.order()

    op = order_page(driver)
    op.info_for_order()

    print('Finished')


# использовался для быстрого прохождения до нужных моментов, минуя авторизацию и прочие пункты
def test_speed():
    driver = webdriver.Chrome(options=options)
    #url = 'https://lactomin.ru'
    url = 'https://lactomin.ru/catalog/proteiny/'
    driver.get(url)
    mp = main_page(driver)
    mp.click_add_to_cart()
    mp.click_btn_go_to()

    cp = cart_page(driver)
    cp.click_order_btn()

    op = order_page(driver)
    op.info_for_order()

