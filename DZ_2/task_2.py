print("Задача 2")
# Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

num = input('Введите натуральное число: ')

even = 0
odd = 0
even_list = []
odd_list = []
for n in num:
    i = int(n)
    if i % 2 == 0:
        even += 1
        even_list += [i]
    else:
        odd += 1
        odd_list += [i]
print(f'У числа {num}: четных цифр - {even} {even_list} и нечетных - {odd} {odd_list} ')
