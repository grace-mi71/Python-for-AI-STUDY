import sys

input=sys.stdin.readline

sticks=input().rstrip()
stack=[]
answer=0

for i,ch in enumerate(sticks):
    if ch=='(':
        stack.append('(')
    elif ch==')':
        stack.pop()
        if sticks[i-1]=='(':
            answer+=len(stack)
        elif sticks[i-1]==')':
            answer+=1

print(answer)