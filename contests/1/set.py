# Set
a = list(set(i) for i in input().split())
b = a[0]
for i in a:
    b = b.intersection(i)
print(*sorted(b), sep = '')
# great eat meat fat attendance
# at
