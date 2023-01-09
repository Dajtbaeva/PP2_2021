import json

with open('country-currency.json', 'r', encoding='utf8') as f:
    x = f.read()
    d1 = json.loads(x)


with open('usd.json', 'r', encoding='utf8') as f:
    y = f.read()
    d2 = json.loads(y)

besties, res, ans, ans2 = ['Bauka', 'Nura', 'Jax', 'Adil'], dict(), dict(), dict()
for i in range(4):
    a = input().split()
    res[besties[i]] = a

l = 0
for k in res.values(): # list from Bauka
    b = int(input())
    maxi, coun, val = [], [], []
    for j in k: # j = Italy
        kod = d1[j].lower()
        cost = d2[kod]["rate"] * b
        money = d2[kod]["name"].lower() + 's'
        maxi.append(cost)
        coun.append(j)
        val.append(money)
    ans[besties[l]] = int(max(maxi))
    pos = maxi.index(max(maxi))
    ans2[coun[pos]] = val[pos]
    # print(besties[l], 'goes to', coun[pos], 'with', ans[besties[l]], val[pos])
    l += 1
n = 0
for k, v in ans2.items():
    print(besties[n], 'goes to', k, 'with', ans[besties[n]], v)
    n += 1