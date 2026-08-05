''' Set Matrix Zero's '''

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
                    
# Brute force approach 

                
        
        