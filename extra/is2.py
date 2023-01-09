a = input().split()
res = [0 for i in range(10)]
for i in a:
    for j in i:
        if j.isdigit():
            res[int(j)] = i
            break
ans = [j for j in res if j != 0]
print(type(a))
print(*ans)
# is2 Thi1s T4estaaaaa 3a -> Thi1s is2 3a T4estaaaaa 