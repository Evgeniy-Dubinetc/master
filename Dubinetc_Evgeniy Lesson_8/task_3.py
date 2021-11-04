print("Задача 3")
# Написать декоратор для логирования типов позиционных аргументов функции, например:
# def type_logger...
#     ...
#
# @type_logger
# def calc_cube(x):
#    return x ** 3
#
# >>> a = calc_cube(5)
# 5: <class 'int'>
# Примечание: если аргументов несколько - выводить данные о каждом через запятую;
# можете ли вы вывести тип значения функции? Сможете ли решить задачу для именованных аргументов?
# Сможете ли вы замаскировать работу декоратора? Сможете ли вывести имя функции, например, в виде:
# >>> a = calc_cube(5)
# calc_cube(5: <class 'int'>)


# импортирую wraps - декоратор для скрытия работы декоратора
from functools import wraps

# создаю декоратор который принимает функцию


def type_logger(func):
    # принимаю аргументы
    @wraps(func)
    def wrapper(*args):
        # прохожу в цикле по аргументам
        for arg in args:
            # вывожу имя функции, аргумент и тип аргумента, в конце ставлю запятую с пробелом
            print(f'{func.__name__}({arg}: {type(arg)})', end=', ')
        return func(*args)

    return wrapper


@type_logger
# создаю функцию для получения кубов
def calc_cube(*args):
    """this shows only 'from functools import wraps'"""
    return list(map(lambda x: x ** 3, args))


a = calc_cube(5, 7)
# вывожу результаты
print(a)
print(calc_cube.__name__)
print(calc_cube.__doc__)
