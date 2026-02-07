import sys

input=sys.stdin.readline

A=int(input())
B=int(input())

result1 = A*(B%10)
result2 = ((B-(B%10))%100)//10


print(result1)
print(A*result2)
print(A*(B//100))
print(A*B)