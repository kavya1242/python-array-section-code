# Sample input array
arr = list(map(int, input().split()))


if not arr:
    res = []
else:
    n = len(arr)
    res = []
    
    # The rightmost element is always dominant
    max_right = arr[-1]
    res.append(max_right)
    
    # Traverse from right to left
    for i in range(n - 2, -1, -1):
        if arr[i] >= max_right:
            max_right = arr[i]
            res.append(arr[i])
            
    # Reverse to get original left-to-right order
    res.reverse()

print("Dominant Elements:", res)
'''
input:
5 4 3 2 1
output:
5 4 3 2 1'''
