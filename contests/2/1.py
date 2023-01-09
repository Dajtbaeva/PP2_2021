from math import *
n, p = list(input().split())
p1 = int(p)
res = 0
for i in n:
    res += int(i) ** p1
    p1 += 1
ans = res // int(n)
if ans * int(n) == res:
    print(ans)
else:
    print(-1)