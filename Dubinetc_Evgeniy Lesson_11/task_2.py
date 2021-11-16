print("Задача 2")
# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.


class Except:
    # принимаю число
    def __init__(self, num):
        # записываю его в атрибут
        self.num = num


def division():
    try:
        # запрашиваю у пользователя делимое и делитель, и проверяю введено число или нет
        num_1 = int(input('Введите делимое: '))
        num_2 = int(input('Введите делитель: '))
        # проверяю делитель не равен ли он 0
        if num_2 == 0:
            return "Делить на ноль нельзя!"
        else:
            result = num_1 / num_2
            return result
    # если введено не число, либо другая ошибка - возвращаю пользователю инфу об ошибке
    except ValueError:
        return "Ошибка! Введено не число"
    except Except as err:
        return err


print(division())
