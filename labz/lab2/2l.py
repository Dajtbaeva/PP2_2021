# Open Closed
open = ['(', '[', '{']
close = [')', ']', '}']
def check(t):
    st = [] # stack
    for i in t:
        if i in open:
            st.append(i)
        elif i in close:
            pos = close.index(i)
            if len(st) != 0 and open[pos] == st[len(st) - 1]:
                st.pop()
            else:
                return 'No'
    if len(st) == 0:
        return 'Yes'
    else:
        return 'No' 
s = input()
print(check(s))