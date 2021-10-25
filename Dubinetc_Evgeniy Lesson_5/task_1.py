print("Задача 1")
# Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield, например:
# >>> odd_to_15 = odd_nums(15)
# >>> next(odd_to_15)
# 1
# >>> next(odd_to_15)
# 3
# ...
# >>> next(odd_to_15)
# 15
# >>> next(odd_to_15)
# ...StopIteration


def odd_nums_w(my_num):
    # задаю значение n
    n = 1
    # пока n будет меньше или равен max_value возвращает значение
    while n <= my_num:
        yield n
        # увеличивает n на 2 и повторяет итерацию
        n += 2


odd_to_15 = odd_nums_w(15)
