import json

with open('a.json', 'r') as f:
    x = f.read()
    d = json.loads(x)

d['hobby'] = 'pp'