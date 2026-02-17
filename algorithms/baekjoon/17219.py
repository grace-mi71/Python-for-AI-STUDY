import sys

input=sys.stdin.readline
n,m=map(int,input().split())

ad_to_ID={}

for _ in range(n):
    ad,ID=map(str,input().rstrip().split())
    ad_to_ID[ad]=ID

for _ in range(m):
    q=input().rstrip()
    print(ad_to_ID[q])