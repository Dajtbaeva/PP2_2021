# Все вместе
n = int(input())
sumi, cnt, product, arif, sum2 = 0, 0, 1, 0, 0
last = n % 10
while n != 0:
    a = n % 10
    sumi += a
    cnt += 1
    product *= a
    first = n
    n //= 10
arif = sumi / cnt
sum2 = first + last
print(sumi)
print(cnt)
print(product)
print(arif)
print(first)
print(sum2)