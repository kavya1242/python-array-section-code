a=[[1,2,3],
   [4,5,6],
   [7,8,9]]
m=len(a)
k=[[0]*m for i in range(m)]
for i in range(m):
    for j in range(m):
        k[j][m-i-1]=a[i][j]
print(k)
