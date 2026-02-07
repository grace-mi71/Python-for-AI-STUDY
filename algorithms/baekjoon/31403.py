A=int(input())
B=int(input())
C=int(input())

print(A+B-C)

if(B>0 and B<10):
    print(A*10+B-C)
elif(B>9 and B<100):
    print(A*100 + B -C)
elif(B>99 and B<1000):
    print(A*1000 + B-C)
elif(B==1000):
    print(A*10000 + B-C)