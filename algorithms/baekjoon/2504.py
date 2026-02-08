import sys

input=sys.stdin.readline

word=input().rstrip()

stack=[]
temp=1
answer=0

for i in range(len(word)):
    ch=word[i]

    if(ch=="("):
        temp*=2
        stack.append(ch)
    elif(ch=="["):
        temp*=3
        stack.append(ch)
    elif(ch==")"):
        if(len(stack)==0 or stack[-1]!="("):
            answer=0
            break
        if(word[i-1]=="("):
            answer+=temp
        stack.pop()
        temp//=2
    elif(ch=="]"):
        if(len(stack)==0 or stack[-1]!="["):
            answer=0
            break
        if(word[i-1]=="["):
            answer+=temp
        stack.pop()
        temp//=3

if stack:
    print(0)
else:
    print(answer)


