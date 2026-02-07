import sys
input= sys.stdin.readline

N,M=map(int, input().split())

cards=list(map(int,input().split()))

A1=0
i=0
j=1
k=2
for i in range(0,N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            A=cards[i]+cards[j]+cards[k]
            if(A<=M and A>=A1):
                A1=A
            
print(A1)