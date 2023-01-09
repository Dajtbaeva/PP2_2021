import os
a = input()
path = '.'
if os.path.exists(a):
    print('Exists')
    print('Filename is', os.path.basename(a))
    print('Directory name is', os.path.dirname(a))
else:
    print("There is no such file")

# C:\Users\AsemS\.vscode\pp2\labz\Lab6\builtin_functions
# Exists
# Filename is builtin_functions
# Directory name is C:\Users\AsemS\.vscode\pp2\labz\Lab6
