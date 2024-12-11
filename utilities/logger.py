import datetime
import os


class Logger():
    file_name = f"C:\\Users\\aternov\\main\\SportShop\\logs\\log_" + str(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")) + ".log"

    @classmethod
    def write_log_to_file(cls, data: str): # cls - работает как принадлежность self. далее идёт запись данных в формате строки
        with open(cls.file_name, 'a', encoding='utf=8') as logger_file: # конструкция открытия файла и добавление записей "а" кодировкой ютф
            logger_file.write(data)

    @classmethod
    def add_start_step(cls, method: str):
        test_name = os.environ.get('PYTEST_CURRENT_TEST')

        # к переменной каждый раз приплюсовывается новые значения и далее записывается в лог
        data_to_add = f"\n-----\n"
        data_to_add += f"Test: {test_name}\n"  # т.к. переменная указана выше, ей не требуется указание str
        data_to_add += f"Start time: {str(datetime.datetime.now())}\n"
        data_to_add += f"Start name method: {method}\n"
        data_to_add += "\n"

        # передаются записанные строки в другую функцию
        cls.write_log_to_file(data_to_add)

    @classmethod
    def add_end_step(cls, url: str, method: str): # явно указываем способ записи переменных

        data_to_add = f"End time: {str(datetime.datetime.now())}\n"
        data_to_add += f"End name method: {method}\n"
        data_to_add += f"URL: {url}\n"
        data_to_add += f"\n-----\n"

        cls.write_log_to_file(data_to_add)