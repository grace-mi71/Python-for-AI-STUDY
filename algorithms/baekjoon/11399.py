import sys
from collections import deque

input=sys.stdin.readline
n=int(input())

result=0
time=list(map(int,input().split()))
time.sort()

for i in range(n):
    result=result+(n-i)*time[i]

print(result)