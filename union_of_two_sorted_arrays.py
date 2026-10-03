a = list(map(int, input().split()))
b = list(map(int, input().split()))
s=set()
for num in a:
    s.add(num)
for num in b:
    s.add(num)
print(sorted(s))