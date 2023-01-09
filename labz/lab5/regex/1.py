import re

pattern = r'^a(b*)$'

if re.search(pattern, input()):
    print('Found a match!!!')
else:
    print('Not matched :(')

# abc -> Not matched :(
# a, abb -> Found a match!!!