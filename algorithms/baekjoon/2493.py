import sys

input=sys.stdin.readline
n=int(input())
heights=list(map(int,input().split()))

stack=[]
answer=[0]*n

for i in range(n):
    h=heights[i]
    while stack and stack[-1][0]<h:
        stack.pop()
    if stack:
        answer[i]=stack[-1][1]
    
    stack.append((h,i+1))

print(*answer)