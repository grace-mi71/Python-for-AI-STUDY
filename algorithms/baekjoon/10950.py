T=int(input())
result=[-1]*T

for i in range(T):
    A, B=map(int,input().split())
    result[i]=A+B

    A=0
    B=0

for i in range(T):
    print(result[i])