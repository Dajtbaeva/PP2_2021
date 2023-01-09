# Zigzag
def zigi(t, k):
    if k == 1:
        print(t)
        exit()
    a, j = ['' for i in range(len(t))], 0
    for i in range(len(t)):
        a[j] += t[i]
        if j == k - 1:
            dir = False
        elif j == 0:
            dir = True
        if dir == True:
            j += 1
        else:
            j -= 1
    res = ''.join(a)
    print(res)
s, n = input(), int(input())
zigi(s, n)