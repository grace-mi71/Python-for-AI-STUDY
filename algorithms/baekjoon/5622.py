import sys

input=sys.stdin.readline

result=0
word=input()

for x in range(len(word)-1):
    if(word[x]=="A"or word[x]=="B"or word[x]=="C"):
        result+=3
    elif(word[x]=="D"or word[x]=="E"or word[x]=="F"):
        result+=4
    elif(word[x]=="G"or word[x]=="H"or word[x]=="I"):
        result+=5
    elif(word[x]=="J"or word[x]=="K"or word[x]=="L"):
        result+=6
    elif(word[x]=="M"or word[x]=="N"or word[x]=="O"):
        result+=7
    elif(word[x]=="P"or word[x]=="Q"or word[x]=="R" or word[x]=="S"):
        result+=8
    elif(word[x]=="T"or word[x]=="U"or word[x]=="V"):
        result+=9
    elif(word[x]=="W"or word[x]=="X"or word[x]=="Y"or word[x]=="Z"):
        result+=10
    
print(result)