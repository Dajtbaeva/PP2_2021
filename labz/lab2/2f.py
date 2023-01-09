# Compensations
d, maxi = dict(), 0
for i in range(int(input())):
    s, v = list(input().split())
    if s not in d:
        d[s] = int(v)
        if int(v) > maxi:
            maxi = int(v)
    else:
        d[s] += int(v)
        if d[s] > maxi:
            maxi = d[s]
res = sorted(d.keys())
for i in res:
    if maxi - d[i] == 0:
        print(i, 'is lucky!')
    else:
        print(i, 'has to receive', maxi - d[i], 'tenge')
