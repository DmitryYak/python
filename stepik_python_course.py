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

# Напишите программу, которая считывает три числа и подсчитывает сумму только положительных чисел.
# 
# a = int(input())
# b = int(input())
# c = int(input())

# if a > 0 and b > 0 and c > 0:
#     print(a + b + c)
# elif a > 0 and c > 0:
#     print(a + c)
# elif a > 0 and b > 0:
#     print(a + b)
# elif b > 0 and c > 0:
#     print(b + c)
# elif a > 0 and b < 0 and c < 0:
#     print(a)
# elif a < 0 and b > 0 and c < 0:
#     print(b)   
# elif a < 0 and b < 0 and c > 0:
#     print(c) 
# elif a < 0 and b < 0 and c > 0:
#     print(c)      
# elif a < 0 and b > 0 and c < 0:
#     print(b)
# else:
#     print('0')

# Напишите программу, которая принимает целое число 
# x и определяет, принадлежит ли данное число указанному промежутку. 
# # 
# x = int(input())
# if x > -1 and x < 17:
#     print('Принадлежит')
# else:
#     print('Не принадлежит')

# Назовем число красивым, если оно является четырехзначным и делится нацело на 
# 7 или на 17. Напишите программу, определяющую, является ли введённое число красивым.
# Программа должна вывести «YES», если число является красивым, или «NO» в противном случае.
# 
# x = int(input())
# if ((x % 7) == 0 or (x % 17) == 0) and (x > 999 and x < 10000):
#     print('YES')
# else:
#     print('NO')
# 
# Неравенство треугольника
# Напишите программу, которая принимает три положительных числа и определяет,
# существует ли невырожденный треугольник с такими сторонами.
# 
# a, b, c = int(input()), int(input()), int(input())
# if (b + c) > a and (a + c) > b and (a + b) > c:
#     print('YES')
# else:
#     print('NO')

# # Високосный год
# Напишите программу, которая определяет, является ли год с данным номером високосным. 
# Если год является високосным, то выведите «YES», иначе выведите «NO».
# Год является високосным, если его номер кратен 4, но не кратен 100, или если он кратен 400.
# 
# year = int(input())
# if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
# #and year % 400 == 0:
#     print('YES')
# else:
#     print('NO')

# # Ход ладьи
# Даны две различные клетки шахматной доски. Напишите программу, которая определяет, 
# может ли ладья попасть с первой клетки на вторую одним ходом. Программа получает на вход четыре числа от 1 до 8 каждое,
# задающие номер столбца и номер строки сначала для первой клетки, потом для второй клетки. Программа должна вывести «YES», 
# если из первой клетки ходом ладьи можно попасть во вторую, или «NO» в противном случае.
# 
# # a = int(input())
# a1 = int(input())
# b = int(input())
# b1 = int(input())
# if ((b % a == 0) or (b1 % a1 ==0)) and (a == b or a1 == b1) :
#     print('YES')
# else:
#     print('NO')

# # Ход короля 🌶️
# Даны две различные клетки шахматной доски. Напишите программу,  которая определяет, может ли король попасть с первой клетки на вторую одним ходом.
# Программа получает на вход четыре числа от 1 до 8 каждое, задающие номер столбца и номер строки сначала для первой клетки,
# потом для второй клетки. Программа должна вывести «YES», если из первой клетки ходом короля можно попасть во вторую,
# или «NO» в противном случае.
# 
# a1 = int(input())
# b1 = int(input())
# a2 = int(input())
# b2 = int(input())
# if (a2 == (a1 + 1) or a2 == (a1 - 1) or a2 == a1) and (b2 == (b1 + 1) or b2 == (b1 - 1) or b2 == b1):
#     print('YES')
# else:
#     print('NO')

# Гонка спидстеров
# Зум бросил вызов Флэшу и предложил ему честный поединок в виде гонки вокруг магнетара.
# В случае проигрыша эта нейтронная звезда зарядится и уничтожит мир,
# поэтому Флэш решил не рисковать без причины, и узнать у своего друга Циско Рамона есть ли смысл принимать вызов.
# Циско получил данные, что скорость Зума равна 
# n, а скорость Флэша равна k.
# Напишите программу, которая должна вывести ответ Циско на вопрос Флэша.
# # 
# n = int(input())
# k = int(input())
# if n > k:
#     print('NO')
# elif k > n:
#     print('YES')
# else:
#     print("Don't know")

# Вид треугольника
# Напишите программу, которая принимает три положительных числа и определяет вид треугольника, длины сторон которого равны введенным числам.
# Формат входных данных
# На вход программе подаются три числа – длины сторон существующего треугольника.
# 
# a = int(input())
# b = int(input())
# c = int(input())
# if a == b and a == c and b == c:
#     print('Равносторонний')
# elif a == b or a == c or b == c:
#     print('Равнобедренный')
# else:
#     print('Разносторонний')

# Среднее число
# Даны три различных целых числа. Напишите программу, которая находит среднее по величине число.

# Формат входных данных
# На вход программе подаётся три различных целых числа, каждое на отдельной строке.

# Формат выходных данных
# Программа должна вывести среднее число.

a = int(input())
b = int(input())
c = int(input())
if a > b > c or c > b > a:
    print(b)
elif b > c > a or a > c > b:
    print(c)
elif c > a > b or b > a > c:
    print(a)
else:
    print('error')

# # 
# Количество дней
# Дан порядковый номер месяца 
# (1,2,…, 12)
# Напишите программу, которая выводит на экран количество дней в этом месяце. Принять, что год является невисокосным.
# Примечание. Постарайтесь написать программу так, чтобы в ней было не более трех условий.
# Формат входных данных
# На вход программе подаётся одно целое число – порядковый номер месяца.
# Формат выходных данных
# Программа должна вывести количество дней в этом месяце.
# 
# a = int(input())
# if a == 1 or a == 3 or a == 5 or a == 7 or a == 8 or a == 10 or a == 12:
#     print('31')
# elif a == 2:
#     print('28')
# else:
#     print('30')

# Церемония взвешивания
# Известен вес боксера-любителя (целое число). Известно, что вес таков, что боксер может быть отнесён к одной из трех весовых категорий:
# Легкий вес – до 60 кг;
# Первый полусредний вес – до 64 кг;
# Полусредний вес – до 69 кг.
# Напишите программу, определяющую, в какой категории будет выступать данный боксер.
# Формат входных данных
# На вход программе подаётся одно целое число.
# Формат выходных данных
# Программа должна вывести текст – название весовой категории.
# 
a = int(input())
if a < 60:
    print('Легкий вес')
elif a >= 60 and a < 64:
    print('Первый полусредний вес')
elif a < 69:
    print('Полусредний вес')
    
# Самописный калькулятор 🌶️
# Напишите программу, которая считывает с клавиатуры два целых числа и строку. Если эта строка является обозначением одной из 
# четырёх математических операций (+, -, *, /), то выведите результат применения этой операции к введённым ранее числам,
# в противном случае выведите «Неверная операция». Если пользователь захочет поделить на ноль, выведите текст «На ноль делить нельзя!».
# Формат входных данных
# На вход программе подаются два целых числа, каждое на отдельной строке, и строка.
# Формат выходных данных
# Программа должна вывести результат применения операции к введенным числам или соответствующий текст, если операция неверная либо если происходит деление на ноль.
# 
a = int(input())
b = int(input())
c = input()
if c == '+':
    print(a + b)
elif c == '-':
    print(a - b)
elif c == '*':
    print(a * b)
elif c == '/':
    if b == 0:
        print('На ноль делить нельзя!')
    else:
        print(a / b)
else:
    print('Неверная операция')
    
# Цветовой микшер 🌶️
# Красный, синий и желтый называются основными цветами, потому что их нельзя получить путем смешения других цветов. 
# При смешивании двух основных цветов получается вторичный цвет:
# если смешать красный и синий, то получится фиолетовый;
# если смешать красный и желтый, то получится оранжевый;
# если смешать синий и желтый, то получится зеленый.
# Напишите программу, которая считывает названия двух основных цветов для смешивания. Если пользователь вводит что-нибудь помимо названий «красный»,
«синий» или «желтый», то программа должна вывести сообщение об ошибке.
В противном случае программа должна вывести название вторичного цвета, который получится в результате.
# Формат входных данных
# На вход программе подаются две строки, каждая на отдельной строке.
# Формат выходных данных
# Программа должна вывести полученный цвет смешения либо сообщение «ошибка цвета», если введён был не цвет.
# 
a = input()
b = input()
if a == 'красный':
    if b == 'красный':
        print('красный')
    elif b == 'синий':
        print('фиолетовый')
    elif b == 'желтый':
        print('оранжевый')
    else:
        print('ошибка цвета')
elif a == 'синий':
    if b == 'синий':
        print('синий')
    elif b == 'красный':
        print('фиолетовый')
    elif b == 'желтый':
        print('зеленый')
    else:
        print('ошибка цвета')
elif a == 'желтый':
    if b == 'желтый':
        print('желтый')
    elif b == 'красный':
        print('оранжевый')
    elif b == 'синий':
        print('зеленый')
    else:
        print('ошибка цвета')
else:
    print('ошибка цвета')
    
# Цвета колеса рулетки 🌶️
# На колесе рулетки карманы пронумерованы от 0 до 36. Ниже приведены цвета карманов: карман 0 зеленый;
# для карманов с 1 по 10 карманы с нечетным номером имеют красный цвет, карманы с четным номером – черный;
# для карманов с 11 по 18 карманы с нечетным номером имеют черный цвет, карманы с четным номером – красный;
# для карманов с 19 по 28 карманы с нечетным номером имеют красный цвет, карманы с четным номером – черный;
# для карманов с 29 по 36 карманы с нечетным номером имеют черный цвет, карманы с четным номером – красный.
# Напишите программу, которая считывает номер кармана и показывает, является ли этот карман зеленым, красным или черным. 
# Программа должна вывести сообщение об ошибке, если пользователь вводит число, которое лежит вне диапазона от 0 до 36.
# Формат входных данных
# На вход программе подаётся одно целое число.
# Формат выходных данных
# Программа должна вывести цвет кармана либо сообщение «ошибка ввода», если введённое число лежит вне диапазона от 0 до 36.
# 
a = int(input())
if a == 0:
    print('зеленый')
if a >= 1 and a <= 10:
    if (a % 2) != 0:
        print('красный')
    if (a % 2) == 0:
        print('черный')
elif a >=11 and a <=18:
    if (a % 2) != 0:
        print('черный')
    if (a % 2) == 0:
        print('красный')
elif a >=19 and a <=28:
    if (a % 2) != 0:
        print('красный')
    if (a % 2) == 0:
        print('черный')        
elif a >=29 and a <=36:
    if (a % 2) != 0:
        print('черный')
    if (a % 2) == 0:
        print('красный')
elif a < 0 or a > 36:
    print('ошибка ввода')

# Напишите программу, которая считывает длины двух катетов в прямоугольном треугольнике и выводит его площадь.
# 
a = float(input())
b = float(input())
s = (1/2) * a * b
print(s)

# # Две старушки
# Две старушки идут навстречу друг другу с постоянными скоростями 
# Определите, через какое время (в часах) старушки встретятся, если расстояние между ними равно 
# S км.
# Формат входных данных
# На вход программе подаются три числа с плавающей точкой S, V1, V2 , каждое на отдельной строке.

# Формат выходных данных 
# Программа должна вывести одно число в соответствии с условием задачи.
# 
s = float(input())
v1 = float(input())
v2 = float(input())
result = s / (v1 + v2)
print(result)

# Напишите программу, которая считывает с клавиатуры одно число и выводит обратное ему.
# Если при этом введённое с клавиатуры число – ноль, то вывести «Обратного числа не существует» (без кавычек).
# # Формат входных данных 
# На вход программе подается одно действительное число.
# Формат выходных данных
# Программа должна вывести действительное число обратное данному, либо текст в соответствии с условием задачи.
# 
a = float(input())
if a == 0:
    print('Обратного числа не существует')
else:
    print(a**-1)

# 451 градус по Фаренгейту 
# У известного американского писателя Рэя Бредбери есть роман «451 градус по Фаренгейту». 
# Напишите программу, которая определяет, какой температуре по шкале Цельсия 
# соответствует указанное значение по шкале Фаренгейта.
# Формат входных данных
# На вход программе подаётся вещественное число градусов по шкале Фаренгейта.
# Формат выходных данных
# Программа должна вывести число градусов по шкале Цельсия.
a = float(input())
b = 5 / 9 * (a - 32)
print(b)

# Dog age
# На вход программе подается число 
# n – количество собачьих лет. Напишите программу, которая вычисляет возраст собаки в человеческих годах.
# Формат входных данных
# На вход программе подаётся натуральное число – количество собачьих лет.
# Формат выходных данных
# Программа должна вывести возраст собаки в человеческих годах.
# Примечание. В течение первых двух лет собачий год равен 10.5 человеческим годам. 
# После этого каждый год собаки равен 4 человеческим годам.
# 
a = int(input())
if a == 1:
    b = 10.5
elif a == 2:
    b = 21
else:
    b = ((a - 2) * 4) + (10.5 * 2)
print(b)

# Первая цифра после точки
# Дано положительное действительное число. Выведите его первую цифру после десятичной точки.
# 
a = float(input())
b = a * 10
c = b % 10
print(int(c))

# Дробная часть
# Дано положительное действительное число. Выведите его дробную часть.
# Формат входных данных
# На вход программе подается положительное действительное число.
# Формат выходных данных
# Программа должна вывести дробную часть числа в соответствии с условием задачи.
# 
a = float(input())
b = a  % 1
print(b)

# Наибольшее и наименьшее
# Напишите программу, которая находит наименьшее и наибольшее из пяти чисел.
# Формат входных данных
# На вход программе подается пять целых чисел, каждое на отдельной строке.
# Формат выходных данных
# Программа должна вывести наименьшее и наибольшее число с поясняющей надписью.
# 
a, b, c, d, i = int(input()),int(input()),int(input()),int(input()),int(input())
print('Наименьшее число =',min(a,b,c,d,i))
print('Наибольшее число =',max(a,b,c,d,i))

# Сортировка трёх 🌶️
# Напишите программу, которая упорядочивает три числа от большего к меньшему.
# Формат входных данных
# На вход программе подается три целых числа, каждое на отдельной строке.
# Формат выходных данных
# Программа должна вывести три числа, каждое на отдельной строке, упорядоченных от большего к меньшему.
# 
a, b, c = int(input()),int(input()),int(input())
big = max(a, b, c)
minim = min(a, b, c)
middle = ((a + b + c) - (big + minim))   
print(big)
print(middle)
print(minim)

Интересное число
# Назовем число интересным, если в нем разность максимальной и минимальной цифры равняется средней по величине цифре.
# Напишите программу, которая определяет, интересное число или нет. Если число интересное, 
# следует вывести «Число интересное», иначе - «Число неинтересное».
# Формат входных данных
# На вход программе подается целое трехзначное число.
# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.
# 
a = num // 100
b = (num // 10) % 10
c = num % 10
big = max(a, b, c)
mini = min(a, b, c)
mid = (a + b + c) - (big + mini)
if (big - mini) == mid:
    print('Число интересное')
else:
    print('Число неинтересное')

# Абсолютная сумма
# Даны пять чисел 
# Напишите программу, которая вычисляет сумму их модулей
# Формат входных данных
# На вход программе подается пять действительных чисел 
# каждое на отдельной строке.
# Формат выходных данных
# Программа должна вывести одно число – сумму модулей введённых чисел.
# 
a, b, c, d ,e = float(input()), float(input()), float(input()), float(input()), float(input())
y = abs(a) + abs(b) + abs(c) + abs(d) + abs(e)
print(y)

# Манхэттенское расстояние
# Прогуливаясь по Манхэттену, вы не можете попасть из точки А в точку Б по кратчайшему пути 
# Напишите программу определяющую манхэттенское расстояние между двумя точками, координаты которых заданы.
# Формат входных данных
# На вход программе подается четыре целых числа, каждое на отдельной строке – (p1, p2, q1, q2)
# Формат выходных данных
# Программа должна вывести одно число – манхэттенское расстояние.
# 
p1, p2, q1, q2 = int(input()), int(input()), int(input()), int(input())
print(abs(p1 - q1) + abs(p2 - q2)) 

# What's Your Name?
# Напишите программу, которая считывает с клавиатуры две строки – имя и фамилию пользователя и выводит фразу:
# «Hello [введенное имя] [введенная фамилия]! You just delved into Python».
# 
name = input()
lastname = input()
print(f'Hello {name} {lastname}! You just delved into Python')

# Футбольная команда
# Напишите программу, которая считывает с клавиатуры название футбольной команды и выводит фразу:
# «Футбольная команда [введённая строка] имеет длину [длина введённой строки] символов».

team = input()
length = len(team)
print(f'Футбольная команда {team} имеет длину {length} символов')
