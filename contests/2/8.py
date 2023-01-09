# Villages
res, ans = [], dict()
for i in range(int(input())):
    a = []
    s = input()
    a.append(s.rstrip()) # village
    for j in range(int(input())):
        n = list(input().split())
        a.append(n)
    res.append(a)
element = input()
for i in res:
    for j in range(1, len(i)):
        b = []
        if element in i[j]:
            pos = i[j].index(element)
            ans[i[j][pos - 1]] = i[0]
    
print(*ans.items(), sep = '\n')

