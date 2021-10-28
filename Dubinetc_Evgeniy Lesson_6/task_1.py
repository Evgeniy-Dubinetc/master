print("Задача 1")
# Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов web-сервера nginx_logs.txt
# (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs) —
# получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>). Например:
# [
# ('141.138.90.60', 'GET', '/downloads/product_2'),
# ('141.138.90.60', 'GET', '/downloads/product_2'),
# ('173.255.199.22', 'GET', '/downloads/product_2'),
# ]
# Примечание: код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.

# открываю файл
with open('nginx_logs.txt') as f:
    # создаю пустой список
    data = []
    # проходим по строкам в файле
    for line in f:
        # каждую строку делю по робелам
        split_line = line.split()
        # наполняю список первым элементом строки из файла, шестым элементом (убираю кавычки), и седьмым
        data.append((split_line[0], split_line[5].replace('"', ''), split_line[6]))

print(data)
