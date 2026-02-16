import sys
input=sys.stdin.readline

n=int(input())
events=[]

for i in range(n):
    x,r=map(int,input().split())
    L=x-r
    R=x+r
    events.append((L,0,i))
    events.append((R,1,i))

events.sort()
stack=[]
ok=True
prev_x=None

for x,type,idx in events:
    if type==0 and prev_x==x:
        ok=False
        break
    if type==0:
        stack.append(idx)
    else:
        if not stack or stack[-1]!=idx:
            ok=False
            break
        stack.pop()
    prev_x=x

print("YES" if ok else "NO")


