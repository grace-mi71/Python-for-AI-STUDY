import sys

dictionary_person=[]

def addDictionary(age, name):
    dictionary_person.append([age,name])


input=sys.stdin.readline
N=int(input())


for i in range(N):
    age_str,name_real=input().split()
    age=int(age_str)
    addDictionary(age, name_real)

dictionary_person.sort(key=lambda x:x[0])

for age, name_real in dictionary_person:
    print(age,name_real)

