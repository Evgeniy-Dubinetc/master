print("Задача 7")
# Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число».
# Реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта.
# Для этого создаёте экземпляры класса (комплексные числа), выполните сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.


class ComplexNumber:
    # принимаю a, b и *args
    def __init__(self, a, b, *args):
        # записываю их в атрибуты
        self.a = a
        self.b = b
        self.c = 'a + b * i'

    def __add__(self, other):
        print(f'Сумма с_1 и с_2 равна')
        # возвращаю сумму
        return f'c = {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        print(f'Произведение с_1 и с_2 равно')
        # возвращаю произведение
        return f'c = {(self.a * other.a) - (self.b * other.b)} + {self.b * other.a} * i'

    def __str__(self):
        return f'c = {self.a} + {self.b} * i'


c_1 = ComplexNumber(7, 5)
c_2 = ComplexNumber(7, 5)
print(c_1)
print(c_1 + c_2)
print(c_1 * c_2)
