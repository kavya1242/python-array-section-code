N=int(input())
arr=list(map(int, input().split()))
smallest = min(arr)
for i in range(smallest, 0, -1):
    is_gcd = True
    for num in arr:
        if num % i != 0:
            is_gcd = False
            break
    if is_gcd:
        print(i)
        break