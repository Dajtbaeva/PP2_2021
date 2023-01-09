# Старинная задача

for n in range(100):
    for k in range(100):
        for m in range(100):
            if 10 * n + 5 * k + 0.5 * m == 100 and n + k + m == 100:
                print(n, k, m)