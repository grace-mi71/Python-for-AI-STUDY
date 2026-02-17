import sys
input=sys.stdin.readline
S=set()
n,m=map(int, input().split())

for i in range(n):
    S.add(input().rstrip())

cnt=0

for _ in range(m):
    word=input().rstrip()
    if word in S:
        cnt+=1
    
print(cnt)