print("Задача 7")
# В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

import random

arr = [random.randint(0, 21) for _ in range(10)]
print(f'Массив: {arr}')

min_num = 0
min_num2 = 1

for i in arr:
    if arr[min_num] > i:
        min_num2 = min_num
        min_num = arr.index(i)
    elif arr[min_num2] > i:
        min_num2 = arr.index(i)

print(f'Два наименьших элемента: {arr[min_num]} и {arr[min_num2]}')
