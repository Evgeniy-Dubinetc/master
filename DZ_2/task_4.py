print("Задача 4")
# Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125
# ...Количество элементов (n) вводится с клавиатуры.

num = int(input("Введите количество элементов: "))
elem = 1
summa = 0

for i in range(num):
    summa += elem
    elem /= -2
print(f'Сумма элементов равна: {summa}')
