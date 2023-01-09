# String calculator
def con(a):
    ans = ''
    for i in range(len(a)):
        if a[i] == '1':
            ans += 'ONE'
        elif a[i] == '2':
            ans += 'TWO'
        elif a[i] == '3':
            ans += 'THR'
        elif a[i] == '4':
            ans += 'FOU'
        elif a[i] == '5':
            ans += 'FIV'
        elif a[i] == '6':
            ans += 'SIX'
        elif a[i] == '7':
            ans += 'SEV'
        elif a[i] == '8':
            ans += 'EIG'
        elif a[i] == '9':
            ans += 'NIN'
        elif a[i] == '0':
            ans += 'ZER'
    return ans

def dig(t):
    ans = ''
    for i in range(0, len(t), 3):
        if t[i : i + 3] == 'ONE':
            ans += '1'
        elif t[i : i + 3] == 'TWO':
            ans += '2'
        elif t[i : i + 3] == 'THR':
            ans += '3'
        elif t[i : i + 3] == 'FOU':
            ans += '4'
        elif t[i : i + 3] == 'FIV':
            ans += '5'
        elif t[i : i + 3] == 'SIX':
            ans += '6'
        elif t[i : i + 3] == 'SEV':
            ans += '7'
        elif t[i : i + 3] == 'EIG':
            ans += '8'
        elif t[i : i + 3] == 'NIN':
            ans += '9'
        elif t[i : i + 3] == 'ZER':
            ans += '0'
    return int(ans)
a, b = input().split('+')
res = dig(a) + dig(b)
print(con(str(res)))
