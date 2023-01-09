# We got stronger
x, a = int(input()), []
while x != 0:
    a.append(x)
    x = int(input())
    
if len(a) % 2 == 0:
    for i in range(len(a) // 2):
        b = len(a) - 1 - i
        if i == b:
            print(a[i], end = ' ')
        else:
            print(a[i] + a[b], end = ' ')
else:
    for i in range(len(a) // 2 + 1):
        b = len(a) - 1 - i
        if i == b:
            print(a[i], end = ' ')
        else:
            print(a[i] + a[b], end = ' ')