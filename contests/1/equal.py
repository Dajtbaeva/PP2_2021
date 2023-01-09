# Equal sum
a = list(map(int, input().split()))
for i in range(len(a)):
    if (sum(a[:i]) == sum(a[i + 1:])):
        print(i)
        exit(0)
print('-1')
# 1 2 3 4 3 2 1 -> 3
# 1 100 50 -51 1 1 -> 1
