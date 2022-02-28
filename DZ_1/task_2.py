print("Задача 2")
# Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6.
# Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака.
# Объяснить полученный результат.

num1 = 5
num2 = 6

# оператор 'И', копирует бит в результат только если бит присутствует в обоих операндах
bit_and = num1 & num2
print(f"Побитовое «И» для {bin(num1)} и {bin(num2)} : {bin(bit_and)} ({bit_and})")

# оператор 'ИЛИ' копирует бит, если он присутствует хотя бы в одном операнде
bit_or = num1 | num2
print(f"Побитовое «ИЛИ» для {bin(num1)} и {bin(num2)} : {bin(bit_or)} ({bit_or})")

# 'Исключительное ИЛИ' оператор копирует бит, если бит присутствует в одном из операндов, но не в обоих сразу
bit_ior = num1 ^ num2
print(f"Исключающее «ИЛИ» для {bin(num1)} и {bin(num2)} : {bin(bit_ior)} ({bit_ior})")

# 'Побитовое отрицание' меняет биты на обратные, там где была единица становиться ноль и наоборот
bit_not_num1 = ~num1
bit_not_num2 = ~num2
print(f"Побитовое отрицание для {bin(num1)} : {bin(bit_not_num1)} ({bit_not_num1}) и для {bin(num2)}: \
{bin(bit_not_num2)} ({bit_not_num2})")

# 'Побитовый сдвиг вправо' - значение левого операнда "сдвигается" вправо на количество бит указанных в правом операнде
bit_shift_right = num1 >> 2
print(f"Битовый сдвиг вправо для {bin(num1)} : {bin(bit_shift_right)} ({bit_shift_right})")

# 'Побитовый сдвиг влево' - значение левого операнда "сдвигается" влево на количество бит указанных в правом операнде
bit_shift_left = num1 << 2
print(f"Битовый сдвиг влево для {bin(num1)} : {bin(bit_shift_left)} ({bit_shift_left})")
