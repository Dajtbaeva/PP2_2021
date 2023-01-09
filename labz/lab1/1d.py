d, z = int(input()), input()
if z == 'k':
    p = input()
    res = "{:." + p + "f}"
    print(res.format(d / 1024))
elif z == 'b':
    print(d * 1024)