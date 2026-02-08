import sys

input=sys.stdin.readline

n=int(input())

#1, 13, 19, 23, 31, 79, 97

def is_prime(x):
    if x<2:
        return False
    for i in range(2, int(x**0.5)+1):
        if x%i==0:
            return False
    return True

def square_sum(x):
    a=0
    while(x>0):
        d=x%10
        a+=d*d
        x//=10
    return a

def sang(x):
    set1=set()

    while(1):
        if x==1:
            return True
        if x in set1:
            return False
        set1.add(x)
        x=square_sum(x)

for i in range(1,n+1):
    if is_prime(i) and sang(i):
        print(i)