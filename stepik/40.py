# Шифр Цезаря
# y=(x+k) mod n, x=(y−k) mod n: xx — символ открытого текста, yy — символ шифрованного текста, 
# nn — мощность алфавита (количество символов), а kk — ключ. для английского языка возможны 25 
# разных преобразований (преобразования ROT 0 и ROT 26 сохраняют исходный текст, а дальше начинаются 
# уже повторения) https://planetcalc.ru/1434/
# put your python code here
def sdvig(symb, num):
    abc = 'abcdefghijklmnopqrstuvwxyz'
    symb_index = abc.find(symb.lower())
    if symb_index + num > 25:
        if symb.lower() == symb:
            return abc[symb_index + num - 26]
        else:
            return abc[symb_index + num - 26].upper()
    else:
        if symb.lower() == symb:
            return abc[symb_index + num]
        else:
            return abc[symb_index + num].upper()

s, res = input().split(), []
for i in range(len(s)):
    cnt, a = 0, ''
    for j in range(len(s[i])):
        if s[i][j].isalpha():
            cnt += 1
    for j in range(len(s[i])):
        if s[i][j].isalpha():
            a += sdvig(s[i][j], cnt)
        else:
            a += s[i][j]
    res.append(a)
print(*res)           

