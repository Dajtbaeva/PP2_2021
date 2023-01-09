besties, res, ans = ['Bauka', 'Nura', 'Jax', 'Adil'], dict(), dict()
for i in range(4):
    a = input().split()
    res[besties[i]] = a

for i in range(4):
    b = int(input())
    for i in res.values(): # list from Bauka
        maxi = []
        for j in i: # j = Italy
            kod = d1[j].lower()
            cost = d2[kod]["rate"] * b
            maxi.append(cost)
        ans[besties[i]] = max(maxi)

            
for i in ans.values():
    for j in i:
        print(j, end = ' ')
    print()
for k, v in res.items():
    print(k, v)