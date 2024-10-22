n = int(input()) #number of rows
m = int(input()) #number of columns
matrix = [[0]*m for _ in range(n)]

for i in range(n):
    for j in range(m):
        matrix[i][j] = input()

for unpacking in matrix:
    print(*unpacking)

for c in range(m):
    for r in range(n):
        print(matrix[r][c], end=' ')
    print()