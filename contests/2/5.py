def resi(t):
    num, b, st = 0, 0, []
    for i in t:
        if i == '(':
            st.append(i)
        elif i == ')' and len(st) != 0:
            if len(st) == 1:
                num += 1
            else:
                num += 3 ** (len(st) - 1)
            st.clear()
    return num
s = input()
print(resi(s))