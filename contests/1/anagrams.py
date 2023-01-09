# Anagrams
strings = input().split()
res = dict()

for w in strings:
    sorted_w = ''.join(sorted(w))
    if sorted_w not in res:
        res[sorted_w]=[w]
    else:
        res[sorted_w].append(w)
print(list(res.values()))
# code mode odec odem oemd doce some does mose
# [['code', 'odec', 'doce'], ['mode', 'odem', 'oemd'], ['some', 'mose'], ['does']]
