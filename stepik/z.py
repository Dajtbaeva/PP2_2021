# Программа должна вывести все простые числа от aa до bb включительно, каждое на отдельной строке
a, b = int(input()), int(input())
for i in range(a, b + 1):
    flag = True
    for j in range(2, i):
        if i % j == 0:
            flag = False
    if flag == True and i != 1:
        print(i)
    else:
        continue
