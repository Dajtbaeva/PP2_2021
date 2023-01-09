# 12 month -> 28n+30k+31m=365.

for n in range(1, 28):
    for k in range(1, 30):
        for m in range(1, 31):
            if 28 * n + 30 * k + 31 * m == 365:
                print(n, k, m)