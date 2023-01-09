n, res = int(input()), []
if n >= 1:
    res.append(0)
    res.append(1)
    if n == 1:
        print(res)
        exit(0)
for i in range(2, n + 1):
    res.append(res[i - 1] + res[i - 2])
print(res)
# 5 -> [0, 1, 1, 2, 3, 5]

