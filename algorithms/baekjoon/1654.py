import sys
input=sys.stdin.readline

k,n=map(int,input().split())
lan=[int(input()) for _ in range(k)]

L,R=1,max(lan)
ans=0

while L<=R:
    mid=(L+R)//2
    cnt=sum(i//mid for i in lan)

    if cnt>=n:
        ans=mid
        L=mid+1
    else:
        R=mid-1

print(ans)
    
