print("Задача 2")
# Доработать предыдущую функцию в num_translate_adv(): реализовать корректную работу с числительными,
# начинающимися с заглавной буквы — результат тоже должен быть с заглавной.
# Например: >>> num_translate_adv("One") "Один"   >>> num_translate_adv("two")  "два"

# создаю словарь снаружи функции
numbers_dict = {
    'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять',
    'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'
}
# запрашиваю у пользователя число
my_number = input('Введите число от 1 до 10 на английском языке: ')

# создаю функцию использования словаря, в которой при помощи get вернется None при некорректном вводе числа


def num_translate(number):
    # если первый знак строки заглавный, переводим всю строку в нижний регистр и первый знак делаем заглавным
    if number[0] == number[0].upper():
        number = number.lower()
        return numbers_dict.get(number).capitalize()
    else:
        return numbers_dict.get(number)


print(num_translate(my_number))
