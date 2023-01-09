n = int(input())
k = []
for i in range(n):
    a = list(input().split())
    b = []
    b = [a[i] for i in range(1, len(a))]
    b.sort(key = lambda x : (len(x), x))
    b.insert(0, a[0])
    k.append(b)
k.sort(key = lambda x : (-len(x), x[0]))
for i in k:
    print(*i)

