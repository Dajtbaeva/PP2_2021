def has_3(b):
    for i in range(1, len(b) - 1):
        if b[i] == 3 and (b[i] == b[i - 1] or b[i] == b[i + 1]):
            return True
    return False

def spy_game(b):
    c = ''
    for i in b:
        if i == '0' or i == '7':
            c += i
    if '007' in c:
        return True
    else:
        return False

def is_prime(a):
        if a == 1: return False
        for i in range(2, a):
            if a % i == 0:
                return False
        return True