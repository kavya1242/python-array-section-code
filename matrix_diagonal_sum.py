matrix=[[1,2,3],
   [4,5,6],
   [7,8,9],]
sum=0

for i in range(len(matrix)):
    sum+=matrix[i][i]
for i in range(len(matrix)):
        j=len(matrix[0])-i-1
        if i!=j:
             sum+=matrix[i][j]
print(sum)
'''
input 
a=[[1,2,3],
   [4,5,6],
   [7,8,9]]
output:
   1+5+9+3+7=25

'''
