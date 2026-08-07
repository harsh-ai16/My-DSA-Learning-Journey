""" Roatate the matrix by 90 degree """

matrix = [
    [5, 1, 9, 11],
    [2, 4, 8, 10],
    [13, 3, 6, 7],
    [15, 14, 12, 16]
]
row=len(matrix)
column=len(matrix[0])

# Brute force approach using storage 
tr_matrix=[[0]*row for _ in range(column)]
for i in range(row):
    for j in range(column):
        tr_matrix[j][row-1-i]=matrix[i][j]
print(tr_matrix)
# Time complexity is O( N² ) and Space complexity is O(N)

# Optimal approach without using extra space
# using transpose and reversing list
for i in range(row):
    for j in range(i+1,column):
        matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]

for i in range(0,row):
    matrix[i].reverse()
print(matrix)
# Time complexitry is O(N²) and space  complecity is O(1)



    