print("Задача 6")
# Реализовать простую систему хранения данных о суммах продаж булочной.
# Должно быть два скрипта с интерфейсом командной строки: для записи данных и для вывода на экран записанных данных.
# При записи передавать из командной строки значение суммы продаж.
# Для чтения данных реализовать в командной строке следующую логику:
# просто запуск скрипта — выводить все записи;
# запуск скрипта с одним параметром-числом — выводить все записи с номера, равного этому числу, до конца;
# запуск скрипта с двумя числами — выводить записи, начиная с номера, равного первому числу, по номер,
# равный второму числу, включительно.
# Подумать, как избежать чтения всего файла при реализации второго и третьего случаев.
# Данные хранить в файле bakery.csv в кодировке utf-8. Нумерация записей начинается с 1. Примеры запуска скриптов:

# python add_sale.py 5978,5
# python add_sale.py 8914,3
# python add_sale.py 7879,1
# python add_sale.py 1573,7
# python show_sales.py
# 5978,5
# 8914,3
# 7879,1
# 1573,7
# python show_sales.py 3
# 7879,1
# 1573,7
# python show_sales.py 1 3
# 5978,5
# 8914,3
# 7879,1


# add_sale.py
import sys
# получаю цену из переменных окружения
price = sys.argv[1]
# открываю файл
with open('bakery.csv', 'a', encoding='utf-8') as f:
    # записываю в файл и перевожу каретку на новую строку
    f.write(price + '\n')

# >>> python add_sale.py 100


# show_sales.py
import sys

# в список nums записываю все, что передается из переменных окружения
nums = sys.argv[1:]
with open('bakery.csv', encoding='utf-8') as f:
    # если длина nums больше 1
    if len(nums) > 1:
        # создаю стартовый и конечный индекс
        start_idx = int(nums[0])
        end_idx = int(nums[1])
    # если длина nums равна 0
    elif len(nums) == 0:
        # создаю стартовый индекс = 0
        start_idx = 0
        # создаю конечный индекс как сумму строк
        end_idx = sum(1 for line in f)
        # перевожу каретку в начало файла
        f.seek(0)
    # если длина nums равна 1
    else:
        # создаю стартовый индекс
        start_idx = int(nums[0])
        # создаю конечный индекс как сумму строк
        end_idx = sum(1 for line in f)
        # перевожу каретку в начало файла
        f.seek(0)
    # в цикле с помощью enumerate получаю линию индекс и линию (idx, line) из файла
    for idx, line in enumerate(f):
        # если стартовый индекс <= следующего индекса + 1(потому что начинается с 0) и этот индекс <= конечного индекса
        if start_idx <= idx + 1 <= end_idx:
            # вывожу на печать строку
            print(line.strip())

# >>> python show_sales.py 1 6
