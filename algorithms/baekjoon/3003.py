import sys

input=sys.stdin.readline

black=[1,1,2,2,2,8]
white=list(map(int, input().split()))

result=[0]*6

for x in range(6):
    result[x]=black[x]-white[x]

print(*result)