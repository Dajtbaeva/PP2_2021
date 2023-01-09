import re
s = input()
pattern = r'(?P<nuzhno>[A-Z][a-z]+)' 
 
if re.search(pattern, s) != None:
    print(re.findall(pattern, s))
else:
    print('Ne naideno')

# isPython -> ['Python']
# AdFhAh -> ['Ad', 'Fh', 'Ah']