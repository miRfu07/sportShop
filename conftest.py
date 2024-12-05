import pytest
from selenium import webdriver




@pytest.fixture()
def set_up():
    print('\nначало пути')


    yield

    print('\nконец непростого пути')
    print('\nДля возобновления ПОЛНОГО тестирования необходимо вернуться в'
          ' корзину и удалить последний заказ')
    # driver.quit()


@pytest.fixture(scope='module')
def set_group():
    print('\nвход в систему')
    # driver = webdriver.Chrome(options=options)
    # url = 'https://www.saucedemo.com/'
    # self.driver.get(self.url)

    yield

    print('\nвыход из системы')
    # driver.quit()