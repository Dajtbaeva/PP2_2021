# Maximum product of two elements
n, a = int(input()), list(map(int, input().split()))
a.sort()
print(a[len(a) - 1] * a[len(a) - 2])
