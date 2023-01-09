import json

with open('a.json', 'r') as f:
    x = f.read()
    d = json.loads(x)

# f = open('a.json','r')
# temp = f.read()

d['myName'] = 'Darina'
d['nums'].sort()
d['heroes']['spider-man'] = 'Tom'
for k, v in d.items():
    print(k, v)

y = json.dumps(d, indent=4)
with open('res.json', 'w') as f:
    f.write(y)

