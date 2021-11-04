print("Задача 4")
# Написать декоратор с аргументом-функцией (callback), позволяющий валидировать входные значения функции
# и выбрасывать исключение ValueError, если что-то не так
# например:
# def val_checker...
#     ...
#
#
# @val_checker(lambda x: x > 0)
# def calc_cube(x):
#    return x ** 3
#
#
# >>> a = calc_cube(5)
# 125
# >>> a = calc_cube(-5)
# Traceback (most recent call last):
#   ...
#     raise ValueError(msg)
# ValueError: wrong val -5
# Примечание: сможете ли вы замаскировать работу декоратора?


# импортирую wraps - декоратор для скрытия работы декоратора
from functools import wraps

# передаю в декоратор функцию, при помощи которой декорирую


def val_checker(decorator_check_func):
    # принимаю на вход саму функцию
    def _val_checker(func_calc_cube):
        @wraps(func_calc_cube)
        # декоратор принимает аргумент функции
        def wrapped(x):
            # проверяю, если все норм возвращаю
            if decorator_check_func(x):
                return func_calc_cube(x)
            else:
                # если что-то не так, выдаю ошибку - ValueError
                raise ValueError(x)

        # возвращаю обёртку
        return wrapped

    # возвращаю обёртку верхнего уравня
    return _val_checker


@val_checker(lambda x: x > 0)
# создаю функцию для получения кубов
def calc_cube(x):
    """calc_cube desc"""
    return x ** 3


a = calc_cube(7)
# вывожу результаты
print(a)
print(calc_cube.__name__)
print(calc_cube.__doc__)
