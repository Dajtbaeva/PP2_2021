# Demon slayer
d1, d2, ans = dict(), dict(), 0
for i in range(int(input())):
    d, w = list(input().split())
    if w not in d1:
        d1[w] = 1
    else:
        d1[w] += 1
for j in range(int(input())):
    h, a, k = list(input().split())
    if a not in d2:
        d2[a] = int(k)
    else:
        d2[a] += int(k)
for l in d1:
    if l in d2:
        d1[l] = d1[l] - d2[l]
    if d1[l] > 0:
        ans += d1[l]    
print('Demons left:', ans)
