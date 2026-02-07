import sys

input=sys.stdin.readline

student_list=[0]*30

for i in range(28):
    n=int(input())
    student_list[n-1]=n

for x in range(30):
    if(student_list[x]==0):
        print(x+1)
    else:
        continue

