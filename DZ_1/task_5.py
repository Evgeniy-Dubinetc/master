print("Задача 5")
# Пользователь вводит две буквы.
# Определить, на каких местах алфавита они стоят и сколько между ними находится букв.

chars = '0abcdefghigklmnopqrstuvwxyz'

char_range = input('Укажите диапазон символов от a до z через пробел: ').split(' ')

a = chars.index(char_range[0])
b = chars.index(char_range[1])
c = b - a

print('Буква {} - на {} месте, буква {} - на {} месте.\
 Количество букв между ними {}.'.format(char_range[0], a, char_range[1], b, c))
