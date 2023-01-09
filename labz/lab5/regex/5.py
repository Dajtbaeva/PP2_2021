import re

pattern = r'.*a+.*b$' 

if re.search(pattern, input()):
    print('Valid')
else:
    print('Not valid')

# aabAbbbc -> Not valid
# acnjflb -> Valid
