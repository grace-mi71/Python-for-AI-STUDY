switch_num=int(input())

switchs=[0]+list(map(int, input().split()))

student = int(input())

def toggle(idx):
    if(switchs[idx]==0):
        switchs[idx]=1
    else:
        switchs[idx]=0
    pass

def boy(num):
    i=num
    while num <= switch_num:
        toggle(num)
        num = i+num
        pass

def girl(num):
    toggle(num)
    i=1
    
    while(1):
        left = num-i
        right = num+i

        if left<1 or right>switch_num:
            break

        if switchs[left]==switchs[right]:
            toggle(left)
            toggle(right)
            pass
        else:
            break
        
        i+=1

for _ in range(student):
    gender, num = map(int,input().split())

    if gender==1:
        boy(num)
    else:
        girl(num)

for i in range(1, switch_num+1):
    print(switchs[i], end=" ")
    if i % 20 == 0:
        print()