import sys
input=sys.stdin.readline
word=[]
stack=[]

n=int(input())
target = [int(input()) for _ in range(n)]

stack=[]
ops=[]
cur=1
possible=True

for num in target:
    while cur<=num:
        stack.append(cur)
        ops.append('+')
        cur+=1
    if stack and stack[-1]==num:
        stack.pop()
        ops.append('-')
    else:
        possible=False
        break

if not possible:
    print("NO")
else:
    print('\n'.join(ops))