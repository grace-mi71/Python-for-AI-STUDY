import sys

input=sys.stdin.readline
n=int(input())
cnt=0

for i in range(n):
    word=input().rstrip()
    stack=[]

    for ch in word:
        if stack and stack[-1]==ch:
            stack.pop()
        else:
            stack.append(ch)
    
    if not stack:
        cnt+=1

print(cnt)