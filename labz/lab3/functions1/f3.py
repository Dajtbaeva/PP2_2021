def puzzle(h, l):
    chickens, rabbits = 0, 0
    if h >= l or l % 2 != 0:
        return 'No solution'
        exit()
    else:
        rabbits = (l - h * 2) / 2
        chickens = h - rabbits
        return int(chickens), int(rabbits)
# heads, tails = map(int, input().split())
# print(puzzle(heads, tails))
print(puzzle(35, 94))
# 35, 94 -> 23, 12 
# 38, 131 -> No solution 
# 116, 282 -> 91, 25