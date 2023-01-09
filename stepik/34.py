# Быстрое слияние двух отсортированных списков в один
def quick_merge(list1, list2):
    result = []

    p1 = 0  # указатель на первый элемент списка list1
    p2 = 0  # указатель на первый элемент списка list2

    while p1 < len(list1) and p2 < len(list2):  # пока не закончился хотя бы один список
        if list1[p1] <= list2[p2]:
            result.append(list1[p1])
            p1 += 1
        else:
            result.append(list2[p2])
            p2 += 1

    if p1 < len(list1):   # прицепление остатка
        result += list1[p1:]
    if p2 < len(list2):
        result += list2[p2:]
    
    return result
list1 = [3, 10, 11, 12, 47, 57, 58, 63, 77, 79, 80, 95]
list2 = [0, 11, 12, 20, 24, 26, 47, 48, 53, 65, 70, 81, 84, 84, 90]
list3 = quick_merge(list1, list2)
print(list3)
# [0, 3, 10, 11, 11, 12, 12, 20, 24, 26, 47, 47, 48, 53, 57, 58, 63, 65, 
# 70, 77, 79, 80, 81, 84, 84, 90, 95]
===========================================================================
def merge(list1, list2):
    pass
    res = list1 + list2
    res.sort()
    return res
res = []
for i in range(int(input())):
    s = [int(a) for a in input().split()]
    res = merge(res, s)
print(*res)
================================================================================
# NEXT PRIME NUMBER
def is_prime(num):
    pass
    if num == 1:
        return False
        return 0
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def get_next_prime(num):
    pass
    x = num + 1
    while is_prime(x) == False:
        x += 1
    return x
# считываем данные
n = int(input())

# вызываем функцию
print(get_next_prime(n))
