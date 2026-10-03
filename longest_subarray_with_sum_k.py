n, k = map(int, input().split())
arr = list(map(int, input().split()))

maxLen = 0

for i in range(0, n):
    currSum = 0
    for j in range(i, n):
        currSum += arr[j]
        if currSum == k:
            maxLen = max(maxLen, j - i + 1)

print(maxLen)