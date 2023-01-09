import json

with open('sample-data.json', 'r', encoding='utf8') as f:
    x = f.read()
d = json.loads(x)

print('Interface Status', '=' * 80, sep='\n')
print('DN', ' ' * 40, 'Description', ' ' * 2, 'Speed', ' ' * 4, 'MTU')
print('-' * 43, '-' * 13, '-' * 11, '-' * 4)
for j in range(len(d['imdata'])): # list of dicts
    for i in d['imdata'][j].values():
        if len(i['attributes']['dn'])  == 41: # one digit
            print(i['attributes']['dn'], ' ' * 15, i['attributes']['speed'], ' ' * 3, i['attributes']['mtu'])
        else:
            print(i['attributes']['dn'], ' ' * 14, i['attributes']['speed'], ' ' * 3, i['attributes']['mtu'])