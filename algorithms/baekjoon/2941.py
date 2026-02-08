import sys

input=sys.stdin.readline
word=input().rstrip()

croatia=["c=","c-","dz=","d-","lj","nj","s=","z="]

for p in croatia:
    word=word.replace(p,'*')

print(len(word))