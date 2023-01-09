def primes(a):
    res = []
    for i in a:
        flag = False
        for j in range(2, i):
            if i % j == 0: # has divisors
                flag = True
        if flag == False:
            res.append(i)
    print(*res)
primes(list(map(int, input().split())))