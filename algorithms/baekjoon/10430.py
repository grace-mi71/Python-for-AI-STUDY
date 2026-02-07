#readline에 괄호를 넣어버리면 문자열이 되어버림!

import sys

input=sys.stdin.readline

A,B,C=map(int,input().split())

print((A+B)%C)
print(((A%C)+(B%C))%C)
print((A*B)%C)
print(((A%C) * (B%C))%C)