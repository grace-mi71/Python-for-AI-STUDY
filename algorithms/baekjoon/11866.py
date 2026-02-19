import sys
from collections import deque
input=sys.stdin.readline

N,K=map(int,input().rstrip().split())
dq=deque()
dq_result=deque()

for i in range(N):
    dq.append(i+1)

while dq:
    dq.rotate(-(K-1))
    ch=dq.popleft()
    dq_result.append(ch)

print('<' + ', '.join(map(str, dq_result)) + '>')