names = ['Bob', 'Alice', 'Guido']
for index, value in enumerate(names):
    print(f'{index}: {value}')

=========================
0: Bob
1: Alice
2: Guido
---------------------------------------------------
names = ['Bob', 'Alice', 'Guido']
for index, value in enumerate(names, 1):
    print(f'{index}: {value}')
==========================
1: Bob
2: Alice
3: Guido
