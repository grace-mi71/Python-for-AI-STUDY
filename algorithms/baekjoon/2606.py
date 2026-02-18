import sys
from collections import defaultdict, deque
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

n=int(input())
m=int(input())

graph=defaultdict(list)

for _ in range(m):
    a,b=map(int,input().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

visited=[False]*(n+1)
q=deque([1])
visited[1]=True
cnt=0

while q:
    now=q.popleft()
    cnt+=1

    for next in graph[now]:
        if not visited[next]:
            visited[next]=True
            q.append(next)

print(cnt-1)