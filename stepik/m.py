n = int(input())
res = True
b = n % 10
while n != 0:
    a = n % 10
    if a < b:
        res = False
    else:
        b = a
    n //= 10
if res == True:
    print('YES')
else:
    print('NO')
# 5321 -> YES; 7820 -> NO


