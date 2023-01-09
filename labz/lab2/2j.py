# Boris and Passwords
ans = []
for i in range(int(input())):
    s = input()
    u, l, res = s.upper(), s.lower(), False
    if s != u and s != l:
        for j in range(len(s)):
            if 47 < ord(s[j]) < 58:
                res = True
        if res == True:
            ans.append(s)
a = set(ans)
print(len(a))
print(*sorted(a), sep = '\n')