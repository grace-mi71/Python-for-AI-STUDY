import sys
from collections import deque

test_case=int(input())
for i in range(test_case):
    N,M=map(int, input().split())
    score=list(map(int, input().split()))

    q=deque((p, idx) for idx, p in enumerate(score))
    count=0

    while q:
        cur=q.popleft()
        if any(cur[0]<other[0] for other in q):
            q.append(cur)
        else:
            count+=1
            if cur[1]==M:
                print(count)
                break

