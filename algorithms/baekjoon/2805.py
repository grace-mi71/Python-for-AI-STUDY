import sys

input=sys.stdin.readline
N,M=map(int,input().split())

tree=list(map(int,input().split()))

L,R=0,max(tree)
ans=0

while(L<=R):
    mid=(L+R)//2
    cnt=sum(max(0,H-mid) for H in tree)

    if cnt>=M:
        ans=mid
        L=mid+1
    else:
        R=mid-1

print(ans)