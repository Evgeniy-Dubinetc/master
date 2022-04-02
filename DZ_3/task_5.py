print("Задача 5")
# В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.

import random

arr = [random.randint(-9, 9) for _ in range(10)]
print(f'Массив: {arr}')

min_index = 0

for i in arr:
    if arr[min_index] > i:
        min_index = arr.index(i)

if arr[min_index] >= 0:
    print(f'В массиве нет отрицательных элементов')
else:
    print(f'Максимальный отрицательный элемент: {arr[min_index]}, находится на позиции {min_index}')
