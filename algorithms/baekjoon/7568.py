import sys

person=[]
result = []

def addPerson(w, h):
    person.append([w,h])

N=int(input())

for i in range(N):
    weight,height=map(int,input().split())
    addPerson(weight,height)

for i in range(N):
    score=1
    for j in range(N):
        if(person[i][0]<person[j][0] and person[i][1]<person[j][1]):
            score+=1
    result.append(score)

print(*result)

