numbers = [2, 4, 6, 8, 10]
languages = ['Python', 'C#', 'C++', 'Java']
print(numbers) # [2, 4, 6, 8, 10]
print(languages) # ['Python', 'C#', 'C++', 'Java']
#------------------------------------------------------------------------
numbers = list(range(5))
even_numbers = list(range(0, 10, 2))  # список содержит четные числа 0, 2, 4, 6, 8
odd_numbers = list(range(1, 10, 2))   # список содержит нечетные числа 1, 3, 5, 7, 9

#------------------------------------------------------------------------
s = 'abcde'
chars = list(s)  # список содержит символы 'a', 'b', 'c', 'd', 'e'
Список ['a', 'b', 'c', 'd', 'e'] присваивается переменной chars

#------------------------------------------------------------------------
Элементы массива всегда имеют одинаковый тип данных и располагаются в памяти компьютера 
непрерывным блоком, а элементы списка могут быть разбросаны по памяти как угодно и могут 
иметь разный тип данных. при выводе содержимого списка с помощью функции print(), все 
строковые элементы списка обрамляются одинарными кавычками.

#------------------------------------------------------------------------
n = int(input())
abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(abc[:n])
10 -> ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

#------------------------------------------------------------------------
numbers = [2, 4, 6, 8, 10]

if 2 in numbers:
    print('Список numbers содержит число 2')
else:
    print('Список numbers не содержит число 2')
# Список numbers содержит число 2

#------------------------------------------------------------------------
fruits = ['apple', 'apricot', 'banana', 'cherry', 'kiwi', 'lemon', 'mango']
fruits[2:5] = ['банан', 'вишня', 'киви']
print(fruits)
['apple', 'apricot', 'банан', 'вишня', 'киви', 'lemon', 'mango']

#------------------------------------------------------------------------
print([1, 2, 3, 4] + [5, 6, 7, 8])
print([7, 8] * 3)
print([0] * 10)

#------------------------------------------------------------------------
a = [1, 2, 3, 4]
b = [7, 8]
a += b   # добавляем к списку a список b
b *= 5   # повторяем список b 5 раз 
print(a)
print(b)

[1, 2, 3, 4, 7, 8]
[7, 8, 7, 8, 7, 8, 7, 8, 7, 8]

#------------------------------------------------------------------------
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('Сумма всех элементов списка =', sum(numbers))

#------------------------------------------------------------------------
numbers = [3, 4, 10, 3333, 12, -7, -5, 4]
print('Минимальный элемент =', min(numbers))
print('Максимальный элемент =', max(numbers))
numbers.append(21)  # добавляем число 21 в конец списка

numbers = []  # создаем пустой список
numbers.append(1) # так можно
numbers[0] = 1 # так нельзя

#------------------------------------------------------------------------
numbers = [0, 2, 4, 6, 8, 10]
odds = [1, 3, 5, 7]
numbers.extend(odds)
print(numbers)

[0, 2, 4, 6, 8, 10, 1, 3, 5, 7]

#------------------------------------------------------------------------
words1 = ['iq option', 'stepik', 'beegeek']
words2 = ['iq option', 'stepik', 'beegeek']

words1.append('python')
words2.extend('python')

print(words1)
print(words2)

['iq option', 'stepik', 'beegeek', 'python']
['iq option', 'stepik', 'beegeek', 'p', 'y', 't', 'h', 'o', 'n']

#------------------------------------------------------------------------
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
del numbers[::2]

print(numbers)

[2, 4, 6, 8]

#------------------------------------------------------------------------
# Сумма двух соседних
n = int(input())
a, res = [], []
cnt = 0
for i in range(n):
    b = int(input())
    a.append(b)
for i in range(n - 1):
    res.append(a[i] + a[i + 1])
print(res)
#------------------------------------------------------------------------
n, a, res = int(input()), [], ''
for i in range(n):
    s  = input()
    a.append(s)
k = int(input()) 
for j in range(len(a)):
    if len(a[j]) > k - 1:
        res += a[j][k - 1]
print(res)

5
abcdef
bcdefg
cdefgh
defghi
efghij
2
-> bcdef

#------------------------------------------------------------------------
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in range(len(numbers)):
    print(numbers[i])
================================================
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in numbers:
    print(num, end=' ')
================================================
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(*numbers)

#------------------------------------------------------------------------
n, a = int(input()), []
for i in range(n):
    b = int(input())
    a.append(b)
del a[a.index(max(a))]
del a[a.index(min(a))]
print(*a, sep = '\n')

#------------------------------------------------------------------------
# УДАЛИТЬ ДУБЛИКАТЫ
n, a = int(input()), []
for i in range(n):
    b = input()
    if b not in a:
        a.append(b)
print(*a, sep = '\n')

#------------------------------------------------------------------------
n, neg, zer, pos = int(input()), [], [], []
for i in range(n):
    b = int(input())
    if b < 0:
        neg.append(b)
    elif b == 0:
        zer.append(b)
    else:
        pos.append(b)
print(*neg, sep = '\n')
print(*zer, sep = '\n')
print(*pos, sep = '\n')

#------------------------------------------------------------------------
n, a = int(input()), []
for _ in range(n):
    b = input()
    a.append(b)
k, c = int(input()), []
for _ in range(k):
    b = input()
    c.append(b)
for i in range(n):
    cnt = 0
    for j in range(k):
        if c[j].lower() in a[i].lower():
            cnt+= 1
    if cnt == k:
        print(a[i])

5
Язык Python прекрасен
C# - отличный язык программирования
Stepik - отличная платформа
BEEGEEK FOREVER!
язык Python появился 20 февраля 1991
2
язык
python
->  Язык Python прекрасен
    язык Python появился 20 февраля 1991

#------------------------------------------------------------------------
SPLIT: string to list
s = 'Python is the most powerful language'
words = s.split()
print(words)

['Python', 'is', 'the', 'most', 'powerful', 'language']

#------------------------------------------------------------------------
numbers = input().split() # Если при запуске этой программы ввести строку 
# 1 2 3 4 5, то список numbers будет следующим  ['1', '2', '3', '4', '5']
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])

#------------------------------------------------------------------------
# РАЗДЕЛИТЕЛЬ У СПЛИТА split('.')
ip = '192.168.1.24'
numbers = ip.split('.')    # указываем явно разделитель
print(numbers)

['192', '168', '1', '24']

#------------------------------------------------------------------------
JOIN: list to string
words = ['Python', 'is', 'the', 'most', 'powerful', 'language']
s = ' '.join(words)
print(s)
s = Python is the most powerful language

#------------------------------------------------------------------------
words = ['Мы', 'учим', 'язык', 'Python']
print('*'.join(words))
print('-'.join(words))
print('?'.join(words))

Мы*учим*язык*Python
Мы-учим-язык-Python
Мы?учим?язык?Python

#------------------------------------------------------------------------
s, t = input(), input()
print(t.join(s))

1234567
*v
1*2*3*4*5*6*7

#------------------------------------------------------------------------
names = ['Gvido', 'Roman' , 'Timur']
print(names)
names.insert(0, 'Anders')
print(names)
names.insert(3, 'Josef')
print(names)

['Gvido', 'Roman' , 'Timur']
['Anders', 'Gvido', 'Roman' , 'Timur']
['Anders', 'Gvido', 'Roman' , 'Josef', 'Timur']

#------------------------------------------------------------------------
names = ['Gvido', 'Roman' , 'Timur']
position = names.index('Timur')
print(position)
2

#------------------------------------------------------------------------
names = ['Gvido', 'Roman' , 'Timur']
if 'Anders' in names:
    position = names.index('Anders')
    print(position)
else:
    print('Такого значения нет в списке')

#------------------------------------------------------------------------
food = ['Рис', 'Курица', 'Рыба', 'Брокколи', 'Рис']
print(food)
food.remove('Рис')
print(food)
['Рис', 'Курица', 'Рыба', 'Брокколи', 'Рис']
['Курица', 'Рыба', 'Брокколи', 'Рис']

#------------------------------------------------------------------------
names = ['Gvido', 'Roman' , 'Timur']
item = names.pop(1)
print(item)
print(names)
Roman
['Gvido', 'Timur']

#------------------------------------------------------------------------
names = ['Timur', 'Gvido', 'Roman', 'Timur', 'Anders', 'Timur']
cnt1 = names.count('Timur')
cnt2 = names.count('Gvido')
cnt3 = names.count('Josef')

print(cnt1)
print(cnt2)
print(cnt3)

3
1
0
#------------------------------------------------------------------------
names = ['Gvido', 'Roman' , 'Timur']
names.reverse()
print(names)
['Timur', 'Roman', 'Gvido']

#------------------------------------------------------------------------
names = ['Gvido', 'Roman' , 'Timur']
names.clear()
print(names)
[]

#------------------------------------------------------------------------
names = ['Gvido', 'Roman' , 'Timur']
names_copy = names.copy()              # создаем поверхностную копию списка names

print(names)
print(names_copy)
['Gvido', 'Roman', 'Timur']
['Gvido', 'Roman', 'Timur']

names = ['Gvido', 'Roman' , 'Timur']
names_copy1 = list(names)             # создаем поверхностную копию с помощью функции list()
names_copy2 = names[:]                # создаем поверхностную копию с помощью среза от начала до конца

#------------------------------------------------------------------------
s = input().split(' ')
for i in range(len(s)):
    s[i] = int(s[i])
ind_min = s.index(max(s))
ind_max = s.index(min(s))
s[ind_min], s[ind_max] = s[ind_max], s[ind_min]
print(*s)

#------------------------------------------------------------------------
a = [1, 7, -3, 9, 0, -67, 34, 12, 45, 1000, 6,  8, -2, 99]
a.sort(reverse = True)   # сортируем по убыванию
print('Отсортированный список:', a)

#------------------------------------------------------------------------
zeros = []
for i in range(10):
    zeros.append(0)
==================================
zeros = [0] * 10

#------------------------------------------------------------------------
numbers = []
for i in range(10):
    numbers.append(i)
=================================
numbers = [i for i in range(10)]

#------------------------------------------------------------------------
1. Создать список, заполненный 10 нулями можно и при помощи списочного выражения:
zeros = [0 for i in range(10)]

2. Создать список, заполненный квадратами целых чисел от 0 до 9 можно так:
squares = [i ** 2 for i in range(10)]

3. Создать список, заполненный кубами целых чисел от 10 до 20 можно так:
cubes = [i ** 3 for i in range(10, 21)]

4. Создать список, заполненный символами строки:
chars = [c for c in 'abcdefg']
print(chars)

#------------------------------------------------------------------------
n = int(input())
lines = [input() for _ in range(n)]
====================================
lines = [input() for _ in range(int(input()))]
====================================
numbers = [int(input()) for _ in range(int(input()))]
=====================================
evens = [i for i in range(21) if i % 2 == 0]
=====================================
evens = [i for i in range(0, 21, 2)]
=====================================
numbers = [i * j for i in range(1, 5) for j in range(2)]
print(numbers)
[0, 1, 0, 2, 0, 3, 0, 4]
=====================================
# Delete first character of each word
keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 
'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'try', 
'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 
'or', 'pass', 'raise', 'return', 'while', 'yield']

new_keywords = [key[1:] for key in keywords]

print(new_keywords)
=====================================
palindromes = [a for a in range(100, 1001) if str(a) == str(a)[::-1]]
print(palindromes)

#------------------------------------------------------------------------
В ОДНУ СТРОКУ

print(*input().split(' '), sep = '\n')
Умей ценить того кто без тебя не может
Умей
ценить
того
кто
без
тебя
не
может

#------------------------------------------------------------------------
В ОДНУ СТРОКУ

print(*[i for i in input() if i.isdigit()], sep = '')
Число Pi примерно равно 3.1415 -> 31415
выводим распоковывая список * переменная цикла i for i in input().....

#------------------------------------------------------------------------
В ОДНУ СТРОКУ
print(*[int(i)**2 for i in input().split(' ') if int(i) % 2 == 0 and (int(i)**2) % 10 != 4])
которая выведет квадраты четных чисел, которые не оканчиваются на цифру 4
1 2 3 4 5 6 7 8 9
16 36

#------------------------------------------------------------------------
Если надо выполнить одинаковое действие со списком, например перевести все 
слова в другой регистр или строки перевести в числа, то достаточно написать 
map(функция, последовательность). Например map(int, список) переведёт весь 
список в целые числа и не надо возле каждой переменной писать int(a)

#------------------------------------------------------------------------
Медленные:
Пузырьковая сортировка (Bubble sort);
Сортировка выбором (Selection sort);
Сортировка простыми вставками (Insertion sort).

Быстрые:
Сортировка Шелла (Shell sort);
Быстрая сортировка (Quick sort);
Сортировка слиянием (Merge sort);
Пирамидальная сортировка (Heap sort);
Сортировка TimSort (используется в Java и Python).

К алгоритмам не основанным на сравнениях можно отнести следующие:
Сортировка подсчетом (Counting sort);
Блочная сортировка (Bucket sort);
Поразрядная сортировка (Radix sort).

#------------------------------------------------------------------------
Пузырьковая сортировка (Bubble sort);

a = [1, 7, -3, 9, 0, -67, 34, 12, 45, 1000, 6,  8, -2, 99]
n = len(a)

for i in range(n - 1):
    for j in range(n - i - 1):
        if a[j] > a[j + 1]:                  # если порядок элементов пары неправильный
            a[j], a[j + 1] = a[j + 1], a[j]  # меняем элементы пары местами 

print('Отсортированный список:', a)
Отсортированный список: [-67, -3, -2, 0, 1, 6, 7, 8, 9, 12, 34, 45, 99, 1000]

#------------------------------------------------------------------------
Сортировка выбором (Selection sort);

a = [78, -32, 5, 39, 58, -5, -63, 57, 72, 9, 53, -1, 63, -97, -21, -94, -47, 
57, -8, 60, -23, -72, -22, -79, 90, 96, -41, -71, -48, 84, 89, -96, 41, -16, 
94, -60, -64, -39, 60, -14, -62, -19, -3, 32, 98, 14, 43, 3, -56, 71, -71, 
-67, 80, 27, 92, 92, -64, 0, -77, 2, -26, 41, 3, -31, 48, 39, 20, -30, 35, 
32, -58, 2, 63, 64, 66, 62, 82, -62, 9, -52, 35, -61, 87, 78, 93, -42, 87, 
-72, -10, -36, 61, -16, 59, 59, 22, -24, -67, 76, -94, 59]
res = []
n = len(a)
for i in range(n):
    b = min(a)
    res.append(b)
    a.remove(b)
    n -= 1
print(*res)

#------------------------------------------------------------------------
Сортировка простыми вставками (Insertion sort).

a = [1, 7, -3, 9, 0, -67, 34, 12, 45, 1000, 6,  8, -2, 99]
n = len(a)

for i in range(1, n): 
    elem = a[i]  # первый элемент из неотсортированной части списка
    j = i
    while j >= 1 and a[j - 1] > elem: 
        a[j] = a[j - 1]
        j -= 1
    a[j] = elem


print('Отсортированный список:', a)

#------------------------------------------------------------------------
# Функция randint() принимает два обязательных аргумента a и b и возвращает
# случайное целое число из отрезка 
import random
from tkinter import PROJECTING

num1 = random.randint(0, 17)
num2 = random.randint(-5, 5)

print(num1)
print(num2)

#------------------------------------------------------------------------
# Следующий код выводит 1010 случайных целых чисел из диапазона [1; \, 100][1;100]:

import random

for _ in range(10):
    print(random.randint(1, 100))

#------------------------------------------------------------------------
# Следующий код задает начальное значение, конечный предел и величину шага:

import random

num = random.randrange(0, 101, 10)

#------------------------------------------------------------------------
# Функция random() возвращает случайное число с плавающей точкой в диапазоне от 
# 0.00.0 до 1.01.0 (исключая 1.01.0). Следующий код выводит случайное число с плавающей 
# точкой из диапазона [0.0; \, 1.0)[0.0;1.0):

import random

num = random.random()
print(num)

#------------------------------------------------------------------------
# Функция uniform() тоже возвращает случайное число с плавающей точкой, но
# при этом она позволяет задавать диапазон для отбора значений.

import random

num = random.uniform(1.5, 17.3)
print(num)

#------------------------------------------------------------------------
# Следующий код генерирует 1010 случайных чисел, и при этом содержит инструкцию, 
# явно устанавливающую начальное значение для генератора случайных чисел:

import random

random.seed(17)   # явно устанавливаем начальное значение для генератора случайных чисел

for _ in range(10):
    print(random.randint(1, 100))

#------------------------------------------------------------------------
Подключение модуля следующим образом:

from random import *
позволяет в дальнейшем не писать название модуля и символ точки при вызове функций модуля.


#------------------------------------------------------------------------
# Мы можем сымитировать бросание монеты путем генерации случайного числа в диапазоне от 
# 0 до 1. Для генерации целых чисел мы будем использовать функцию randint():
import random

for _ in range(10):
    num = random.randint(0, 1)
    if num == 0:
        print('Орел')
    else:
        print('Решка')

#------------------------------------------------------------------------
# Следующий код перемешивает список numbers случайным образом, а затем выводит его содержимое:

import random

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
random.shuffle(numbers)
print(numbers)

#------------------------------------------------------------------------
# Функция choice() принимает список (строку) в качестве обязательного аргумента 
# и возвращает один случайный элемент из переданного списка (строки).
import random

print(random.choice('BEEGEEK'))
print(random.choice([1, 2, 3, 4]))
print(random.choice(['a', 'b', 'c', 'd']))

E
3
c

#------------------------------------------------------------------------
# Функция sample() принимает два обязательных аргумента: список (строку) и 
# количество случайных элементов, а возвращает список случайных элементов в указанном количестве.

import random
 
numbers = [2, 5, 8, 9, 12]

print(random.sample(numbers, 1))
print(random.sample(numbers, 2))
print(random.sample(numbers, 3))
print(random.sample(numbers, 5))

[9]
[12, 5]
[9, 2, 8]
[12, 8, 9, 5, 2]

#------------------------------------------------------------------------
from random import randint
print("Игра - 'Угадайка число!'")
name = input('Пожалуйста введите ваше имя: ')
num = randint(1, 100)
while True:
    user_num = int(input(f'{name} введите число от 1 до 100: '))
    if user_num > num:
        print('Слишком много, попробуйте еще раз')
    elif user_num < num:
        print('Слишком мало, попробуйте еще раз')
    else:
        print('Вы угадали, поздравляем!')
        break

#------------------------------------------------------------------------
# Программа должна вывести наименьшее количество вопросов, которых гарантированно
# хватит Руслану, чтобы угадать число Тимура.
num = int(input())
cnt = 0
while num != 1:
    if num % 2 != 0:
        num += 1
    num //= 2
    cnt += 1
print(cnt)

8 -> 3

#------------------------------------------------------------------------
from random import *

num = randint(1,100)

print('Добро пожаловать в числовую угадайку')


#------------------------------------------------------------------------
MINI PROJECTING
# Функция проверки введенных данных на корректность:
def is_valid(num):
    if num.isdigit():
        num = int(num)
        if 1 <= num <= 100:
            return True
        else:
            return False
    else:
        return False

import random                    # подключаем модуль

number = random.randint(1, 101)  # генерируем случайное число от 1 до 100

print('Добро пожаловать в числовую угадайку')

while True:
    response = input('Введите число от 1 до 100:')
    if not is_valid(responce):
        print('А может быть все-таки введем целое число от 1 до 100?')
        continue
    response = int(response)
    # Сравнение введенного числа с загаданным числом:
    if val < number:
        print('Ваше число меньше загаданного, попробуйте еще разок')
    elif val > number:
        print('Ваше число больше загаданного, попробуйте еще разок')
    else:
        print('Вы угадали, поздравляем!')
        break

print('Спасибо, что играли в числовую угадайку. Еще увидимся...')

#------------------------------------------------------------------------
# магический шар 8 (шар судьбы) — шуточный способ предсказывать будущее. 
# Программа должна просить пользователя задать некий вопрос, чтобы случайным образом на него ответить.

import random

answers = ['Бесспорно', 'Мне кажется - да', 'Пока не ясно, попробуй снова', 'Даже не думай', 
'Предрешено', 'Вероятнее всего', 'Спроси позже', 'Мой ответ - нет', 'Никаких сомнений', 
'Хорошие перспективы', 'Лучше не рассказывать', 'По моим данным - нет', 'Определённо да', 
'Знаки говорят - да', 'Сейчас нельзя предсказать', 'Перспективы не очень хорошие', 
'Можешь быть уверен в этом', 'Да', 'Сконцентрируйся и спроси опять', 'Весьма сомнительно']
print('Привет Мир, Я магический шар, и я знаю ответ на любой твой вопрос.')

name = input('Как тебя зовут?')
print('Привет',  name)
again = 'д'

while again.lower() == 'д':
    question = input('Задай мне свой вопрос: ')
    print(random.choice(answers))
    again = input('Задать еще один вопрос? (д = да, н = нет): ')
    
    if not again.lower() == 'д':
        print('Возвращайся если возникнут вопросы!')

#------------------------------------------------------------------------
# программа генерирует заданное количество паролей и включает в себя умную настройку 
# на длину пароля, а также на то, какие символы требуется в него включить, а какие исключить.

import random
def generate_password(length, chars):
    password = ''
    for j in range(length):
        password += random.choice(chars)
    return password

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'

chars = ''
n = int(input('Введите количество паролей для генерации: '))
length = int(input('Введите длину пароля: '))
add_digit = input('Включить цифры? (д = да, н = нет) ').strip()
add_lowercase = input('Включить прописные буквы? (д = да, н = нет) ').strip()
add_uppercase = input('Включить строчные буквы? (д = да, н = нет) ').strip()
add_punctuation = input('Включить символы, такие как !#$%&*+-=?@^_? (д = да, н = нет) ').strip()
remove_badsymbols = input('Исключить символы il1Lo0O? (д = да, н = нет)').strip()

if add_digit.lower() == 'д':
    chars += digits
if add_lowercase.lower() == 'д':
    chars += lowercase_letters
if add_uppercase.lower() == 'д':
    chars += uppercase_letters
if add_punctuation.lower() == 'д':
    chars += punctuation
if remove_badsymbols.lower() == 'д':
    for c in 'il1Lo0O':
        chars = chars.replace(c, '')
for _ in range(n):
    generate_password(length, chars)

#------------------------------------------------------------------------
#------------------------------------------------------------------------
#------------------------------------------------------------------------
#------------------------------------------------------------------------
#------------------------------------------------------------------------
#------------------------------------------------------------------------
#------------------------------------------------------------------------
#------------------------------------------------------------------------
#------------------------------------------------------------------------
#------------------------------------------------------------------------
#------------------------------------------------------------------------
#------------------------------------------------------------------------
#------------------------------------------------------------------------
#------------------------------------------------------------------------
#------------------------------------------------------------------------
#------------------------------------------------------------------------
#------------------------------------------------------------------------
#------------------------------------------------------------------------
#------------------------------------------------------------------------
#------------------------------------------------------------------------
#------------------------------------------------------------------------
#------------------------------------------------------------------------
#------------------------------------------------------------------------
#------------------------------------------------------------------------
#------------------------------------------------------------------------
#------------------------------------------------------------------------
#------------------------------------------------------------------------
#------------------------------------------------------------------------
#------------------------------------------------------------------------
#------------------------------------------------------------------------
#------------------------------------------------------------------------
#------------------------------------------------------------------------
#------------------------------------------------------------------------
#------------------------------------------------------------------------
#------------------------------------------------------------------------
#------------------------------------------------------------------------
#------------------------------------------------------------------------
#------------------------------------------------------------------------
#------------------------------------------------------------------------
#------------------------------------------------------------------------
#------------------------------------------------------------------------
#------------------------------------------------------------------------
#------------------------------------------------------------------------
#------------------------------------------------------------------------
#------------------------------------------------------------------------
#------------------------------------------------------------------------
#------------------------------------------------------------------------
#------------------------------------------------------------------------
#------------------------------------------------------------------------
#------------------------------------------------------------------------
#------------------------------------------------------------------------
#------------------------------------------------------------------------
#------------------------------------------------------------------------
#------------------------------------------------------------------------
#------------------------------------------------------------------------
#------------------------------------------------------------------------
#------------------------------------------------------------------------
#------------------------------------------------------------------------
#------------------------------------------------------------------------
#------------------------------------------------------------------------
#------------------------------------------------------------------------
#------------------------------------------------------------------------
#------------------------------------------------------------------------
#------------------------------------------------------------------------

