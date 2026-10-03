a=list(map(int, input().split()))
b=list(map(int, input().split()))
ans=[]
i,j=0,0
while i<len(a) and j<len(b):
    if a[i]==b[j]:
        ans.append(a[i])
        i+=1
        j+=1
    elif a[i]<b[j]:
        i+=1
    else:
        j+=1
print(*ans)