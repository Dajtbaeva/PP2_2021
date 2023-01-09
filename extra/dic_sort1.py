d = [
    {
        'surname': 'Zhapar',
        'id': '19B030307'
    },
    {
        'surname': 'Ashim',
        'id': '19B030307'
    },
    {
        'surname': 'Ernat',
        'id': '21B21893040'
    }
]

# print(*sorted(d, key=lambda x: x['id'][:3]))
print(*sorted(d, key=lambda x: (x['id'][:3], x['surname'])))
print(type(d))




# Closest point
from math import *

global xi, yi
def funi(z):
    return sqrt((z[0] - xi) ** 2 + (z[1] - yi) ** 2)

xi, yi = map(int, input().split())
res = []
for i in range(int(input())):
    x, y = map(int, input().split())
    tup = tuple((x, y))
    res.append(tup)
res.sort(key = funi) # like a comp
for j in res:
    print(*j)