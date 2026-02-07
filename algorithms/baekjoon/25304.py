import sys

input=sys.stdin.readline

result=0

x=int(input())
n=int(input())

for i in range(n):
    a,b=map(int, input().split())

    result=result+a*b

if result==x:
    print("Yes")
else:
    print("No")    