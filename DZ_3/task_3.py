print("Задача 3")
# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

arr = [random.randint(0, 99) for _ in range(7)]
print(f'Массив до изменения: {arr}')

max_num = arr[0]
min_num = arr[0]

for i in arr:
    if i > max_num:
        max_num = i
    elif i < min_num:
        min_num = i
min_index = arr.index(min_num)
max_index = arr.index(max_num)
arr[min_index], arr[max_index] = arr[max_index], arr[min_index]
print(f'Массив после изменения: {arr}')
