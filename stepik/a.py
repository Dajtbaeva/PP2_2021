
for i in range(8):
    for j in range(6):
        print('*', end='')
    print()

******
******
******
******
******
******
******
******

#--------------------------------------------------------

for i in range(8):
    for j in range(i + 1):
        print('*', end='')
    print()
*
**
***
****
*****
******
*******
********

#--------------------------------------------------------------------------

n = int(input())
x = n // 2 + 1
for i in range(x):
    for j in range(i + 1):
        print('*', end = '')
    print()
for i in range(n // 2, 0, -1):
    for g in range(i):
        print('*', end = '')
    print()

3
*
**
*

5
*
**
***
**
*

#--------------------------------------------------------------------------

n = int(input())
for i in range(1, n + 1):
    for j in range(i):
        print(i, end = '')
    print()

5
1
22
333
4444
55555
#--------------------------------------------------------------------------

def get_powers(num):
    return num**2, num**3, num**4
a, b, c = get_powers(2)
print(a)
print(b)
print(c)

