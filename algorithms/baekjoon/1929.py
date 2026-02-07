import sys

input=sys.stdin.readline

M,N=map(int, input().split())

isPrime=[True]*(N+1)
isPrime[0]=False
isPrime[1]=False

limit=int(N**0.5)
for i in range(2,limit+1):
    if isPrime[i]:
        for j in range(i**2,N+1,i):
            isPrime[j]=False

for num in range(M,N+1):
    if isPrime[num]==True:
        print(num)