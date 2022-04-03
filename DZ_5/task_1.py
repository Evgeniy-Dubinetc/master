print("Задача 1")
# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала
# (т.е. 4 отдельных числа) для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий) и
# вывести наименования предприятий, чья прибыль выше среднего и отдельно вывести наименования предприятий,
# чья прибыль ниже среднего.
# Примечание: для решения задачи попробуйте применить какую-нибудь коллекцию из модуля collections

import collections

company = collections.namedtuple('company', ['name', 'q1', 'q2', 'q3', 'q4', 'y'])
companys = []
q = int(input("Введити количество предприятий: "))
total = 0
for i in range(q):
    name = input(f"Название {i + 1}-ого предприятия: ")
    q1 = int(input("Прибыль за 1 квартал: "))
    q2 = int(input("Прибыль за 2 квартал: "))
    q3 = int(input("Прибыль за 3 квартал: "))
    q4 = int(input("Прибыль за 4 квартал: "))
    y = q1 + q2 + q3 + q4
    total += y
    companys.append(company(name=name, q1=q1, q2=q2, q3=q3, q4=q4, y=y))
total_avg = total / q
print(f"Предприятия с прибылью выше средней {total_avg}: ")
for company in companys:
    if company.y >= total_avg:
        print(company.name)
print(f"Предприятия с прибылью ниже средней {total_avg}: ")
for company in companys:
    if company.y < total_avg:
        print(company.name)
