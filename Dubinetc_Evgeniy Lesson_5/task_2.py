print("Задача 2")
# Решить задачу генерации нечётных чисел от 1 до n (включительно), не используя ключевое слово yield.

# задаю значение переменной
my_num = 15
# создаю генератор от 1 до 15 включительно с шагом 2
odd_nums_gen = (n for n in range(1, my_num + 1, 2))


print(next(odd_nums_gen))
print(next(odd_nums_gen))
print(next(odd_nums_gen))
