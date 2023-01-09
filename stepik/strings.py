#Decimal to Binary
from abc import abstractmethod

n = int(input())
s = ''
while n > 0:
    s = str(n % 2) + s
    n //= 2
print(s)
b = str(n % 2) + b и Ответ: при n=8 b=1000 
b = b + str(n % 2) Ответ: при n=8 b=0001
# ------------------------------------
s = 'abcdef'
for c in s:
    print(c)
# ------------------------------------
s = 'abcdef'
for i in range(len(s)):
    print(s[i])
# ------------------------------------
s = input()
for i in range(-1, -len(s) - 1, -1):
    print(s[i])

x = "hello world"
x[::-1] = "dlrow olleh"
# ------------------------------------
s = input()
flag = False
for i in range(len(s)):
    if s[i] in '0123456789':
        print('Цифра')
        flag = True
        break
if flag == False:
    print('Цифр нет') 
# ------------------------------------
# Программа должна вывести количество одинаковых соседних символов
s = input()
cnt = 0
for i in range(len(s) - 1):
    if s[i] == s[i + 1]:
        cnt += 1
print(cnt)
# ------------------------------------
s = input()
g, sog = 0, 0
for i in range(len(s)):
    if s[i] in 'ауоыиэяюёеАУОЫИЭЯЮЁЕ':
        g += 1
    elif s[i] in 'бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ':
        sog += 1
print('Количество гласных букв равно', g)
print('Количество согласных букв равно', sog)
# ------------------------------------
s = 'abcdefghij'
print(s[:]) # abcdefghij
print(s[:-1]) # without last char
print(s[2:5]) # cde
print(s[0:6]) or print(s[:6]) # abcdef 
print(s[2:]) # cdefghij
print(s[:7]) # abcdefg
print(s[-9:-4]) # bcdef
print(s[-3:]) # hij
print(s[:-3]) # abcdefg
print(s[1:7:2]) # bdf
print(s[::-1]) # jihgfedcba -> reversed string
print(s[3::2]) # dfhj
print(s[:7:3]) # adg
print(s[::2]) # acegi
print(s[::-2]) # jhfdb
print(s[1:len(s) - 1]) # without first and last chars
# ------------------------------------
# Palindrome
s = input()
t = s[::-1]
if s == t:
    print('YES')
else:
    print('NO')
# ------------------------------------
# VSE
s = input()
print(s[2])
print(s[len(s) - 2])
print(s[:5])
print(s[:len(s) - 2])
print(s[::2])
print(s[1::2])
print(s[::-1])
print(s[-1::-2])
третий символ этой строки;
предпоследний символ этой строки;
первые пять символов этой строки;
всю строку, кроме последних двух символов;
все символы с четными индексами;
все символы с нечетными индексами;
все символы в обратном порядке;
все символы строки через один в обратном порядке, начиная с последнего.
# ---------------------------------------------------------------
# Напишите программу, которая разрежет ее на две равные части, переставит их местами 
from math import*
s = input()
res = True
if len(s) == 1:
    print(s)
    res = False
if res == True:
    a = ceil(len(s)//2)
    if len(s) % 2 == 0:
        print(s[-a:] + s[:a])
    else:
        print(s[-a:] + s[:a + 1])

or print(s[len(s) // 2] + s[len(s) % 2])
# ---------------------------------------------------------------
# Самый частотный символ
s = input()
maxi, res = 0, 0
for i in s:
    if s.count(i) >= maxi:
        maxi = s.count(i)
        res = i
print(res)
# abaabbcccc -> c
# ---------------------------------------------------------------
age = 27
name = 'Timur'
profession = 'math teacher'
txt = 'My name is {}, I am {}, I work as a {}'.format(name, age, profession)
print(txt)
# ---------------------------------------------------------------
first_name = 'Timur'
last_name = 'Guev'
age = 27
profession = 'math teacher'
affiliation = 'BeeGeek'
print(f'Hello, {first_name} {last_name}. You are {age}. You are a {profession}. 
You were a member of {affiliation}')
# ---------------------------------------------------------------
# СДВИГ
n, s = int(input()), input()
for i in range(len(s)):
    a = ord(s[i]) - n
    if a < 97:
        a = 26 + a
    print(chr(a), end = '')
# ---------------------------------------------------------------

for i in range(26):
    print(chr(ord('A') + i)) 
# ---------------------------------------------------------------
s = 'Python'

print(*s)
print()
print(*s, sep='\n')
P y t h o n

P
y
t
h
o
n
# ---------------------------------------------------------------

METHODS!!!!!!!!!!!!!
print(s.capitalize()) #первый символ имеет верхний регистр,а все остальные символы имеют нижний регистр
print(s.swapcase()) 
print(s.title()) # первый символ каждого слова переводится в верхний регистр, остальное в нижний регистр
print(s.lower())
print(s.upper())
print(s.count('oo', 0, 8)) # count(<sub>, <start>, <end>) считает количество непересекающихся вхождений 
# подстроки <sub> в исходную строку s.s = 'foo goo moo' -> 2
print(s.startswith('foo')) # startswith(<suffix>, <start>, <end>) определяет начинается ли исходная 
# строка s подстрокой <suffix> Если исходная строка начинается с подстроки <suffix>,метод возвращает 
# значение True, а если нет, то  False
print(s.endswith('bar')) 
# find(<sub>, <start>, <end>) находит индекс первого вхождения подстроки <sub> в исходной строке s, -1
# rfind(<sub>, <start>, <end>) ищет первое вхождение подстроки <sub> начиная с конца строки s, otherwise -1
# strip() возвращает копию строки s у которой удалены все пробелы стоящие в начале и конце строки
# lstrip() возвращает копию строки s у которой удалены все пробелы стоящие в начале строки
# rstrip() возвращает копию строки s у которой удалены все пробелы стоящие в конце строки
# strip(), lstrip(), rstrip() могут принимать на вход опциональный аргумент<chars>
# Необязательный аргумент <chars>– это строка, которая определяет набор символов для удаления
# replace(<old>, <new>) возвращает копию s со всеми вхождениями подстроки <old>, замененными на <new>
print(s1.isalnum()) # True or False состоит ли исходная строка ТОЛЬКО из буквенно-цифровых символов
print(s1.isalpha()) # True or False состоит ли исходная строка ТОЛЬКО ИЗ БУКВ
print(s1.isdigit()) # True or False состоит ли исходная строка ТОЛЬКО ИЗ ЦИФР
print(s1.islower()) 
print(s1.isupper())
print(s1.isspace()) # True or False состоит ли исходная строка ТОЛЬКО ИЗ ПРОБЕЛОВ
num1 = ord('A') # num = 65 -> принимает именно одиночный символ
chr1 = chr(65) # A
chr(ord('A')) = 'A', ord(chr(65)) = 65

# ---------------------------------------------------------------
# Напишите программу, которая возвращает исходную строку и переворачивает последовательность
# символов, заключенную между первым и последним вхождением буквы «h».


s = input()
s2 = s[s.find('h') + 1: s.rfind('h')]
print(s[:s.find('h') + 1] + s2[::-1] + s[s.rfind('h'):])



