import sys
input=sys.stdin.readline

n=int(input())
p=[]

for i in range(n):
    x,y=map(int,input().split())
    p.append((x,y))

p.sort()

for x,y in p:
    print(x,y)