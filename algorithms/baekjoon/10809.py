S= input().strip()
pos = [-1]*26

for i in range(len(S)):
    ch=S[i]
    idx=ord(ch)-ord('a')

    if(pos[idx]==-1):
        pos[idx] = i

for x in pos:
    print(x, end=" ")