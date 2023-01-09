import os
with open('4.txt', 'r', encoding='utf8') as f:
    x = sum([1 for i in f])
print(f'The number of lines in a text file is {x}')
# The number of lines in a text file is 4