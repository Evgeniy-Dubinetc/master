print("Задача 3")
# Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками» в проводнике).
# Написать скрипт, который собирает все шаблоны в одну папку templates, например:
# |--my_project
#    ...
#   |--templates
#    |   |--mainapp
#    |   |  |--base.html
#    |   |  |--index.html
#    |   |--authapp
#    |      |--base.html
#    |      |--index.html
# Примечание: исходные файлы необходимо оставить; обратите внимание, что html-файлы расположены в родительских папках
# (они играют роль пространств имён); предусмотреть возможные исключительные ситуации; это реальная задача,
# которая решена, например, во фреймворке django.

import os
import shutil
# создаю папку my_dir, если папки с таким именем не имеется
my_dir = 'task3'  # save folder
if not os.path.exists(my_dir):
    os.mkdir(my_dir)

folder = r'my_project'  # search folder
# создаю пустой список
files = []

# генерирую имена файлов в виде тройных кортежей
for r, d, f in os.walk(folder):
    for file in f:
        # если в названии имеется .html
        if '.html' in file:
            # создаю конкатенацию пути к файлу
            files.append(os.path.join(r, file))
for path in files:
    # создаю конкатенацию пути к файлу
    folder = os.path.join(my_dir, os.path.basename(os.path.dirname(path)))
    # создаю папку, если папки с таким именем не имеется
    if not os.path.exists(folder):
        os.mkdir(folder)
    save_path = os.path.join(folder, os.path.basename(path))
    shutil.copy(path, save_path)
