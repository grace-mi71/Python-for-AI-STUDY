import sys

input=sys.stdin.readline

N=int(input())

arr=[-1]*N
for i in range(N):
    arr[i]=int(input())
#-----------------------------입력

arr.sort()

#-----------------------------정렬

for i in range(N):
    print(arr[i])

#-----------------------------출력