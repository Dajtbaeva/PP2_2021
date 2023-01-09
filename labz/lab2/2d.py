# Tsunami
n = int(input())
for i in range(1, n + 1):
    if n % 2 == 0:
        print('#' * i + '.' * (n - i))
    else:
        print('.' * (n - i) + '#' * i)