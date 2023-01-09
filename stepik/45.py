# Панграмма – это фраза, содержащая в себе все буквы алфавита
def is_pangram(text):
    pass
    a = text.lower().replace(' ', '')
    if len(set(a)) == 26:
        return True
    else:
        return False
# считываем данные
text = input()

# вызываем функцию
print(is_pangram(text))