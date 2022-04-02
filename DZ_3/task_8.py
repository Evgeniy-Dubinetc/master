print("Задача 8")
# Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.

matrix = []

for i in range(4):
    matrix.append([])
    summa = 0
    for j in range(4):
        user_number = int(input(f'Введите {i + 1} элемент {j + 1} столбца: '))
        summa += user_number
        matrix[i].append(user_number)

    matrix[i].append(summa)

for a in matrix:
    print(('{:>4d}' * 5).format(*a))
