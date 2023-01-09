for i in range(int(input())):
    n = int(input())
    if n <= 10:
        print('Go to work!')
    elif 10 < n <= 25:
        print('You are weak')
    elif 25 < n <= 45:
        print('Okay, fine')
    elif n > 45:
        print('Burn! Burn! Burn Young!')