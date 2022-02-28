print("Задача 1")
# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

number = input('Введите трехзначное число: ')
product = 1
summa = 0
for f in number:
    summa += int(f)
    product *= int(f)
print(f"Сумма цифр равна: {summa}")
print(f"Произведение цифр равно: {product}")
