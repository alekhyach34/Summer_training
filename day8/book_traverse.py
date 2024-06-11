def searchword(n,worfs,target):
    rows=len(grid)
    cols=len(grid[0])
    def backtrack(row,col,idx):
        if idx==len(target):
            return True
        if row<0 or col<0 or row>=rows or col>=cols or grid[row][col]!=target[idx]:
            return False
        temp=grid[row][col]
        grid[row][col]='2'        
        dorikindhi=(backtrack(row-1,col,idx+1) or backtrack(row+1,col,idx+1) or backtrack(row,col-1,idx+1) or backtrack(row,col+1,idx+1))        
        grid[row][col]=temp
        return dorikindhi
    for i in range(rows):
        for j in range(cols):
            if grid[i][j]==target[0]:
                if backtrack(i,j,0):
                    print("yes")
                    return
    print("no")   
n=int(input())
grid=[]
target="boook"
for i in range(n):
    a=input()
    grid.append(a)
grid=[list(row) for row in grid]
searchword(n,grid,target)