import sys

input=sys.stdin.readline
t=int(input())

for _ in range(t):
    N=int(input())

    zero,one=1,0

    for i in range(N):
        zero,one=one,zero+one
    
    print(zero,one)

# Zero[N]=One[N-1]
# One[N]=Zero[N-1]+One[N-1]