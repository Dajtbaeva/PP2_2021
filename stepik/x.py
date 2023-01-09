a, b = int(input()), int(input())
maxi = 0
sumi = 0
res = 0
for i in range(a, b + 1):
    for j in range(1, i + 1):
        if i % j == 0:
            sumi += j
    if sumi >= maxi:
        maxi = sumi
        res = i
    sumi = 0
print(res, maxi)
