board=[
    [0,0,0,1,],
    [1,0, 0, 1,],
    [1,1, 1, 0,],
    [0,0, 0, 0,]]
m,n=len(board),len(board[0])
newboard=[[0]*n for i in range(m)]
for i in range(m):
    for j in range(n):
        live=0
        cell=board[i][j]
        directions = [(-1,0), (1,0), (0,-1), (0,1), (-1,-1), (-1,1), (1,-1), (1,1)]
                
        for dr, dc in directions:
            ni, nj = i + dr, j + dc
            if(0 <= ni < m and 0 <= nj < n):
                live += board[ni][nj]

        if cell==1:
            if live<2 or live>3:
                newboard[i][j]=0
            else:
                newboard[i][j]=1
        elif cell==0:
            if live==3:
                newboard[i][j]=1
print(newboard)



