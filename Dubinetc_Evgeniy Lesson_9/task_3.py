print("Задача 3")
# Реализовать базовый класс Worker (работник).
# определить атрибуты: name, surname, position (должность), income (доход);
# последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: оклад и премия,
# например, {"wage": wage, "bonus": bonus};
# создать класс Position (должность) на базе класса Worker;
# в классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учётом премии (get_total_income);
# проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные,
# проверить значения атрибутов, вызвать методы экземпляров.

from decimal import *
class Worker:


    def __init__(self, name, surname, position, income):
        # каждый атрибут записываю в свой защищенный атрибут
        self.name = name
        self.surname = surname
        self.position = position
        self._income_wage = income['wage']
        self._income_bonus = income['bonus']


# создаю класс Position (должность) на основе класса Worker
class Position(Worker):


    def get_full_name(self):
        # методом возвращаю имя, фамилию и должность
        return f'{self.name} {self.surname} {self.position}'


    def get_total_income(self):
        # использую Decimal для более точного суммирывания оклада и премии
        return f"{Decimal(self._income_wage + self._income_bonus)}"


# передаю данные
pos = Position('Петр', 'Петров', 'тракторист', {"wage": 45000.55, "bonus": 17000.33})

print(pos.get_full_name())
print(pos.get_total_income())
