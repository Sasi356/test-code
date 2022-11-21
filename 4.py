def solve(matrix):
    n = len(matrix)
    left,top,right,bottom = n-1,n-1,0,0
    for i in range(n):
        for j in range(n):
            if matrix[i][j]==0:
                left = min(left,j)
                top = min(top,i)
                right = max(right,j)
                bottom = max(bottom,i)
    return [(top,left),(top,right),(bottom,left),(bottom,right)]
matrix = []
n = 256
for i in range(n):
    x = list(map(int,input().split()))
    matrix.append(x)
print(solve(matrix))
