import sys
input=sys.stdin.readline

n,m=map(int, input().split())
board=[input().rstrip() for _ in range(n)]

min_cnt=64

for i in range(n-7):
    for j in range(m-7):
        cnt1,cnt2=0,0
        for x in range(8):
            for y in range(8):
                if (i+x + j+y)%2==0:
                    if board[i+x][j+y]!='W':cnt1+=1
                    if board[i+x][j+y]!='B':cnt2+=1
                else:
                    if board[i+x][j+y]!='B':cnt1+=1
                    if board[i+x][j+y]!='W':cnt2+=1
        min_cnt=min(cnt1,cnt2,min_cnt)

print(min_cnt)
