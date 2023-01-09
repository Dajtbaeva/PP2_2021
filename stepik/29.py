# Hod konem
from math import*
x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
if abs(x2 - x1) == 1 and abs(y2 - y1) == 2 or abs(x2 - x1) == 2 and abs(y2 - y1) == 1:
    print('YES')
else:
    print('NO')




