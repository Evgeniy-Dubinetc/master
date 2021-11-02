print("Задача 2")
# (вместо 1) Написать скрипт, создающий из config.yaml стартер для проекта со следующей структурой:
# |--my_project
#    |--settings
#    |  |--__init__.py
#    |  |--dev.py
#    |  |--prod.py
#    |--mainapp
#    |  |--__init__.py
#    |  |--models.py
#    |  |--views.py
#    |  |--templates
#    |     |--mainapp
#    |        |--base.html
#    |        |--index.html
#    |--authapp
#    |  |--__init__.py
#    |  |--models.py
#    |  |--views.py
#    |  |--templates
#    |     |--authapp
#    |        |--base.html
#    |        |--index.html
# Примечание: структуру файла config.yaml придумайте сами, его можно создать в любом текстовом редакторе «руками»
# (не программно); предусмотреть возможные исключительные ситуации, библиотеки использовать нельзя.

# pip install pyyaml

import yaml
import os
# создаю структуру проекта
d = {'my_project': [
    {'settings': ['__init__.py', 'dev.py', 'prod.py']},
    {'mainapp': ['__init__.py', 'models.py', 'views.py', {'templates': [{'mainapp': ['base.html', 'index.html']}]}]},
    {'authapp': ['__init__.py', 'models.py', 'views.py', {'templates': [{'authapp': ['base.html', 'index.html']}]}]}]}
# создаю и открываю файл на запись
f = open('config.yaml', 'w')
# записываю данные
f.write(yaml.dump(d))
# закрываю файл
f.close()

# открываю файл и записываю в него данные
with open("config.yaml") as y_file:
    d = yaml.safe_load(y_file)


def create_data(data):
    # в цикле с помощью метода словарей items получаю на выход кортежи (ключ, значение)
    for folder, data_tmps in data.items():
        # если папка с таким именем отсутствует
        if not os.path.exists(folder):
            # создаю ее
            os.mkdir(folder)
        # вносим изменения в папке
        os.chdir(folder)
        for data_tmp in data_tmps:
            # в цикле проверяю, если это словарь,
            if isinstance(data_tmp, dict):
                # то передаю его в эту функцию
                create_data(data_tmp)
            else:
                # проверяю существует ли файл
                if not os.path.exists(data_tmp):
                    if '.' in data_tmp:
                        # открываю файл и записываю в него данные
                        with open(data_tmp, 'w') as f:
                            f.write('')
    else:
        # меняю текущий каталог
        os.chdir('../')


create_data(d)
