'''# row * col -->6 l is input,location 4,6-->trees will burn from left right,top and bottom op:no.of unburned trees 
l=[[0,1,1,1,0,1],
   [0,1,0,1,0,0],
   [1,0,1,1,0,0],
   [0,0,0,1,1,1],
   [1,1,0,0,0,1],
   [1,1,1,0,1,0]]
#r,c=input(),input()'''
r=int(input())
c= int(input())
a=[]
matrix = []
print("Enter the entries rowwise:")
for i in range(r):
    a = []
    for j in range(c):
        a.append(int(input()))
    matrix.append(a)
for i in range(r):
    for j in range(c):
        print(matrix[i][j], end=" ")
    print()






























'''
def burn_trees(matrix, start_row, start_col):
    rows, cols = len(matrix), len(matrix[0])
    queue = [(start_row, start_col)]
    unburned_count = 0

    # Directions for neighboring trees
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while queue:
        row, col = queue.pop(0)  # Pop the front element
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < rows and 0 <= new_col < cols and matrix[new_row][new_col] == 0:
                # Mark neighboring unburned tree as burning
                matrix[new_row][new_col] = 1
                unburned_count -= 1
                queue.append((new_row, new_col))

    return unburned_count

# Given matrix l and specified location (4, 6)
start_row, start_col = 4, 6
result = burn_trees(l, start_row, start_col)
print(f"Number of unburned trees: {result}")
'''