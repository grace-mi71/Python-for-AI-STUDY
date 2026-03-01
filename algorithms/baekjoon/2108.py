import sys
from collections import Counter
input=sys.stdin.readline
stack=[]
n=int(input())

for i in range(n):
    m=int(input())
    stack.append(m)

# print(int((sum(stack)/len(stack))+0.5))
print(round(sum(stack)/n))

stack_sort=sorted(stack)
mid=int((n//2)+0.5)
print(stack_sort[mid])

cnt = Counter(stack_sort)
modes = cnt.most_common(2)
if len(modes) > 1 and modes[0][1] == modes[1][1]:
    print(modes[1][0])
else:
    print(modes[0][0])

print(stack_sort[-1]-stack_sort[0])