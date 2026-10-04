
matrix=[[1,1,0],
   [1,0,1],
   [0,0,0],]


#reverse
for i in range(len(matrix)):
    matrix[i]=matrix[i][::-1]
#flipping
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j]==0:
            matrix[i][j]=1
        else:
            matrix[i][j]=0
print(matrix)


'''
input 
matrix=[[1,1,0],
   [1,0,1],
   [0,0,0],]



output:
   1+5+9+3+7=25 


'''
    
