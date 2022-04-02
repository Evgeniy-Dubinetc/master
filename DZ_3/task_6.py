print("Задача 6")
# В одномерном массиве найти сумму элементов,
# находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.


import random

arr = [random.randint(0, 21) for _ in range(10)]
print(f'Массив: {arr}')

min_num = 0
max_num = 0
step = 1
summa = 0

for i in arr:
    if arr[min_num] > i:
        min_num = arr.index(i)
    elif arr[max_num] < i:
        max_num = arr.index(i)

if max_num - min_num < 0:
    step = -1

for i in arr[min_num + step:max_num:step]:
    summa += i

print(f'Сумма элементов между минимальным и максимальным, составляет: {summa}')
