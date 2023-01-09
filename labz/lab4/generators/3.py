def res(n):
    for i in range(n):
        if i % 12 == 0:
            yield i
print(*res(int(input())))