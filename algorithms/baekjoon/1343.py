board = input().strip()

result=""
cnt=0

for ch in board:
    if ch=='X':
        cnt+=1
        pass

    else:
        if (cnt > 0):
            if(cnt%2==1):
                print("-1")
                exit()
            else:
                result += 'AAAA'*(cnt//4)
                remain = cnt % 4
                if(remain == 2):
                    result += 'BB'
                    pass
        cnt = 0
        result += '.'

if (cnt > 0):
    if(cnt%2==1):
        print("-1")
        exit()
    else:
        result += 'AAAA'*(cnt//4)
        remain = cnt % 4
        if(remain == 2):
            result += 'BB'

print(result)