import sys
input=sys.stdin.readline

while 1:
    word=input().rstrip()
    if word=='.':
        break
    
    stack=[]
    is_right=True
    
    for ch in word:
        if ch in '([':
            stack.append(ch)
        elif ch=='[':
            stack.append(ch)
        elif ch==')':
            if not stack or stack[-1]!='(':
                is_right=False
                break
            stack.pop()
        elif ch==']':
            if not stack or stack[-1]!='[':
                is_right=False
                break
            stack.pop()

    if is_right and not stack:
        print('yes')
    else:
        print('no')

