s = input()
dic = dict()
for i in s:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1
        
res = sorted(dic.items(), key = lambda x: -x[1])
for k, v in res:
    print(k * v, end = '')