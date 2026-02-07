import sys
input=sys.stdin.readline

N=int(input())

if(N==1):
    print("1")
else:
    i=1
    result=1
    while(1):
        if(N<=result):
            print(i)
            break
        else:
            result = result+6*i
            i=i+1

