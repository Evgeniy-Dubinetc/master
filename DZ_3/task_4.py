print("Задача 4")
# Определить, какое число в массиве встречается чаще всего.


from random import random
L = 21
arr = [0] * L
for i in range(L):
    arr[i] = int(random() * 20)
print(f'Массив: {arr}')

num = arr[0]
max_frq = 1
for i in range(L - 1):
    frq = 1
    for j in range(i + 1, L):
        if arr[i] == arr[j]:
            frq += 1
    if frq > max_frq:
        max_frq = frq
        num = arr[i]

if max_frq > 1:
    print(f'Число {num}, встречается {max_frq} раз(а)')
else:
    print('Все элементы уникальны')
