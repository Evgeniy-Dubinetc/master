print("Задача 9")
# Найти максимальный элемент среди минимальных элементов столбцов матрицы.

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
