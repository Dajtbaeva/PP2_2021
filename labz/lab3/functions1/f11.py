def pali(b):
    b = b.strip('.?!,;:" "')
    t = b.replace(' ', '')
    p = t[::-1]
    print(p)
    if p == t:
        print('Palindrome')
    else:
        print('Not polindrome')
a = input()
pali(a.lower())
# Was it a car or a cat I saw? -> wasitacaroracatisaw = Palindrome