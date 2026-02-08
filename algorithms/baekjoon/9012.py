import sys
from collections import deque

input=sys.stdin.readline
n=int(input())

for _ in range(n):
    stack=[]
    ok=True
    word=input().rstrip()

    for i in range(len(word)):
        ch=word[i]
        if ch=='(':
            stack.append(ch)
        elif ch==')':
            if not stack:
                ok=False
                break
            stack.pop()

    if(ok and not stack):
        print("YES")
    else:
        print("NO")