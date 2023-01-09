# Наибольшие числа 
n = int(input())
maxi, prev = 0, 0
for i in range(n):
    a = int(input())
    if a > maxi:
        prev = maxi
        maxi = a
    else:
        if prev < a < maxi:
            prev = a
print(maxi)
print(prev)
