import sys

input=sys.stdin.readline

N,M=map(int, input().split())
score={}

for x in range(N):
    word=input().rstrip()
    if len(word)<M:
        continue
    if word in score:
        score[word]+=1
    else:
        score[word]=1

def sort_word(word):
    cnt=score[word]
    len_word=len(word)

    return(-cnt,-len_word,word)

words=list(score.keys())
words.sort(key=sort_word)

for y in words:
    print(y)



