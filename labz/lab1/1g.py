# TO DECIMAL

def todec(a):
    deg, res = len(n) - 1, 0
    for i in n:
        res += int(i) * 2 ** deg
        deg -= 1
    return res
n = input()
print(todec(n))
<<<<<<< HEAD

=======
>>>>>>> b54f68d5b49c659f02c4d2ebce55a24eb869954c
"""
def todec(a, d, res, i):
    if d == -1:
        return res
    res += (ord(a[i]) - 48) * 2 ** d
    return todec(a, d - 1, res, i + 1)

n = input()
print(todec(n, len(n) - 1, 0, 0))
<<<<<<< HEAD
"""
=======
"""
>>>>>>> b54f68d5b49c659f02c4d2ebce55a24eb869954c
