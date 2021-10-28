print("Задача 4")
# (вместо 3) Решить задачу 3 для ситуации, когда объём данных в файлах превышает объём ОЗУ
# (разумеется, не нужно реально создавать такие большие файлы, это просто задел на будущее проекта).
# Также реализовать парсинг данных из файлов — получить отдельно фамилию, имя и отчество для пользователей
# и название каждого хобби: преобразовать в какой-нибудь контейнерный тип (список, кортеж, множество, словарь).
# Обосновать выбор типа. Подумать, какие могут возникнуть проблемы при парсинге.
# В словаре должны храниться данные, полученные в результате парсинга.

# импортирую из модуля itertools - zip_longest
from itertools import zip_longest
# открываю файлы с пользователями и хобби
with open('task4.txt', 'w', encoding='utf-8') as f:
    with open('users.csv', encoding='utf-8') as users:
        with open('hobby.csv', encoding='utf-8') as hobby:
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
