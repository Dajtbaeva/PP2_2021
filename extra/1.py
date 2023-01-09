a = list(map(int, input().split()))
print(*[(a[i] + a[i + 1]) / 2 for i in range(len(a) - 1)])