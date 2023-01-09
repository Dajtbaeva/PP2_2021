# Цифровой корень
n = int(input())
res = 0
while n >= 10:
    while n > 0:
        a = n % 10
        res += a
        n //= 10
    n = res
    res = 0
print(n)