roman_n = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,
            'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
def roma(t):
    i, res = 0, 0
    while i < len(t):
        if t[i : i + 2] in roman_n and i < len(t):
            res += roman_n[t[i : i + 2]]
            i += 2
        else:
            res += roman_n[t[i]]
            i += 1
    return res
s = input()
print(roma(s))