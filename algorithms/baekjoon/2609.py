import sys
input=sys.stdin.readline
GCD=0
a,b=map(int,input().split())

origin_a=a
origin_b=b

while(1):
    r=a%b
    a=b
    b=r
    if(r==0):
        GCD=a
        break
    
    
print(GCD)
print(origin_a*origin_b//GCD)

