# Discs
put, res = [], []
for i in range(int(input())):
    s = input()
    if s[0] == '1':
        put.append(s[2:])
    else:
        res.append(put[0])
        put.pop(0)  
print(*res, end = ' ')