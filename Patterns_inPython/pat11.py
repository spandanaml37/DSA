n=int(input("enter the number"))
for i in range(0,n):
    for j in range(0,i+1):
        if(i+j)%2==0:
            print("1",end="")
        else:
            print("0",end="")
    print()