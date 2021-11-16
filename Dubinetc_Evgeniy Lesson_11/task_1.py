print("Задача 1")
# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod. Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

from datetime import date


class Data:
    # принимаю дату
    def __init__(self, data):
        # записываю её в атрибут
        self.data = data

    @classmethod
    def type(cls, data):
        try:
            # с помощью list comprehension преобразовываю строчный тип к типу «Число»
            day, month, year = [int(i) for i in data.split('-')]
            # возвращаю типы числа, месяца и года
            return f"{type(day), day},{type(month), month},{type(year), year}"
        except ValueError:
            return 'Введена некорректная дата!'

    @staticmethod
    def valid(data):
        try:
            # разбиваю строку по делителю '-' на число, месяц, год
            day, month, year = data.split('-')
            # провожу валидацию числа, месяца и года
            date(int(year), int(month), int(day))
            return 'Введена корректная дата'
        except ValueError:
            return 'Введена некорректная дата!'


print(Data.valid('12-11-2021'))
print(Data.type('12-11-2021'))
print(Data.valid('12-25'))
