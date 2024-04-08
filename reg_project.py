import re
import os
import glob
import json
import time

print('Анализ файлов Python.\n')
time.sleep(3)
print('Идёт подготовка файлов, подождите.. \n')


class Analyzer():  # Реализует функции в виде методов класса.
    def __init__(self):
        self.info = {}
        self.__py_files = self.__search_py_files()

    def get_file_info(self, file_read):
        """Извлекает информацию из файла"""
        classes = re.findall(r'class\s[A-Za-z0]*:', file_read)
        functions = re.findall(r'def\s[a-zA-Z]+\(\w*\):', file_read)
        variables = re.findall(r'([A-Za-z0-9-]*)\s=', file_read)
        return {'classes': classes, 'functions': functions, 'variables': variables}

    def __search_py_files(self):
        """Находит все файлы с рашсиирением .py."""
        my_directory = 'C:\\'
        search = os.path.join(my_directory, '**', '*.py')
        python_files = glob.glob(search, recursive=True)
        return python_files

    def save_info(self, filename):
        """Сохраняет данные о файле."""
        with open(filename, 'w', encoding='utf-8', errors='ignore') as info_file:
            for python_file in self.__py_files:
                with open(python_file, 'r', encoding='utf-8') as pf:
                    try:
                        file_code = pf.read()
                        info_result = self.get_file_info(file_code)
                        self.info[python_file] = info_result
                    except Exception as e:
                        print(f'Ошибка при обработке файла: {python_file}')
            json.dump(self.info, info_file)

    def show_data(self, filename):
        """Сохраняет информацию о программах в текстовый файл."""
        with open(filename, 'w', encoding='utf-8', errors='ignore') as result_file:
            for key, value in self.info.items():
                result_file.write(f'Программа: {key}\n')
                result_file.write(f'Результат анализа: {value}\n\n')


analyzer_beta = Analyzer()

result_beta_file_name = input('Введите название первого файла: ')
result_file_name = input('Введите название второго файла: ')
print('\nИдёт анализ..\n')
analyzer_beta.save_info(f'{result_beta_file_name}.txt')
analyzer_beta.show_data(f'{result_file_name}.txt')
print('\nАнализ завершён!')
