import itertools  
def permut(s): 
    perm = set(itertools.permutations(s)) 
    for i in perm: 
        print(*i, sep='') 
permut(input())

# global ans
# ans = set()
# def permut(t, i, e):
#     if i == e:
#         res = ''.join(t)
#         ans.add(res)
#     else:
#         for j in range(i, e + 1):
#             t[i], t[j] = t[j], t[i]
#             permut(t, i + 1, e)
#             t[i], t[j] = t[j], t[i] # backtrack
# s = list(input())
# l = len(s)
# permut(s, 0, l - 1) # list, init ind, ending ind
# print(*ans)
