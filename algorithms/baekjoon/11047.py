import sys
input=sys.stdin.readline

N,K=map(int,input().split())
arr=[0]*N
cnt=0

for i in range(N):
    arr[i]=int(input())

arr.reverse()

for i in range(len(arr)):
    if arr[i]<=K:
        cnt=cnt+K//arr[i]
        K %= arr[i]
    else: continue

print(cnt)