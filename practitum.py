# bremen_musicians = ['Кот', 'Пёс', 'Трубадур', 'Осёл', 'Петух']
# # Код цикла
# for musician in bremen_musicians:
#     # Каждый элемент списка bremen_musicians
#     # по очереди будет передан в переменную musician
#     # и напечатан
#     print(musician)
#
# # Код, который выполняется после цикла
# print('Нам дворцов заманчивые своды не заменят никогда свободы!')
#
# song = { 'one', 'two', 'three', 'two'}
#
# print(type(song))
#
# print (song)
#
# mass = ['one', 'two', 'three', 'two', 'one', 'five', 'six']
#
# print(mass[2])
#
# set_mass = set(mass)
#
# print(set_mass)
# mass_two = {'one', 'two', 'three', 'two', 'one', 'five', 'six'}
# for i in mass_two:
#     print(i)
#
# print('hello')
#
# playlist = {
#     'Venus',
#     'Yesterday',
#     'Fireball',
#     'Time',
#     'Poison'
# }
# playlist.add('tommorow')
#
# print(playlist)
#
# playlist_1 = {'Три белых коня', 'Happy new year', 'Снежинка'}
# playlist_2 = {'Last christmas', 'Снежинка', 'Happy new year'}
# playlist_3 = playlist_1.union(playlist_2)
#
# print(playlist_3)
#
import datetime

english = {
    'рука': 'arm',
    'нога': 'leg',
    'хвост': 'tail',
    'питон': 'python',
    'бэкенд-разработчик': 'back-end developer'
}
# english['голова'] = 'head'
#
# print(english)
#
# bremen_musicians = ['Кот', 'Пёс', 'Трубадур', 'Осёл', 'Петух']
#
# for musician in bremen_musicians:
#     print(musician)

# for key, value in english.items():
#     print(key, '+', value)

favorite_songs = {
    'Тополиный пух': 'Иванушки international',
    'Город золотой': 'Аквариум',
    'Звезда по имени Солнце': 'Кино',
    'Space Oddity': 'David Bowie',
    'Рыба': 'Аквариум',
    'Серенада Трубадура': 'Муслим Магомаев',
}

# for i in favorite_songs.values():
#     print(i)
#
# for i in favorite_songs.keys():
#     print(i)

# for i, b in favorite_songs.items():
#     print(i, b)

friends =  {
    'Серёга': 'Омск',
    'Соня': 'Москва',
    'Дима': 'Челябинск',
    'Айгуль': 'Казань',
    'Алёна': 'Белгород',
    'Даниил': 'Санкт-Петербург',
    'Лев': 'Тула',
    'Валера': 'Сыктывкар',
    'Антон': 'Ялта',
    'Карен': 'Краснодар'
}

for i , b in friends.items():
    print(i,"live in", b)

friends_dict = {
    "one": "Kostya",
    "two": True
}

friends_list = [
    'Kostya',
    'Den',
    True
]

friends_set = {
    'Kostya',
    'Luntik',
    'Mila',
    False
}
if 'Kostya' in friends_dict:
    print('yes')

if True in friends_list:
    print(friends_list[2])


sleep_list = [
    'спать',
    'дрыхнуть',
    'кемарить',
    'спать',
    'drink'
]

sleep_list.append("new word")

print(sleep_list)

if "drink" not in sleep_list:
    print("great")
else:
    print("give me a glass")

sleep_list.append("new value")
print(sleep_list)

some_set = {
    'one',
    'two',
    True
}
print(some_set)
some_set.add(False)
print(some_set)

playlist = {
    'Venus',
    'Yesterday',
    'Fireball',
    'Time',
    'Poison',
    'Thunderstruck'
}
new_music = [
    'Kashmir',
    'Smoke on the Water',
    'Bohemian Rhapsody',
    'Zombie',
    'Let It Be',
    'Its My Life',
]
for i in new_music:
    if i not in playlist:
        playlist.add(i)
    # Здесь ваш код

print(playlist)

new_music.append(('nose mc'))
print(new_music)

playlist.add('nose mc')
print(playlist)

for i in new_music:
    print(i)
    if 'nose mc' in new_music:
        print('nose has in this playlst')

friends = {
    'Серёга': 'Омск',
    'Соня': 'Москва',
    'Дима': 'Челябинск',
    'Алина': 'Хабаровск',
    'Егор': 'Пермь'
}


def is_anyone_in(collection, city):
    for friend in friends:
        if not collection[friend] == city:
            print('В городе', collection[friend], 'у меня есть друг, но мне туда не надо.')
        else:
            print('В городе', collection[friend], ' живёт '+ friend + '. Обязательно зайду в гости!')


is_anyone_in(friends, 'Хабаровск')

print(friends["Серёга"])


my_collegue = {
    'Alex': 'python',
    'Dima': 'JS',
    'Alex Nik': 'devops',
    'Tatiana': 'accountant',
    'Vitalik': True
}

def who_is(who, position):
    for i in who:
        if who[i] == position:
            print(i, 'helps me to study', who[i])

who_is(my_collegue, 'python')

def count_coll(how, friends):
    if how == "how many friends":
        print(len(friends))

count_coll("how many friends", my_collegue)

DATABASE = {
    'Серёга': 'Омск',
    'Соня': 'Москва',
    'Миша': 'Москва',
    'Дима': 'Челябинск',
    'Алина': 'Красноярск',
    'Егор': 'Пермь',
    'Коля': 'Красноярск'
}

def process_anfisa(query):
    if query == 'Сколько у меня друзей?':
        count = len(DATABASE)
        return 'У тебя ' + str(count) + ' друзей.'
    # Здесь проверьте, что переменная query равна строке 'Кто все мои друзья?'
    elif query == 'Кто все мои друзья?':
        friends_string = ''
        # Чтобы получить перечень друзей -
        # переберите словарь DATABASE в цикле
        for i in DATABASE:
            friends_string += i + " "     # Добавляйте к переменной friends_string имя друга и пробел
        # Верните строку, составленную из 'Твои друзья: ' и friends_string
        return'Твои друзья: '+  friends_string
    elif query == 'Где все мои друзья?':
        for city in DATABASE.value():
            print(city)
    else:
        return '<неизвестный запрос>'

# Не изменяйте следующий код
print('Привет, я Анфиса!')
print(process_anfisa('Сколько у меня друзей?'))
print(process_anfisa('Кто все мои друзья?'))
# print(process_anfisa('Где все мои друзья?'))

print(DATABASE.values())

string = 'what are you doing'

print(string)
list_from_string = list(string)

print('list:',  list_from_string)

set_from_string = set(string)
print('set', str(set_from_string))

print(string.split('d'))

monument_string = 'Я памятник себе воздвиг нерукотворный'

index_list = [0, 1, 2, 8, 6, 17, 24]

for i in index_list:
    # На каждой итерации цикла
    # берём из строки monument_string элемент с индексом i и печатаем полученную букву
    print(monument_string[i])


some_string = 'good morning'

short_str = [1, 2, 5, -5]

for l in short_str:
    print(some_string[l])

milk = 'molokovoz'

new_milk = milk.split('o')
print(new_milk)

counter_str = 'Раз-два-  три-четыре-пять,  вышел  зайчик погулять'

new_counter = counter_str.split(' ')
print(new_counter)

word_list_count = counter_str.split()
print(word_list_count)

new_join = ' '.join(word_list_count)
print(new_join)

def check_query(query):
# Допишите код тела функции
    elements  = query.split(', ')
    if elements[0] == 'Анфиса':
        return 'запрос к Анфисе'
    else:
        return 'запрос к кому-то ещё'




# Дальше следует код, вызывающий вашу функцию; не изменяйте его:
queries = [
    'Анфиса, сколько у меня друзей?',
    'Андрей, ну где ты был?',
    'Андрей, ну обними меня скорей!',
    'Анфиса, кто все мои друзья?'
]

# Напечатаем результат.
# Переберём список вопросов в цикле
for q in queries:
    # Каждый из вопросов передадим аргументом
    # в функцию check_query()
    result = check_query(q)
    # И для каждого вызова напечатаем вопрос и, через дефис - вердикт программы
    print(q, '-', result)

DATABASE = {
    'Серёга': 'Омск',
    'Соня': 'Москва',
    'Миша': 'Москва',
    'Дима': 'Челябинск',
    'Алина': 'Красноярск',
    'Егор': 'Пермь',
    'Коля': 'Красноярск'
}


def process_anfisa(query):
    if query == 'Сколько у меня друзей?':
        count = len(DATABASE)

        return 'У тебя ' + str(count) + ' друзей.'
    elif query == 'Кто все мои друзья?':
        # Из словаря DATABASE создайте строку с помощью join();
        # имена друзей разделите запятой и пробелом.
        # Запишите эту строку в переменную friends_string (вместо пустых кавычек).
        friends_string = ', '.join(DATABASE)

        # Этот цикл больше не понадобится, удалите его

        return 'Твои друзья: ' + friends_string
    elif query == 'Где все мои друзья?':
        unique_cities = set(DATABASE.values())
        # Из сета unique_cities создайте строку с помощью join();
        # названия городов разделите запятой и пробелом.
        # Запишите эту строку в переменную cities_string (вместо пустых кавычек).
        cities_string = ', '.join(unique_cities)

        # Этот цикл больше не понадобится, удалите его

        return 'Твои друзья в городах: ' + cities_string
    else:
        return '<неизвестный запрос>'


print('Привет, я Анфиса!')
print(process_anfisa('Сколько у меня друзей?'))
print(process_anfisa('Кто все мои друзья?'))
print(process_anfisa('Где все мои друзья?'))

numbers_2 = [123, 132, 2342, 21]
print(type(numbers_2))

def calc_stat(listened):  # От англ. calculate statistics, посчитать статистику
    # Напишите код функции calc_stat()
    summer = 0
    for i in listened:
        summer += i
    return f'Вы прослушали {len(listened)} песен общей продолжительностью {int(summer / 60)} минут.'

print(calc_stat([189, 148, 210, 144, 174, 158, 163, 189, 227, 198]))


DATABASE = {
    'Серёга': 'Омск',
    'Соня': 'Москва',
    'Миша': 'Москва',
    'Дима': 'Челябинск',
    'Алина': 'Красноярск',
    'Егор': 'Пермь',
    'Коля': 'Красноярск'
}

def process_anfisa(query):
    if query == 'Сколько у меня друзей?':
        count = len(DATABASE)
        # В следующей строке замените конкатенацию на f-строку
        return 'У тебя ' + str(count) + ' друзей.'
    elif query == 'Кто все мои друзья?':
        friends_string = ', '.join(DATABASE)
        # В следующей строке замените конкатенацию на f-строку
        return 'Твои друзья: ' + friends_string
    elif query == 'Где все мои друзья?':
        unique_cities = set(DATABASE.values())
        cities_string = ', '.join(unique_cities)
        # В следующей строке замените конкатенацию на f-строку
        return 'Твои друзья в городах: ' + cities_string
    else:
        return '<неизвестный запрос>'


print('Привет, я Анфиса!')
print(process_anfisa('Сколько у меня друзей?'))
print(process_anfisa('Кто все мои друзья?'))
print(process_anfisa('Где все мои друзья?'))

DATABASE = {
    'Серёга': 'Омск',
    'Соня': 'Москва',
    'Миша': 'Москва',
    'Дима': 'Челябинск',
    'Алина': 'Красноярск',
    'Егор': 'Пермь',
    'Коля': 'Красноярск'
}

def process_anfisa(query):
    if query == 'Сколько у меня друзей?':
        count = len(DATABASE)
        # В следующей строке замените конкатенацию на f-строку
        return f'У тебя {str(count)} друзей.'
    elif query == 'Кто все мои друзья?':
        friends_string = ', '.join(DATABASE)
        # В следующей строке замените конкатенацию на f-строку
        return f'Твои друзья: {friends_string}'
    elif query == 'Где все мои друзья?':
        unique_cities = set(DATABASE.values())
        cities_string = ', '.join(unique_cities)
        # В следующей строке замените конкатенацию на f-строку
        return f'Твои друзья в городах: {cities_string}'
    else:
        return '<неизвестный запрос>'


print('Привет, я Анфиса!')
print(process_anfisa('Сколько у меня друзей?'))
print(process_anfisa('Кто все мои друзья?'))
print(process_anfisa('Где все мои друзья?'))

DATABASE = {
    'Серёга': 'Омск',
    'Соня': 'Москва',
    'Миша': 'Москва',
    'Дима': 'Челябинск',
    'Алина': 'Красноярск',
    'Егор': 'Пермь',
    'Коля': 'Красноярск'
}


# Новая функция, она возвращает правильное словосочетание, склоняя слово "друзья"
# в зависимости от того, какое число передано в аргументе friends_count
def process_query(query):
    twice_el = query.split(', ')
    if twice_el[0] == 'Анфиса':
        return process_anfisa(twice_el[1])
    else:
        return process_friend(twice_el[0], twice_el[1])


def process_friend(name, query):
    if name in DATABASE:
        # for i in DATABASE.keys():
        # if i == name:
        if query == 'ты где?':
            city = DATABASE[name]
            return f'{name} в городе {city}'
        else:
            return '<неизвестный запрос>'

    else:
        return f'У тебя нет друга по имени {name}'


def format_friends_count(friends_count):
    if friends_count == 1:
        return '1 друг'
    elif 2 <= friends_count <= 4:
        return f'{friends_count} друга'
    else:
        return f'{friends_count} друзей'


def process_anfisa(query):
    if query == 'сколько у меня друзей?':
        count = len(DATABASE)
        # Вызовите функцию format_friends_count() и передайте в неё count.
        # Отредактируйте строку ниже: в ней должно использоваться выражение,
        # которое вернёт функция format_friends_count()
        return f'У тебя {format_friends_count(count)}.'
    elif query == 'кто все мои друзья?':
        friends_string = ', '.join(DATABASE)
        return f'Твои друзья: {friends_string}'
    elif query == 'где все мои друзья?':
        unique_cities = set(DATABASE.values())
        cities_string = ', '.join(unique_cities)
        return f'Твои друзья в городах: {cities_string}'
    else:
        return '<неизвестный запрос>'


print('Привет, я Анфиса!')
print(process_query('Анфиса, сколько у меня друзей?'))
print(process_query('Анфиса, кто все мои друзья?'))
print(process_query('Анфиса, где все мои друзья?'))
print(process_query('Анфиса, кто виноват?'))
print(process_query('Соня, ты где?'))
print(process_query('Коля, что делать?'))
print(process_query('Антон, ты где?'))


# Подключите библиотеку random и дайте ей краткое имя
import random as r
answers = ['Норм.', 'Лучше всех :)', 'Ну так', 'Отличненько!', 'Ничего, жить буду']

def how_are_you():
    return r.choice(answers)

import datetime as dt

tommorow_morning = dt.datetime(2023,4,25)
print(tommorow_morning)

my_time = datetime.datetime.utcnow()
period = datetime.timedelta(hours=3)
moscow_time = my_time + period
print(moscow_time)


import datetime as dt

UTC_OFFSET = {
    'Санкт-Петербург': 3,
    'Москва': 3,
    'Самара': 4,
    'Новосибирск': 7,
    'Екатеринбург': 5,
    'Нижний Новгород': 3,
    'Казань': 3,
    'Челябинск': 5,
    'Омск': 6,
    'Ростов-на-Дону': 3,
    'Уфа': 5,
    'Красноярск': 7,
    'Пермь': 5,
    'Воронеж': 3,
    'Волгоград': 3,
    'Краснодар': 3,
    'Калининград': 2
}
def what_time(city):
    if city in UTC_OFFSET:
        time_now = dt.datetime.utcnow()
        return time_now + dt.timedelta(hours = UTC_OFFSET[city])
    # Напишите код тела функции;
    # она должна вернуть текущее время в городе city

print(what_time('Екатеринбург'))

import datetime as dt

DATABASE = {
    'Серёга': 'Омск',
    'Соня': 'Москва',
    'Дима': 'Челябинск',
    'Алина': 'Красноярск',
    'Егор': 'Пермь'
}

UTC_OFFSET = {
    'Санкт-Петербург': 3,
    'Москва': 3,
    'Самара': 4,
    'Новосибирск': 7,
    'Екатеринбург': 5,
    'Нижний Новгород': 3,
    'Казань': 3,
    'Челябинск': 5,
    'Омск': 6,
    'Ростов-на-Дону': 3,
    'Уфа': 5,
    'Красноярск': 7,
    'Пермь': 5,
    'Воронеж': 3,
    'Волгоград': 3,
    'Краснодар': 3,
    'Калининград': 2
}

def what_time(friend):
    if friend in DATABASE:
        my_friend = DATABASE[friend]
        time_utc = dt.datetime.utcnow()
        return time_utc + dt.timedelta(hours = UTC_OFFSET[my_friend])
    # напишите код тела функции
    # пусть она вернет время у друга из аргумента friend


    #1. Сделайте так, чтобы функция what_time() возвращала время в формате часы:минуты.

import datetime as dt


DATABASE = {
    'Серёга': 'Омск',
    'Соня': 'Москва',
    'Дима': 'Челябинск',
    'Алина': 'Красноярск',
    'Егор': 'Пермь'
}

UTC_OFFSET = {
    'Санкт-Петербург': 3,
    'Москва': 3,
    'Самара': 4,
    'Новосибирск': 7,
    'Екатеринбург': 5,
    'Нижний Новгород': 3,
    'Казань': 3,
    'Челябинск': 5,
    'Омск': 6,
    'Ростов-на-Дону': 3,
    'Уфа': 5,
    'Красноярск': 7,
    'Пермь': 5,
    'Воронеж': 3,
    'Волгоград': 4,
    'Краснодар': 3,
    'Калининград': 2
}


def what_time(friend):
    utc_time = dt.datetime.utcnow()
    city = DATABASE[friend]
    result = utc_time + dt.timedelta(hours =UTC_OFFSET[city])
    return result.strftime('%H:%M')
    #return utc_time + dt.timedelta(hours =UTC_OFFSET[city])


print(what_time('Соня'))



#2. Примените все полученные в этой теме знания, чтобы научить Анфису отвечать на вопросы про друзей, сколько у них сейчас времени:
#Артём, который час?
#Антон, который час?

import datetime as dt

DATABASE = {
    'Сергей': 'Омск',
    'Соня': 'Москва',
    'Алексей': 'Калининград',
    'Миша': 'Москва',
    'Дима': 'Челябинск',
    'Алина': 'Красноярск',
    'Егор': 'Пермь',
    'Коля': 'Красноярск',
    'Артём': 'Владивосток',
    'Петя': 'Михайловка'
}

UTC_OFFSET = {
    'Москва': 3,
    'Санкт-Петербург': 3,
    'Новосибирск': 7,
    'Екатеринбург': 5,
    'Нижний Новгород': 3,
    'Казань': 3,
    'Челябинск': 5,
    'Омск': 6,
    'Самара': 4,
    'Ростов-на-Дону': 3,
    'Уфа': 5,
    'Красноярск': 7,
    'Воронеж': 3,
    'Пермь': 5,
    'Волгоград': 3,
    'Краснодар': 3,
    'Калининград': 2,
    'Владивосток': 10
}


def format_count_friends(count_friends):
    if count_friends == 1:
        return '1 друг'
    elif 2 <= count_friends <= 4:
        return f'{count_friends} друга'
    else:
        return f'{count_friends} друзей'


def what_time(city):
    offset = UTC_OFFSET[city]
    city_time = dt.datetime.utcnow() + dt.timedelta(hours=offset)
    f_time = city_time.strftime("%H:%M")
    return f_time


def process_anfisa(query):
    if query == 'сколько у меня друзей?':
        count = len(DATABASE)
        return f'У тебя {format_count_friends(count)}.'
    elif query == 'кто все мои друзья?':
        friends_string = ', '.join(DATABASE)
        return f'Твои друзья: {friends_string}'
    elif query == 'где все мои друзья?':
        unique_cities = set(DATABASE.values())
        cities_string = ', '.join(unique_cities)
        return f'Твои друзья в городах: {cities_string}'
    else:
        return '<неизвестный запрос>'


def process_friend(name, query):
    if name in DATABASE:
        city = DATABASE[name]
        if query == 'ты где?':
            return f'{name} в городе {city}'
        elif query == 'который час?':
            if city in UTC_OFFSET:
                # if cities == city:
                return f'Там сейчас {what_time(city)}'
            else:
                return f'<не могу определить время в городе {city}>'



        else:
            return '<неизвестный запрос>'
    else:
        return f'У тебя нет друга по имени {name}'


def process_query(query):
    elements = query.split(', ')
    if elements[0] == 'Анфиса':
        return process_anfisa(elements[1])
    else:
        return process_friend(elements[0], elements[1])


def runner():
    queries = [
        'Анфиса, сколько у меня друзей?',
        'Анфиса, кто все мои друзья?',
        'Анфиса, где все мои друзья?',
        'Анфиса, кто виноват?',
        'Коля, ты где?',
        'Соня, что делать?',
        'Антон, ты где?',
        'Алексей, который час?',
        'Артём, который час?',
        'Антон, который час?',
        'Петя, который час?'
    ]
    for query in queries:
        print(query, '-', process_query(query))


runner()

#У вас есть запрос «как стать бэкенд-разработчиком». Соберите URL страницы, на которой Яндекс покажет результаты поиска по этому запросу.

user_query = 'как стать бэкенд-разработчиком'

url = 'https://yandex.ru/search/?text='
new = user_query.split(' ')
new_string = '%20'.join(new)
# ваш код здесь
print(url+new_string)