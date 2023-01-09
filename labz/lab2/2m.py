#  Important dates
x, a = input(), []
while x != '0':
    x = x.split()
    a.append(x)
    x = input()
a.sort(key = lambda z : (z[2], z[1], z[0]))
for j in a:
    print(*j)