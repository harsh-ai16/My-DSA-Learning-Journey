
matrix = [
    [1, 2, 3],
    [5, 6, 7],
    [9, 10, 11]
]

row=len(matrix)
column=len(matrix[0])

# Some basic Operations in 2D list

# Upper Traingular Matrix
# for i in range(0,row):
#     for j in range(i,column):
#         print(matrix[i][j],end=" ")
#     print()
for i in range(0,row):
    for j in range(0,column):
        if j>=i:
            print(matrix[i][j],end=" ")
        else:
            print(" ",end=" ")
    print()

# Lower Triangular Matrix
# for i in range(0,row):
#     for j in range(0,i+1):
#         print(matrix[i][j],end=" ")
#     print()
for i in range(0,row):
    for j in range(0,column):
        if j<=i:
            print(matrix[i][j],end=" ")
        else:
            print(" ",end=" ")
    print()

# Diagonal Elements
for i in range(0,row):
    for j in range(0,column):
        if i==j:
            print(matrix[i][j],end=" ")
        else:
            print(" ",end=" ")
    print()

# Secondary Diagonal Elements
for i in range(0,row):
    for j in range(0,column):
            if i+j==2:
                print(matrix[i][j],end=" ")
            else:
                print(" ",end=" ")
    print()

# Transpose of Matrix
tr_matrix=[[0]*row for _ in range(column)]
for i in range(0,row):
    for j in range(0,column):
        tr_matrix[j][i]=matrix[i][j]
    
print(tr_matrix)