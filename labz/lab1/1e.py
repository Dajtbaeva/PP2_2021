def isprime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
            break
    return True

a, b = map(int, input().split())
if a < 500 and isprime(a) == True and b % 2 == 0:
    print('Good job!')
else:
    print('Try next time!')