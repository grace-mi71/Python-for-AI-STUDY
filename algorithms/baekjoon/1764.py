import sys
input=sys.stdin.readline

n,m=map(int,input().split())
s1=set()
s2=set()

for _ in range(n):
    s1.add(input().rstrip())
for _ in range(m):
    s2.add(input().rstrip())

duplicates=sorted(s1.intersection(s2))

print(len(duplicates))

for i in range(len(duplicates)):
    print(duplicates[i])