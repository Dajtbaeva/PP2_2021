import re

pattern = r'ab{2,3}'

if re.search(pattern, input()):
    print('Found a match!!!')
else:
    print('Not matched :(')

# ab -> Not matched :(
# aabbbbbccdshg -> Found a match!!!