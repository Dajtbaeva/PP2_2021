# Численный треугольник 3
n = int(input())
res = 1
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(res, end = ' ')
        res += 1
    print()

4
1 
2 3 
4 5 6 
7 8 9 10 
