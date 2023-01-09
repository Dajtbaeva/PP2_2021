def kvadraty(a, b):
    for i in range(a, b):
        yield i ** 2

for j in kvadraty(int(input()), int(input()) + 1):
    print(j)