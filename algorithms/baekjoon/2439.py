S=int(input())

for i in range(S):
    space=" "*(S-i-1)
    star="*" * (i+1)
    print(space+star)