print("Задача 2")
# Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2,
# то во второй массив надо заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5 - если индексация начинается с нуля),
# т.к. именно в этих позициях первого массива стоят четные числа.


import random

arr = [random.randint(0, 99) for _ in range(7)]
print(f'Первый массив {arr}')
index_list = []

for i in arr:
    if i % 2 == 0:
        index_list.append(arr.index(i))

print(f'Индексы чётных чисел: {index_list}')
