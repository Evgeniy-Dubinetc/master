print("Задача 1")
# Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
# Числа и знак операции вводятся пользователем.
# После выполнения вычисления программа не должна завершаться, а должна запрашивать новые данные для вычислений.
# Завершение программы должно выполняться при вводе символа '0' в качестве знака операции.
# Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'),
# то программа должна сообщать ему об ошибке и снова запрашивать знак операции.
# Также сообщать пользователю о невозможности деления на ноль, если он ввел 0 в качестве делителя.


while True:
    try:
        num_1, operand, num_2 = [
                i for i in
                input('Введите математическое выражение через пробел (число операнд число): ').split()
                ]
    except ValueError:
        print('Неправильный ввод.')
        continue

    num_1 = int(num_1)
    num_2 = int(num_2)

    if operand == '0':
        break
    elif operand == '+':
        print(f'{num_1} {operand} {num_2} = {num_1 + num_2}')
    elif operand == '-':
        print(f'{num_1} {operand} {num_2} = {num_1 - num_2}')
    elif operand == '*':
        print(f'{num_1} {operand} {num_2} = {num_1 * num_2}')
    elif operand == '/':
        if num_2 == 0:
            print('Делить на ноль нельзя')
        else:
            print(f'{num_1} {operand} {num_2} = {num_1 / num_2}')
