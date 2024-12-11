import os
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
        # создание уникального скриншота и сохранение в отдельную папку
        date_now = datetime.datetime.now().strftime('%Y.%m.%d.%H.%M.%S')  # для того, чтобы скрин каждый раз был новым
        # Задаем НЕ корневую директорию проекта
        parent_folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        # Формируем путь до папки screen внутри проекта
        screenshots_folder = os.path.join(parent_folder, 'screen')
        # Убедимся, что папка существует, если нет – создадим её
        os.makedirs(screenshots_folder, exist_ok=True)
        # Сохраняем скриншот
        ultraSS = 'screen' + date_now + '.jpg'  # Имя файла
        filename = os.path.join(screenshots_folder, ultraSS)
        self.driver.save_screenshot(filename)
        print('screenshot is rdy')

    """Method assert URL"""

    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print('url is correct')