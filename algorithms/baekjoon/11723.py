import sys

input=sys.stdin.readline
m=int(input())
s=0

for _ in range(m):
    cmd, *x=input().rstrip().split()
    x=int(x[0]) if x else 0

    if cmd=="add":
        s|=(1<<x)
    elif cmd=="remove":
        s&=~(1<<x)
    elif cmd=="check":
        print(1 if s & (1<<x) else 0)
    elif cmd=="toggle":
        s^=(1<<x)
    elif cmd =="all":
        s=(1<<21)-1
    elif cmd=="empty":
        s=0