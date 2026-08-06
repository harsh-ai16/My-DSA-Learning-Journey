''' Set Matrix Zero's '''

matrix = [
    [5, 1, 0, 4],
    [2, 3, 7, 8],
    [9, 0, 6, 1],
    [4, 5, 2, 0]
]
rows=len(matrix)
column=len(matrix[0])

# Optimal Approach 
class Solution(object):
    def setZeroes(self, matrix):
        row=len(matrix)
        column=len(matrix[0])
        rowtrack=[0]*row
        columntrack=[0]*column
        for i in range(row):
            for j in range(column):
                if matrix[i][j]==0:
                    rowtrack[i]=-1
                    columntrack[j]=-1
        
        for i in range(row):
            for j in range(column):
                if rowtrack[i]==-1 or columntrack[j]==-1:
                    matrix[i][j]=0
# Time complexity is O(N*M) and space complexity is O(N+M) :. N,M are rows, columns
                    
# Brute force approach 
def infinity(r,c):

    for i in range(rows):
        if matrix[i][c]!=0:
            matrix[i][c]=float("inf")

    for j in range(column):
            if matrix[r][j]!=0:
                matrix[r][j]=float("inf")

def getzero(matrix):
    for i in range(rows):
        for j in range(column):
            if matrix[i][j]==0:
                infinity(i,j)
getzero(matrix)

for i in range(rows):
    for j in range(column):
        if matrix[i][j]==float("inf"):
            matrix[i][j]=0
print(matrix)

# Time complexity is O( (N*M)*(N+M)+(N*M) ) Space complexity is O(1)



                
        
        