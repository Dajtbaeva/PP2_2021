BY KEYS
>>> d = {'a': 10, 'b': 15, 'c': 4}
>>> list_keys = list(d.keys())
>>> list_keys.sort()
>>> for i in list_keys:
...     print(i, ':', d[i])
... 
a : 10
b : 15
c : 4
--------------------------------------------------------
print(*sorted(mydict.items()), sep='\n')
('2', 34)
('audi', 100)
('bmw', 39)
('mers', 124)
--------------------------------------------------------------
BY VALUES
>>> d = {'a': 10, 'b': 15, 'c': 4}
>>> list_d = list(d.items())
>>> list_d
[('a', 10), ('b', 15), ('c', 4)]
>>> list_d.sort(key=lambda i: i[1])
>>> list_d
[('c', 4), ('a', 10), ('b', 15)]
>>> for i in list_d:
...     print(i[0], ':', i[1])
... 
c : 4
a : 10
b : 15
-------------------------------------------------------------
#sorted(collection, key, reverse=True/False)
ls = []
n = int(input())
for _ in range(n):
    name, last_name, age = input().split()
    ls.append((name, last_name, int(age)))
for name, last_name, age in sorted(ls):
    print(name, last_name, age)
--------------------------------------------------------------------
#sorted(collection, key, reverse=True/False)
ls = []
n = int(input())
for _ in range(n):
    name, last_name, age = input().split()
    ls.append((name, last_name, int(age)))
for name, last_name, age in sorted(ls, key = lambda x: (x[2], x[1], x[0])):
    print(name, last_name, age)