m, p, n = float(input()), float(input()), int(input())
for i in range(n):
    print(i + 1, m * ((p / 100) + 1) ** i)
# 10
# 50
# 6
# -----
# 1 10.0
# 2 15.0
# 3 22.5
# 4 33.75
# 5 50.625
# 6 75.9375
