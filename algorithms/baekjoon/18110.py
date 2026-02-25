import sys
input=sys.stdin.readline

n=int(input())

if n==0:
    print(0)
    sys.exit()
else:
    arr=sorted([int(input()) for _ in range(n)])

    p=int((n*0.15)+0.5)
    avg=sum(arr[p:n-p])/(n-2*p)
    print(int(avg+0.5))