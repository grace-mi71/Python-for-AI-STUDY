import sys
input=sys.stdin.readline

n=int(input())
count=0
num=666

while 1:
    if '666' in str(num):
        count+=1
        if count==n:
            print(num)
            break
    num+=1