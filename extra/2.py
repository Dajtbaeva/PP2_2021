a, b = list(map(int, input().split())), int(input())
print(*(list(map(lambda x: x ** 2 // b, a))))