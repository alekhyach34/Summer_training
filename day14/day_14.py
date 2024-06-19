# -*- coding: utf-8 -*-
"""day_14.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1DxRMJLlca27Lgc-aaAoAESUki72yPstQ
"""

n=[2,5,2,3,6,7,1,0,5]
n1=[2,5,5,5,6,7,7,7]
l = [0] * len(n)
r= [0]*len(n)
m=0
m1=0
s=0
for i in range(len(n)):
  if n[i]>m:
    m=n[i]
  l[i]=m
for i in range(len(n)-1,-1,-1):
  if n[i]>m1:
    m1=n[i]
  r[i]=m1
for i in range(len(n)):
  # Calculate the minimum of l[i] and r[i], then subtract n[i], and finally take the absolute value
  s=s+(abs(min(l[i],r[i]) - n[i]))
print(s)

a=[1,3,4,5]
l=[0]*17
l1=[]
for i in range(len(a)):
  for j in range(len(l1)):
    if a[i]<l1[j]:
      l1[j]=a[i]
    if a[i]>l1[j]:
      l.append((a[i]-l1[j])+1)
print(set(l))
print(l)

a = [1, 3, 4, 5]
for i in range(len(a)):
    l = []
    for j in range(18):
        l.append(a[i]*0)
    #print(l)
l1=[0,1,2,3,4,5,6,7,8,9,]
#l=[0][0]*17
for i in range(len(a)):
  for j in range(len(l1)):
    if a[i]>l1[j]:
      l[j]=a[i]
    if a[i]<l1[j]:
      l.append((a[i]-l1[j])+1)
print(set(l))

s1=[1, 3, 4, 5]
s2=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
m=[]
l=[]
u=len(s1)
v=len(s2)
s=0
for i in range(u+1):
  l=[0]*(v+1)
  m.append(l)
for i in range(1,u+1):
  for j in range(1,v+1):
    if s1[i-1]==s2[j-1]:
      m[i][j]=m[i-1][j-1]+1
    else:
      m[i][j]=max(m[i][j-1],m[i-1][j])
print(m[len(s1)][len(s2)])
while u!=0 and v!=0:
    if(s1[u-1]==s2[v-1]):
        s=s+s1[u-1]
        u=u-1
        v=v-1
    else:
        if(m[u][v]==m[u-1][v]):
            u=u-1
        else:
            v=v-1
s=s[::-1]
print(s)



s1=[3, 4, 7]
s2=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
m=[]
l=[]
u=len(s1)
v=len(s2)
m=[]
s=[] # Initialize s as a list to store matching elements
for i in range(u+1):
  l=[0]*(v+1)
  m.append(l)
for i in range(1,u+1):
  for j in range(1,v+1):
    if s1[i-1]==s2[j-1]:
      m[i][j]=m[i-1][j-1]+1
    else:
      m[i][j]=max(m[i][j-1],m[i-1][j])
print(m[len(s1)][len(s2)])
while u!=0 and v!=0:
    if(s1[u-1]==s2[v-1]):
        s.append(s1[u-1]) # Append matching element to s
        u=u-1
        v=v-1
    else:
        if(m[u][v]==m[u-1][v]):
            u=u-1
        else:
            v=v-1
s = s[::-1] # Now you can reverse the list s
print(s)

s1=[1, 3, 4, 5]
m[0][0]=s1[0]
m[1][1]=s1[1]
m[2][1]=s1[2]
m[3][1]=s1[3]
print(m)

#coins
def fun():
    l1=[-1]*(n+1)
    l1[0]=0
    for i in l:
        for j in range(1,n+1):
            if j>=i:
                if l1[j-i]!=-1:
                    if l1[j]!=-1:
                        l1[j]=min(l1[j],l1[j-i]+1)
                    else:
                        l1[j]=l1[j-i]+1
    print(l1[-1])
l=[1,3,4,5]
n=17
fun()

#Using Recursion Finding Paths
def path(n,m):
  if n==0 or m==0:
      return 0
  if n==1 and m==1:
    return 1
  return path(n-1,m)+path(n,m-1)
n=int(input())
m=int(input())
path(n,m)
#dynamic

def find_paths(matrix, i, j, path, paths):
    if i == len(matrix) - 1 and j == len(matrix[0]) - 1:
        paths.append(path + [(i, j)])
        return
    if i < len(matrix) - 1:
        find_paths(matrix, i + 1, j, path + [(i, j)], paths)
    if j < len(matrix[0]) - 1:
        find_paths(matrix, i, j + 1, path + [(i, j)], paths)

n = int(input())
m = int(input())
matrix = [[0]*m for _ in range(n)]
paths = []
find_paths(matrix, 0, 0, [], paths)

for path in paths:
    print(path)

def count_paths(n, m, i, j):
    if i == n - 1 and j == m - 1:
        return 1
    if i >= n or j >= m:
        return 0
    return count_paths(n, m, i + 1, j) + count_paths(n, m, i, j + 1)

n = int(input())
m = int(input())
number_of_paths = count_paths(n, m, 0, 0)

print(number_of_paths)

def count_paths_dp(n, m):
    dp = [[0]*m for _ in range(n)]
    for i in range(n):
        dp[i][0] = 1
    for j in range(m):
        dp[0][j] = 1
    for i in range(1, n):
        for j in range(1, m):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[n-1][m-1]

n = int(input())
m = int(input())
number_of_paths = count_paths_dp(n, m)

print(number_of_paths)

def is_valid(x, y, n, m, visited):
    return 0 <= x < n and 0 <= y < m and not visited[x][y]
def find_all_paths(x, y, n, m, visited, path, paths):
    if x == n - 1 and y == m - 1:
        paths.append(path + [(x, y)])
        return
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
    visited[x][y] = True
    for dx, dy in directions:
        new_x, new_y = x + dx, y + dy
        if is_valid(new_x, new_y, n, m, visited):
            find_all_paths(new_x, new_y, n, m, visited, path + [(x, y)], paths)
    visited[x][y] = False
n = 4
m = 3
visited = [[False]*m for _ in range(n)]
paths = []
find_all_paths(0, 0, n, m, visited, [], paths)
print(len(paths))

def is_valid(x, y, n, m, visited):
    return 0 <= x < n and 0 <= y < m and not visited[x][y]

def find_all_paths(x, y, n, m, visited, path, paths):
    if x == n - 1 and y == m - 1:
        paths.append(path + [(x, y)])
        return
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
    visited[x][y] = True
    for dx, dy in directions:
        new_x, new_y = x + dx, y + dy
        if is_valid(new_x, new_y, n, m, visited):
            find_all_paths(new_x, new_y, n, m, visited, path + [(x, y)], paths)
    visited[x][y] = False

n = 4
m = 3
visited = [[False]*m for _ in range(n)]
paths = []
find_all_paths(0, 0, n, m, visited, [], paths)

print(f"There are {len(paths)} paths. they are:")
for path in paths:
    print(path)

def unique_paths_with_paths(m, n):
    def dfs(x, y, visited, path, all_paths):
        if x == m - 1 and y == n - 1:
            all_paths.append(path[:])  # Add a copy of the current path
            return

        visited.add((x, y))

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited:
                path.append((nx, ny))
                dfs(nx, ny, visited, path, all_paths)
                path.pop()  # Backtrack

        visited.remove((x, y))

    if m == 0 or n == 0:
        return 0, []

    all_paths = []
    dfs(0, 0, set(), [(0, 0)], all_paths)

    return len(all_paths), all_paths

# Example usage:
num_paths, paths = unique_paths_with_paths(2,3)
print(f"Number of unique paths: {num_paths}")
print("Paths:")
for path in paths:
    print(path)

def fun(i,j,c):
    if(i>0 or i>=n or j<0 or j>=m):
        return
    if(i==m-1 and j==n-1):
        c=c+1
        return c
    vi.append((i,j))
    if((i-1,j) not in vi):
        fun(i-1,j,c)
    if((i,j-1) not in vi):
        fun(i,j-1,c)
    if((i+1,j) not in vi):
        fun(i+1,j,c)
    if((i,j+1) not in vi):
        fun(i,j+1,c)
    vi.pop()
    return c
n=4
m=3
vi=[]
print(fun(0,0,0))

def fun(i,j,c):
    if(i<0 or i>=n or j<0 or j>=m): # Fixed the base case condition
        return 0 # Return 0 when out of bounds
    if(i==n-1 and j==m-1):
        return c+1 # Increment count when destination is reached
    vi.append((i,j))
    c = fun(i-1,j,c) # Assign the return value of recursive calls to c
    c = fun(i,j-1,c)
    c = fun(i+1,j,c)
    c = fun(i,j+1,c)
    vi.pop()
    return c
n=4
m=3
vi=[]
print(fun(0,0,0))

print("\nAll possible paths")
def fun(i,j,c):
    if(i<0 or i>=n or j<0 or j>=m): # Fixed the base case condition
        return 0 # Return 0 when out of bounds
    if(i==n-1 and j==m-1):
        return c+1 # Increment count when destination is reached
    if (i,j) in vi: # Check if current cell has been visited
        return 0 # Return 0 if already visited
    vi.append((i,j))
    c += fun(i-1,j,0) # Accumulate the count from recursive calls
    c += fun(i,j-1,0)
    c += fun(i+1,j,0)
    c += fun(i,j+1,0)
    vi.pop()
    return c # Return the total count

n=4
m=3
k=1
l=2
vi=[]
print(fun(0,0,0))
print("\nWhen Obstacle at (1,2) position, the possible paths are:")
def fun(i,j,c):
    if(i<0 or i>=n or j<0 or j>=m or(i==k and j==k)): # Fixed the base case condition
        return 0 # Return 0 when out of bounds
    if(i==n-1 and j==m-1):
        return c+1 # Increment count when destination is reached
    if (i,j) in vi: # Check if current cell has been visited
        return 0 # Return 0 if already visited
    vi.append((i,j))
    c += fun(i-1,j,0) # Accumulate the count from recursive calls
    c += fun(i,j-1,0)
    c += fun(i+1,j,0)
    c += fun(i,j+1,0)
    vi.pop()
    return c # Return the total count

n=4
m=3
k=1
l=2
vi=[]
print(fun(0,0,0))

def print_board(board):
    for row in board:
        print(" ".join(row))
    print("\n")

def is_safe(board, row, col):
    N = len(board)
    # Check row on left side
    for i in range(col):
        if board[row][i] == 'Q':
            return False
    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False
    # Check lower diagonal on left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False
    return True
def solve_n_queens_util(board, col):
    N = len(board)
    if col >= N:
        return True
    for i in range(N):
        if is_safe(board, i, col):
            board[i][col] = 'Q'
            if solve_n_queens_util(board, col + 1):
                return True
            board[i][col] = '_'  # Backtrack
    return False
def solve_n_queens(N):
    board = [['_' for _ in range(N)] for _ in range(N)]
    if not solve_n_queens_util(board, 0):
        print("Solution does not exist")
        return False
    print_board(board)
    #return True
N = 6
solve_n_queens(N)

'''_ _ _ _ Q R
   Q _ _ _ _ _
   _ _ _ _ Q -
   _ Q _ _ _ _
   _ _ _ _ _ Q
   _ _ Q _ _ _   for this do code as rooke-R will kill queens in its vertical and horizontal position, then find the maximum number of queens can be placed'''