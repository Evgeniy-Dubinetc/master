print("Задача 1")
# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

number = input('Введите трехзначное число: ')
summa = 0
product = 1

for i in number:
    summa += int(i)
    product *= int(i)
print(f"Сумма цифр - {summa}")
print(f"Произведение цифр - {product}")
