# XOR in an array
n = list(map(int, input().split()))
x = None
if len(n) <= 1:
    x = int(input())
if x is None:
    x = n[1]
n = n[0]

a, res = [x + 2 * i for i in range(n)], 0
for i in range(n):
    res ^= a[i]
print(res)