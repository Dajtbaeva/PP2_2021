# TO DECIMAL
def unsyscode(num, n=2):
    count, result = len(num)-1, 0
    for i in num:
        result += int(i) * n ** count
        count -= 1
    return result

num = input()
print(unsyscode(num))