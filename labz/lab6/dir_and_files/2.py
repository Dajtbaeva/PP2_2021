import os
a = input()

print('Existence:', os.access(a, os.F_OK)) # Существование
print('Readable:', os.access(a, os.R_OK)) # Читаемость
print('Writable:', os.access(a, os.W_OK)) # Возможность записи
print('Executable:', os.access(a, os.X_OK)) # Возможность выполнения

# C:\Users\AsemS\.vscode\pp2\labz\Lab6\dir_and_files
# Existence: True
# Readable: True
# Writable: True
# Executable: True
