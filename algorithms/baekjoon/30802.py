N=int(input())


size=list(map(int,input().split()))

T,P=map(int,input().split())

result=0

for i in range(6):
    real=(size[i]//T)+1
    if(size[i]%T==0):
        real=size[i]//T
    result+=real
print(result)

maxP=N//P
minP=N%P

print(maxP, minP, end=" ")