def unique(a):
    res = []
    for i in a:
        if i not in res:
            res.append(i)
    print(*res)
unique(input().split())