# IS IT PALINDROME
# объявление функции
def is_palindrome(text):
    s = ''.join(c for c in text if c.isalpha())
    s = s.lower()
    if s == s[::-1]:
        return True
    else:
        return False
# считываем данные
txt = input()

# вызываем функцию
print(is_palindrome(txt))