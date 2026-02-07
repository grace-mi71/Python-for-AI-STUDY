import sys

input=sys.stdin.readline

t=int(input())

for _ in range(t):
    word=input().rstrip()
    print(word[0],word[len(word)-1],sep="")
