import sys

input=sys.stdin.readline
n,m=map(int,input().split())

arr=[0]+list(map(int, input().rstrip().split()))

for i in range(1,n+1):
    arr[i] = arr[i]+arr[i-1]

for k in range(m):
    i,j=map(int, input().rstrip().split())
    print(arr[j]-arr[i-1])