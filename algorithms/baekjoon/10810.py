import sys

input=sys.stdin.readline

N,M=map(int,input().split())

ball_list=[0]*N

for _ in range(M):
    i,j,k=map(int, input().split())
    for x in range(i-1,j):
        ball_list[x]=k
    
print(*ball_list)
