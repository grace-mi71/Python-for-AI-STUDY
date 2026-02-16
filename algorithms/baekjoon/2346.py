import sys
from collections import deque

n=int(input())
word=list(map(int,input().split()))

q=deque((p,idx+1) for idx,p in enumerate(word))
result_dq=[]

while q:
    cur=q.popleft()
    move, idx=cur
    result_dq.append(idx)

    if not q:
        break

    if move>0:
        q.rotate(-(move-1))
    else:
        q.rotate(-move)

print(*result_dq)
