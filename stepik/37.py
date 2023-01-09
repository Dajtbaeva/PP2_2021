# объявление функции
def convert_to_python_case(text):
    pass
    res = text[0].lower()
    for i in range(1, len(text)):
        if text[i].isupper() and i != 0:
            res += '_' + text[i].lower()
        else:
            res += text[i]
    return res
# считываем данные
txt = input()

# вызываем функцию
print(convert_to_python_case(txt))