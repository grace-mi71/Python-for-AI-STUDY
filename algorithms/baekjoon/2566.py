import sys

input=sys.stdin.readline

array=[[0]*9 for _ in range(9)]

for i in range(9):
    row=list(map(int,input().split()))
    for j in range(9):
        array[i][j]=row[j]

max_value=-1
max_row=0
max_col=0

for x in range(9):
    for y in range(9):
        if array[x][y]>max_value:
            max_value=array[x][y]
            max_row=x
            max_col=y

print(max_value)
print(max_row+1,max_col+1)
