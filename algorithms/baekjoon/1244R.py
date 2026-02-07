switch_num=int(input())

state = [0]+list(map(int, input().split()))

student = int(input())

def toggle(idx):
    if(switch_num[idx]==0):
        switch_num[idx]=1
    else:
        switch_num[idx]=0
    pass

def boy(num):
    i=num
    while (num <= switch_num):
        toggle(switch_num[num])
        num = i+num
    pass

def girl(num):
    left=num-1
    right=num+1
    
    while(1):
        if(left < 1 or right > switch_num):
            break

        if(switch_num[left]==switch_num[right]):
            toggle(switch_num[left])
            toggle(switch_num[right])
        else:
            break
    pass

for _ in range (student):
    gender, num=map(int,input().split())

    if(gender==1):
        boy(num)
    else:
        girl(num)
    pass

for i in range(1, switch_num+1):
    print(state[i], end=" ")
    if(i%20):
        print()