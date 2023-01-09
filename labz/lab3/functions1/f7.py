def has_3(b):
    for i in range(1, len(b) - 1):
        if b[i] == 3 and (b[i] == b[i - 1] or b[i] == b[i + 1]):
            print('True') 
            exit()
    print('False')
a = list(map(int, input().split()))
has_3(a)