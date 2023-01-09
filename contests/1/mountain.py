# t can be created if and only if: 1)length of array >= 3 
# 2)There exist some index i on what we can say that arr[0] < arr[1] < arr[2] < ... 
# < arr[i] > arr[i + 1] > arr[i + 2] > ... arr[n - 1]

# 1 2 3 4 5 4 3 2 1 -> Yes
# 2 1 -> No

a = list(map(int, input().split()))
if len(a) < 3:
    print('No')
    exit()
for i in range(len(a) - 2):
    if a[i] < a[i + 1] and a[i + 1] > a[i + 2]:
        print('Yes')
        exit()
print('No')