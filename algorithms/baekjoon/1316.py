import sys

input=sys.stdin.readline

cnt=0
n=int(input())

for _ in range(n):
    seen=set()
    word=input().rstrip()
    prev=""
    is_group=True

    for ch in word:
        if ch!=prev:
            if ch in seen:
                is_group=False
                break
            seen.add(prev)
            prev=ch

    if is_group:
        cnt+=1

print(cnt)


