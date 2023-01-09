s = input()
print('Максимальная цифра равна', max(s))
print('Минимальная цифра равна', min(s))

#-----------------------------------------------------------

num = int(input())
flag = True

for i in range(2, num // 2 + 1):
    if num % i == 0:
        flag = False
if num > 1 and flag == True:
    print('Число простое')
else:
    print('Число составное')

#-----------------------------------------------------------

num = int(input())
flag = True

for i in range(2, int(num ** 0.5) + 1):
    if num % i == 0:
        flag = False
if num > 1 and flag == True:
    print('Число простое')
else:
    print('Число составное')

#-----------------------------------------------------------

for hours in range(24):
    for minutes in range(60):
        for seconds in range(60):
            print(hours, ':', minutes, ':', seconds)

0 : 0 : 0
0 : 0 : 1
0 : 0 : 2
...
23 : 59 : 58
23 : 59 : 59 

#-----------------------------------------------------------

print('What is your name?')
name = input()
print('My name is', name)

