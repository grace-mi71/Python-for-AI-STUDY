import sys
t=int(input())
p=[0]*101
p[1]=p[2]=p[3]=1

for _ in range(t):
    n=int(input())
    if n<4:
        print(p[n])
    else:
        for i in range(4,n+1):
            p[i]=p[i-3]+p[i-2]
        print(p[n])
