a, c = list(input()), input()
res = [i for i in range(len(a)) if a[i] == c]
if len(res) == 1:
    print(*res)
else:
    print(min(res), max(res))