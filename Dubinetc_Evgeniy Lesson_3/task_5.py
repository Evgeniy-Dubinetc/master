print("Задача 5")
# Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов,
# взятых из трёх списков (по одному из каждого):
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
# Например: >>> get_jokes(2) ["лес завтра зеленый", "город вчера веселый"]
# Документировать код функции.
# Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках
# (когда каждое слово можно использовать только в одной шутке)? Сможете ли вы сделать аргументы именованными?

# импортирую рандом и создаю три списка
import random
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

# создаю функцию с числовым аргументом n


def get_jokes(n):
    # создаю пустой список
    list_1 = []
    # циклом генерируем три переменные n раз, наполняя list_1 по одному элементу из списков
    for i in range(n):
        ran_nouns = random.choice(nouns)
        ran_adverbs = random.choice(adverbs)
        ran_adjectives = random.choice(adjectives)
        list_1.append(f'{ran_nouns} {ran_adverbs} {ran_adjectives}')
        # возвращаю список с шутками
    return list_1


# создаю функцию с числовым аргументом n и "флагом" повтора


def get_jokes_flag(n, flag=True):
    # создаю пустой список шуток
    flag_list = []
    # если flag=False
    if not flag:
        # при условии если число повторов n превышает длину одного из списков
        if n > min(len(nouns), len(adverbs), len(adjectives)):
            # возвращаем flag
            return 'flag'
        # иначе random.shuffle перемешивает списки
        else:
            random.shuffle(nouns)
            random.shuffle(adverbs)
            random.shuffle(adjectives)
            # циклом генерируем три переменные n раз, наполняя flag_list по одному элементу
            for i in range(n):
                flag_list.append(f'{nouns[i]} {adverbs[i]} {adjectives[i]}')
    # если flag=True
    else:
        # циклом генерируем три переменные n раз, наполняя flag_list по одному элементу из списков
        for i in range(n):
            ran_nouns = random.choice(nouns)
            ran_adverbs = random.choice(adverbs)
            ran_adjectives = random.choice(adjectives)
            flag_list.append(f'{ran_nouns} {ran_adverbs} {ran_adjectives}')
    # возвращаю список с шутками
    return flag_list


print(get_jokes(1))
print(get_jokes(2))
print(get_jokes(3))
print(get_jokes_flag(4, False))
print(get_jokes_flag(5, False))
print(get_jokes_flag(6, False))
print(get_jokes_flag(7, False))
