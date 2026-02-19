import sys
input=sys.stdin.readline

N,M=map(int,input().split())
N1=1
M1=1
for i in range(N,N-M,-1):
    N1=N1*i
for j in range(1,M+1):
    M1=M1*j

print(N1//M1)