s, sumi = input(), 0
for i in range(len(s)):
    sumi += int(ord(s[i]))
if sumi > 300:
    print('It is tasty!')
else:
    print('Oh, no!')


