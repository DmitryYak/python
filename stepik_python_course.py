# Напишите программу, которая выводит указанный треугольник, состоящий из звездочек (*).

# put your python code here
print("*")
print("**")
print("***")
print("****")
print("*****")
print("******")
print("*******")

# print('Как тебя зовут?')
# # name = input()
# print('Привет,', name)

# На вход программе подается строка текста – имя человека. Напишите программу,
# которая выводит на экран приветствие в виде слова «Привет» (без кавычек),
# после которого должна стоять запятая и пробел, а затем введенное имя.

# print(f'Привет, {input()}')

#На вход программе подается строка текста – название футбольной команды.
#Напишите программу, которая повторяет ее на экране со словами « - чемпион!» (без кавычек).

# print(f'{input()} - чемпион!')

# Напишите программу, которая считывает три строки по очереди,
# а затем выводит их в той же последовательности, каждую на отдельной строчке.
# print(input())
# print(input())
# print(input())

# Напишите программу, которая считывает три строки по очереди,
# а затем выводит их в обратной последовательности, каждую на отдельной строчке.
# Sample Input 1:
#
# Hello
# it's
# me

# a = input()
# b = input()
# c = input()
#
# print(c)
# print(b)
# print(a)

print('a', 'b', sep='1', end='inish')
a = 8
print('c', a, 'd', sep='&', end='finish_two')

print('a', 'b', 'c', sep='*')
print('d', 'e', 'f', sep='**', end='')
print('g', 'h', 'i', sep='+', end='%')
print('j', 'k', 'l', sep='-', end='\n')
print('m', 'n', 'o', sep='/', end='!')
print('p', 'q', 'r', sep='1', end='%')
print('s', 't', 'u', sep='&', end='\n')
print('v', 'w', 'x', sep='%')
print('y', 'z', sep='/', end='!')

# Напишите программу, которая выводит на экран текст «I***like***Python» (без кавычек).

print('I', 'like', 'Python', sep='***')

print('Раз', sep='*')
print('Два', sep='*')
print('Три', sep='*')

# Напишите программу, которая считывает строку-разделитель и три строки, а затем выводит указанные строки через разделитель.
#
# Формат входных данных
# На вход программе подаётся строка-разделитель и три строки, каждая на отдельной строке.
#
# Формат выходных данных
# Программа должна вывести введённые три строки через разделитель.
#
# y = input()
# a = input()
# b = input()
# c = input()
# print(a, b, c, sep=y)

# Напишите программу, которая приветствует пользователя, выводя слово «Привет» (без кавычек),
# после которого должна стоять запятая и пробел, а затем введенное имя и восклицательный знак.
#
# Формат входных данных
# На вход программе подаётся одна строка — имя пользователя.

# print(f'Привет, {input()}!')

# Напишите программу вывода на экран трех последовательно идущих чисел,
# каждое на отдельной строке. Первое число вводит пользователь, остальные числа вычисляются в программе.

# a = int(input())
# print(a)
# print(a + 1)
# print(a + 2)

# Напишите программу, которая считывает три целых числа и выводит на экран их сумму.
# Каждое число записано в отдельной строке.

# a = int(input())
# b = int(input())
# c = int(input())
# print(a + b + c)

# Напишите программу, вычисляющую объём куба и площадь его полной поверхности, по введённому значению длины ребра.

# a = int(input())
# v = (a * a * a)
# s = (a * a * 6)
# print(f'Объем = {v}')
# print(f'Площадь полной поверхности = {s}')

# Напишите программу, которая считывает целое число,
# после чего на экран выводится следующее и предыдущее целое число с пояснительным текстом.

# a = int(input())
# last = a - 1
# next = a + 1
# print(f'Следующее за числом {a} число: {next}')
# print(f'Для числа {a} предыдущее число: {last}')

# Напишите программу, которая считает стоимость трех компьютеров,
# состоящих из монитора, системного блока, клавиатуры и мыши.
#
# mon = int(input())
# block = int(input())
# mouse = int(input())
# klava = int(input())
# sum_3 = (mon + block + mouse + klava) * 3
# print(sum_3)

# Напишите программу, в которой вычисляется сумма, разность и произведение двух целых чисел, введенных с клавиатуры.
#
# a = int(input())
# b = int(input())
# sum = a + b
# di = a - b
# mult = a * b
# print(f'{a} + {b} = {sum}')
# print(f'{a} - {b} = {di}')
# print(f'{a} * {b} = {mult}')

# Что будет выведено на экран в результате выполнения следующей программы?

a = 15 // (16 % 7)
b = 34 % a * 5 - 29 % 5 * 2
print(a + b)

print(9%7)

# На вход программе подаётся натуральное число – количество сантиметров.
# Программа должна вывести одно число – полное число метров.
#
# x = int(input())
# res_met = x //100
# print(res_met)

# n школьников делят
# �
# k мандаринов поровну, неделящийся остаток остается в корзине.
# Сколько целых мандаринов достанется каждому школьнику?
# Сколько целых мандаринов останется в корзине?
# Формат входных данных
# На вход программе подаётся два целых числа: количество школьников и количество мандаринов, каждое на отдельной строке.
#
# Формат выходных данных
# Программа должна вывести два числа: количество мандаринов, которое достанется каждому школьнику,
# и количество мандаринов, которое останется в корзине, каждое на отдельной строке.
# schoolchildren = int(input())
# mandarines = int(input())
# res_chil = mandarines // schoolchildren
# man_in_basket = mandarines % schoolchildren
# print(res_chil)
# print(man_in_basket)

# all_people = int(input())
# half = all_people // 2
# result = int(half % 2) + half
# print(result)

# Безумный титан Танос собрал все 6 камней бесконечности и намеревается уничтожить половину населения Вселенной по щелчку пальцев.
# При этом если население Вселенной является нечетным числом, то титан проявит милосердие и
# округлит количество выживших в большую сторону. Помогите Мстителям подсчитать количество выживших.
#
# Формат входных данных
# На вход дается число целое
# n – население Вселенной.
#
# all_people = int(input())
# result = (all_people + (all_people % 2)) // 2
# print(result)

# В купейном вагоне имеется
# 9 купе с четырьмя местами для пассажиров в каждом. Напишите программу,
# которая определяет номер купе, в котором находится место с
# заданным номером (нумерация мест сквозная, начинается с 1)
#На вход программе подаётся целое число – место с заданным номером в вагоне.
#
# nom = int(input()) * -1
# print((nom // 4) * -1)

# Напишите программу для пересчёта величины временного интервала, заданного в минутах,
# в величину, выраженную в часах и минутах.
#
# inp = int(input())
# hour = inp // 60
# min = inp % 60
# print(f'{inp} мин - это {hour} час {min} минут.')

# Напишите программу, в которой рассчитывается сумма и произведение цифр положительного трёхзначного числа.
# На вход программе подаётся положительное трёхзначное число.
#
# num = int(input())
# num_1 = num // 100
# num_2 = (num // 10) % 10
# num_3 = num % 10
# 
# print('Сумма цифр =', num_1 + num_2 + num_3)
# print('Произведение цифр =', num_1 * num_2 * num_3)

#Дано трехзначное число abc, в котором все цифры различны. Напишите программу, которая выводит шесть чисел, образованных при перестановке цифр заданного числа.
#Программа должна вывести шесть чисел, образованных при перестановке цифр заданного числа в следующем порядке: 
#abc,acb,bac,bca,cab,cba.
#
#i = int(input())
#a = i // 100
#b = (i // 10) % 10 
#c = i % 10
#print(f'{a}{b}{c}')
#print(f'{a}{c}{b}')
#print(f'{b}{a}{c}')
#print(f'{b}{c}{a}')
#print(f'{c}{a}{b}')
#print(f'{c}{b}{a}')

# Напишите программу для нахождения цифр четырёхзначного числа.
# На вход программе подаётся положительное четырёхзначное целое число.
# # 
# x = int(input())
# a = x //1000
# b = (x // 100) % 10
# c = (x // 10) % 10
# d = x % 10
# print(f'Цифра в позиции тысяч равна {a}')
# print(f'Цифра в позиции сотен равна {b}')
# print(f'Цифра в позиции десятков равна {c}')
# print(f'Цифра в позиции единиц равна {d}')

# При регистрации на сайтах требуется вводить пароль дважды. 
# Это сделано для безопасности, поскольку такой подход уменьшает возможность неверного ввода пароля.

# Напишите программу, которая сравнивает пароль и его подтверждение. Если они совпадают,
# то программа выводит: «Пароль принят», иначе: «Пароль не принят».
# # 
# a, b = input(), input()
# if a == b:
#     print('Пароль принят')
# else:
#     print('Пароль не принят')

# Напишите программу, которая определяет, является число четным или нечетным.
# # 
# x = int(input())
# if (x % 2) == 0:
#     print('Четное')
# else:
#     print('Нечетное')

# Напишите программу, которая проверяет, что для заданного четырехзначного числа выполняется следующее соотношение:
# сумма первой и последней цифр равна разности второй и третьей цифр.
# На вход программе подаётся одно целое положительное четырёхзначное число.
# # 
# x = int(input())
# a = x // 1000
# b = (x // 100) % 10
# c = (x // 10) % 10
# d = x % 10
# if (a + d) == (b - c):
#     print('ДА')
# else:
#     print('НЕТ')

# Роскомнадзор
# Напишите программу, которая определяет, разрешен пользователю доступ к интернет-ресурсу или нет.
# На вход программе подаётся целое число — возраст пользователя.
# # 
# age = int(input())
# if age < 18:
#     print('Доступ запрещен')
# else:
#     print("Доступ разрешен")

# Арифметическая прогрессия
# Напишите программу, которая определяет, являются ли три заданных числа (в указанном порядке) последовательными членами
# 
# a = int(input())
# b = int(input())
# c = int(input())
# if c - (b - a) == b:
#     print('YES')
# else:
#     print('NO')

# Напишите программу, которая определяет наименьшее из двух чисел.
# 
# a = int(input())
# b = int(input())
# if a < b:
#     print(a)
# else:
#     print(b)

# Напишите программу, которая определяет наименьшее из четырёх чисел.
# 
# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())

# if a <= b and a <= c and a <= d:
#     print(a)
# elif b <= a and b <= c and b <= d:
#     print(b)
# elif c <= a and c <= b and c <= d:
#     print(c)
# else:
#     print(d)

# Возрастная группа
# Напишите программу, которая по введённому возрасту пользователя сообщает, к какой возрастной группе он относится:
# до 13 включительно – детство;
# от 14 до 24 – молодость;
# от 25 до 59 – зрелость;
# от 60 – старость.
# 
# age = int(input())
# if age <= 13:
#     print('детство')
# elif age < 24:
#     print('молодость')
# elif age < 59:
#     print('зрелость')
# else:
#     print('старость')


