n, a = int(input()), []
for i in range(n):
    a.append([int(j) for j in input().split()])
res = [[0 for i in range(n)] for i in range(n)]
for i in range(len(a)):
    for j in range(len(a[0])):
        for k in range(len(a)):
            res[i][j] += a[i][k] * a[k][j]  
for i in range(len(res)):
    for j in range(len(res)):
        if res[i][j] != a[i][j]:
            print('Bad matrix')
            exit()
print('Good matrix')