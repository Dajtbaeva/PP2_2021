n = int(input())
d = {}
d['a'] = d['b'] = d['c'] = 0

for _ in range(n):
    words = list(map(str, input().split()))
    for i in range(len(words)):
        for j in range(len(words[i])):
            if words[i][j] in 'QWERTYUIOPASDFGHJKLZXCVBNM' and i == 0:
                d['a'] += 1
            elif words[i][j] in 'aeiou' and i == 1:
                d['b'] += 1
            elif words[i][j].isdigit() and i == 2:
                d['c'] += 1
print(*d.values())
# Input:
# 2
# SDIUFhhjskdfhkdsJHDF asohufduasidufSHKFHhkflda adsljfh981319yhjaf89123
# DFSHUjsdif132h13hi ahdsjfhahraiiieay123123 ahsfdha3j2h23hjhzfsASHDL

# Output:
# The number of Capital letters in first words (QWERTYUIOPASDFGHJKLZXCVBNM)
# The number of lowercase vowels in second words (aeiou)
# The number of digits in third words (1234567890)

# 14 16 15