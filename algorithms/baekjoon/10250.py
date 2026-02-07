T=int(input())

for i in range(T):
    H,W,N=map(int,input().split())

    forward=(N % H) * 100
    back=N//H + 1

    if(forward == 0):
        forward=H * 100
        back = back-1
    
    print(forward + back)

    H=0
    W=0
    N=0