def spy_game(b):
    c = ''
    for i in b:
        if i == '0' or i == '7':
            c += i
    if '007' in c:
        print('True')
    else:
        print('False')
a = list(input().split())
spy_game(a)
