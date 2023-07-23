import logging
import sys
from colorama import init, Fore

# Инициализация colorama
init()

class Logger:
    def __init__(self, filename):
        self.filename = filename
        self.logger = logging.getLogger("my_logger")
        self.logger.setLevel(logging.DEBUG)

        self.console_handler = logging.StreamHandler(stream=sys.stdout)  # Устанавливаем поток sys.stdout для поддержки UTF-8
        self.console_formatter = logging.Formatter(Fore.RED + '%(levelname)s - %(message)s' + Fore.RESET)  # Используем colorama для красного цвета
        self.console_handler.setFormatter(self.console_formatter)
        self.logger.addHandler(self.console_handler)

        self.file_handler = logging.FileHandler(filename, encoding='utf-8')  # Добавляем поддержку UTF-8 для файлового обработчика
        self.file_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        self.file_handler.setFormatter(self.file_formatter)
        self.logger.addHandler(self.file_handler)

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)
