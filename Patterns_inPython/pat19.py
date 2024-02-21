n=int(input("enter the number"))
for i in range(n,-1,-1):
    for j in range(0,i):
        print("*",end="")
    for j in range(2*n-2*i):
        print(" ",end="")
    for l in range(i,0,-1):
        print("*",end="")
    print()
for i in range(1,n+1):
    for j in range(0,i):
        print("*",end="")
    for j in range(2*n-2*i):
        print(" ",end="")
    for l in range(i,0,-1):
        print("*",end="")
    print()