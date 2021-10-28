print("Задача 5")
# (вместо 4) Решить задачу 4 и реализовать интерфейс командной строки,
# чтобы можно было задать путь к обоим исходным файлам и путь к выходному файлу со словарём.
# Проверить работу скрипта для случая, когда все файлы находятся в разных папках.


import sys
from itertools import zip_longest
# пользователей, хобби и выходной файл беру из системного окружения
# (sys.argv - заводит как переменную то, что передали в файл)
users, hobby, out = sys.argv[1:]
# открываю выходной файл и файлы с пользователями и хобби
with open(out, 'w', encoding='utf-8') as f:
    with open(users, encoding='utf-8') as users:
        with open(hobby, encoding='utf-8') as hobby:
            # создаю генератор, где каждой линии присваивается 1, и спомощью функции sum они складываются
            num_lines_users = sum(1 for line in users)
            num_lines_hobby = sum(1 for line in hobby)

            # проверяю, если количество линий пользователей меньше кол-ва линий хобби, выходим из скрипта с кодом «1»
            if num_lines_users < num_lines_hobby:
                exit(1)

            # курсор (каретку) возвращаю в начало файлов (после генератора каретка остается в конце файла)
            users.seek(0)
            hobby.seek(0)
        # проходим по файлам с помощью zip_longest, наполняя line_user - ФИО пользователей, и line_user_hobby - хобби
        # если в файле, хранящем данные о хобби, меньше записей, чем в файле с пользователями, zip_longest вернет None.
            for line_user, line_user_hobby in zip_longest(users, hobby):
                # записываю строку с пользователем и хобби (strip уберет системные символы), если хобби не имеет
                # значение None, записываю line_user_hobby
                f.write(f'{line_user.strip()}: '
                        f'{line_user_hobby.strip() if line_user_hobby is not None else line_user_hobby}\n')

# пример запуска скрипта >>>
# (передаем путь до файлов с пользователями, хобби, и название файла - куда выводить результат)
# python homework.py "users.csv" "hobby.csv" "task5.txt"
