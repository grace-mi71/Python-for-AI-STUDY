import sys

input=sys.stdin.readline

N,M=map(int,input().split())

box=[0]*N

for x in range(N):
    box[x]=x+1

for y in range(M):
    i,j=map(int,input().split())

    box[i-1],box[j-1]=box[j-1],box[i-1]

print(*box)