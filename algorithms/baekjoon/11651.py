import sys
input=sys.stdin.readline

N=int(input())
list_xy=[]

for i in range(N):
    x,y=map(int,input().split())
    list_xy.append((x,y))

list_xy.sort(key=lambda p:(p[1],p[0]))

for x,y in list_xy:
    print(x,y)

