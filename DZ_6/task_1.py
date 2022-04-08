print("Задача 1")
# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
# Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько вариантов кода для одной и той же задачи.
# Результаты анализа вставьте в виде комментариев к коду.
# Также укажите в комментариях версию Python и разрядность вашей ОС.

# Python 3.9   Windows 10 х 64


import sys
import random

matrix = []

for i in range(5):
    matrix.append([])
    matrix[i].extend([random.randint(1, 100) for _ in range(5)])

min_nums = []
min_nums.extend(matrix[0])

for string in matrix:
    print()
    print(('{:4d} ' * len(string)).format(*string))
    i = 0
    for j in string:
        if j < min_nums[i]:
            min_nums[i] = j
        i += 1

print()
print('Минимальные элементы столбцов матрицы:')
print(('{:4d} ' * len(min_nums)).format(*min_nums))
print()

min_nums.sort(reverse=True)
print('Максимальный элемент среди минимальных:', min_nums[0])

sum_size = 0
sum_size += sys.getsizeof(i)
sum_size += sys.getsizeof(string)
sum_size += sys.getsizeof(j)
sum_size += sys.getsizeof(matrix)
sum_size += sys.getsizeof(min_nums)

print(f'Переменные занимают {sum_size} байт')


