import sys

input=sys.stdin.readline

n=int(input())

numbers=list(map(int,input().split()))

find_number=int(input())

result=0

for i in range(len(numbers)):
    if(numbers[i]==find_number):
        result+=1

print(result)
