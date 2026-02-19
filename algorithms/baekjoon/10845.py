import sys
from collections import deque

input=sys.stdin.readline
n=int(input())
dq=deque()

for i in range(n):
    cmd=input().rstrip().split()

    if cmd[0]=='push':
        dq.append(cmd[1])
    elif cmd[0]=='pop':
        if dq:
            ch=dq.popleft()
            print(ch)
        else: print('-1')
    elif cmd[0]=='size':
        print(len(dq))
    elif cmd[0]=='empty':
        if dq:
            print('0')
        else: print('1')
    elif cmd[0]=='front':
        if dq:
            print(dq[0])
        else: print('-1')
    elif cmd[0]=='back':
        if dq:
            print(dq[-1])
        else: print('-1')