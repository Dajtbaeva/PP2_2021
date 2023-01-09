# Численный треугольник 4

n = int(input())
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end = '')
    for l in range(i - 1, 0, -1):
        print(l, end = '')
    print()

6
1
121
12321
1234321
123454321
12345654321
