import time
import datetime


class Base():
    def __init__(self, driver):
        self.driver = driver


    """Method get current URL"""

    def get_current_url(self):
        get_url = self.driver.current_url
        print('Current URL is: ' + get_url)


    """Method assert word"""

    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        # print('Word was checked')


    """Method screenshot"""

    def get_screenshot(self):
        # # создание уникального скриншота и сохранение в отдельную папку
        date_now = datetime.datetime.now().strftime('%Y.%m.%d.%H.%M.%S') # для того, чтобы скрин каждый раз был новым
        ultraSS = 'screen' + date_now + '.jpg'
        time.sleep(1)
        self.driver.save_screenshot('C:\\Users\\aternov\\main\\SportShop\\screen\\' + ultraSS)

    """Method assert URL"""

    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print('url is correct')