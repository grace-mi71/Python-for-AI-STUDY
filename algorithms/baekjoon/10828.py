import sys
from collections import deque

input=sys.stdin.readline
dq=deque()

def push(dq,i):
    dq.append(i)

def pop(dq):
    if(len(dq)==0):
        print(-1)
    else:
        print(dq.pop())

def size(dq):
    print(len(dq))

def empty(dq):
    if(len(dq)==0):
        print(1)
    else:
        print(0)

def top(dq):
    if(len(dq)==0):
        print(-1)
    else:
        print(dq[-1])

n=int(input())
for _ in range(n):
    cmd=input().split()

    if(cmd[0]=="push"):
        push(dq,int(cmd[1]))
    elif(cmd[0]=="pop"):
        pop(dq)
    elif(cmd[0]=="size"):
        size(dq)
    elif(cmd[0]=="empty"):
        empty(dq)
    elif(cmd[0]=="top"):
        top(dq)
    








# import sys
# from collections import deque

# input=sys.stdin.readline

# dq=deque()

# def push(dq,i):
#     dq.append(i)

# def pop(dq):
#     if(len(dq)==0):
#         print(-1)
#     else:
#         popValue=dq.popleft()
#         print(popValue)

# def size(dq):
#     print(len(dq))

# def empty(dq):
#     if(len(dq)==0):
#         print(1)
#     else:
#         print(0)

# def front(dq):
#     if(len(dq)==0):
#         print(-1)
#     else:
#         print(dq[0])

# def back(dq):
#     if(len(dq)==0):
#         print(-1)
#     else:
#         print(dq[-1])

# n=int(input())

# for _ in range(n):
#     cmd=input().split()

#     if cmd[0]=="push":
#         push(dq, int(cmd[1]))
#     elif cmd[0]=="pop":
#         pop(dq)
#     elif cmd[0]=="size":
#         size(dq)
#     elif cmd[0]=="empty":
#         empty(dq)
#     elif cmd[0]=="front":
#         front(dq)
#     elif cmd[0]=="back":
#         back(dq)


