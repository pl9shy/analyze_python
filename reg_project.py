import re
import os
import glob


class Analyzer():  #Реализует функции в виде методов класса.
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
        with open(filename, 'w') as python_file:
            for python_file in self.__py_files:
                with open(python_file, 'r'):
                    file_code = python_file.read()
                    info_result = self.get_file_info(file_code)
                    self.info[python_file] = info_result

    def insert_data(self):
        """Сохраняет информацию о программах в текстовый файл."""
        with open('analyze_result.txt', 'w', encoding='utf-8') as result_file:
            for key, value in self.info.items():
                result_file.write(f'Программа: {key}\n')
                result_file.write(f'Результат анализа: {value}')


analyzer_beta = Analyzer()
analyzer_beta.insert_data()
print(analyzer_beta.info)
