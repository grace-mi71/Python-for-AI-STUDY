import sys

input=sys.stdin.readline

t=int(input())

for i in range(t):
    j=i+1
    a,b=map(int,input().split())
    c=a+b
    print("Case #", j , ": ",c,sep="")