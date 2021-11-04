print("Задача 1")
# Написать функцию email_parse(<email_address>), которая при помощи регулярного выражения извлекает
# имя пользователя и почтовый домен из email адреса и возвращает их в виде словаря.
# Если адрес не валиден, выбросить исключение ValueError.
# Пример:
# >>> email_parse('someone@geekbrains.ru')
# {'username': 'someone', 'domain': 'geekbrains.ru'}
# >>> email_parse('someone@geekbrainsru')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# raise ValueError(msg)
# ValueError: wrong email: someone@geekbrainsru
# Примечание: подумайте о возможных ошибках в адресе и постарайтесь учесть их в регулярном выражении;
# имеет ли смысл в данном случае использовать функцию re.compile()?


# импортирую библиотеку
import re
# создаю регулярное выражение с помощью re.compile, в котором две группы с неограниченным количеством букв на англ.
# языке и цифр, далее точка (\.) и группа с неограниченным количеством букв на англ. языке
EMAIL = re.compile(r'([a-z0-9]+)@([a-z0-9]+\.[a-z]+)')


# создаю функцию, которая принимает email
def email_parse(email):
    # с помощью findall получаю нулевой элемент
    found_info = EMAIL.findall(email)[0]
    if found_info:
        # если нашлось совпадение c (r'([a-z0-9]+)@([a-z0-9]+\.[a-z]+)'), получаю имя и адрес
        name, address = found_info
    else:
        # иначе вывожу ошибку, что email не корректный
        raise ValueError(f'wrong email: {email}')
    # возвращаю имя и адрес
    return name, address


print(email_parse('someone@geekbrains.ru'))
print(email_parse('someone@geekbrainsru'))
