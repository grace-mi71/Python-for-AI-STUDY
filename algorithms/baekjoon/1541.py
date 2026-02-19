import sys

input=sys.stdin.readline

expr=input().rstrip()
parts=expr.split('-')

nums=[]

for i in parts:
    s=sum(map(int,i.split('+')))
    nums.append(s)

result=nums[0]

for x in nums[1:]:
    result=result-x

print(result)