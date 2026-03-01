import sys
input=sys.stdin.readline
stack=[]

k=int(input())
for i in range(k):
    
    n=int(input())
    if n!=0:
        stack.append(n)
    else:
        stack.pop()
    
print(sum(stack))