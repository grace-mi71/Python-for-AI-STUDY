import sys

input=sys.stdin.readline

n,m=map(int,input().split())

box_list=[0]*n

for x in range(n):
    box_list[x]=x+1

for _ in range(m):
    i,j=map(int,input().split())

    box_list[i-1:j]=box_list[i-1:j][::-1]

print(*box_list)
