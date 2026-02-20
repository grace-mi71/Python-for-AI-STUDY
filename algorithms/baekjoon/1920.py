import sys
input=sys.stdin.readline

N=int(input())
arr1=list(map(int,input().split()))
arr1_set=set(arr1)

N=int(input())
arr2=list(map(int, input().split()))

for i in arr2:
    if i in arr1_set:
        print('1')
    else:
        print('0')