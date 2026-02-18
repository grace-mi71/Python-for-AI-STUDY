import sys

input=sys.stdin.readline
t=int(input())

for _ in range(t):
    n=int(input())
    clothes={}

    for i in range(n):
        name, category=input().rstrip().split()
        clothes[category]=clothes.get(category,0)+1
    
    result=1
    for count in clothes.values():
        result*=(count+1)
    print(result-1)

