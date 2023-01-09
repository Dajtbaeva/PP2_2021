import os
path = r'C:\Users\AsemS\.vscode\pp2\labz'
print("Only directories:", [imya for imya in os.listdir(path) if os.path.isdir(os.path.join(path, imya))])
print("Only files:")
print([imya for imya in os.listdir(path) if os.path.isfile(os.path.join(path, imya))])
print("All directories and files:")
print([imya for imya in os.listdir(path)])

# Only directories: ['.git', 'Lab1', 'Lab2', 'Lab3', 'Lab4', 'Lab5', 'Lab6']
# Only files:
# ['README.md']
# All directories and files:
# ['.git', 'Lab1', 'Lab2', 'Lab3', 'Lab4', 'Lab5', 'Lab6', 'README.md']