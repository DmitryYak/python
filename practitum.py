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