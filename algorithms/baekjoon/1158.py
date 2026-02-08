import sys
from collections import deque

input=sys.stdin.readline

N,K=map(int, input().split())

stack=deque(range(1,N+1))
arr=deque()

while(stack):
    stack.rotate(-(K-1))
    arr.append(stack.popleft())

print("<"+', '.join(map(str,arr))+'>')