s = input()
t = ''.join(reversed(s))
print('Palindrome!') if s == t else print('Not palindrome :(')