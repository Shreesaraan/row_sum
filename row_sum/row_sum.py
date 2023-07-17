def row_sum(rows,columns,matrix):
    sum=[]
    for i in range(rows):
        add=0
        for j in range(columns):
            add+=matrix[i][j]
        sum.append(add)
    return sum

matrix=[]
rows=int(input("Number of rows : "))
columns=int(input("Number of columns : "))
for i in range(rows):
    matrix.append(list(map(int,input().split())))
print("Row Sum : ",row_sum(rows,columns,matrix))