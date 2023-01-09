# Final essay
import re
s = input()
a = re.sub("[^\w]", " ",  s).split()
b = set(a)
print(len(b))
print(*sorted(b), sep = '\n')

"""
re.sub(pattern, repl, string)
pattern is any non-alphanumeric character.
[\w] means any alphanumeric character and is equal to the character set [a-z, A-Z, 0-9]
match any non-alphanumeric character and replace it with a space 
and then we split() it which splits string by space and converts it to a list

1)
d = input().split()
s = set()
for j in d:
    if not j[-1].isalpha(): # True or False состоит ли исходная строка ТОЛЬКО ИЗ БУКВ
        j = j[:len(j) - 1]
    s.add(j)
res = list(s)
print(len(res))
res.sort()
for i in res:
    print(i)

2)
res = []
for i in input().split():
    i = i.strip('.?!,;:')
    if i not in res:
        res.append(i)
print(len(res))
print(*sorted(res), sep = '\n')
strip() возвращает копию строки s у которой удалены все пробелы стоящие в начале и конце строки,
может принимать на вход опциональный аргумент<chars>– это строка, которая определяет набор 
символов для удаления

"""
