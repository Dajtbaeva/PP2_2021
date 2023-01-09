a = list(map(int, input().split()))
res, ans = 0, [0]
for i in a:
    res += i
    ans.append(res)
print(max(ans))