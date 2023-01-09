# Asmay -> You are initially located at the 1 element in array, and
# each element represents your maximum jump length at that position
a, c = list(map(int, input().split())), 0
for i in a:
    for j in range(c, c + 1 + a[c]):
        if c + 1 + a[c] >= len(a):
            print(1)
            exit(0)
        if c + a[c] < a[j] + j:
            c = j
print(0)
# 2 3 1 1 4 -> 1
# 3 2 1 0 4 -> 0
# 2 3 0 1 3 4 1 5 8 0 56 3 1 -> 1
