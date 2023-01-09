s = input()
a = sum([1 for i in s if i.islower()])
b = sum([1 for k in s if k.isupper()])

print(f'Yhe number of lowercase letters is {a} and the number of upper case letters is {b}')