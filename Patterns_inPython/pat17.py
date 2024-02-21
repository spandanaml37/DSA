n=int(input("enter the number"))
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for k in range(0,i):
        print(chr(ord('A')+k),end="")
    for l in range(i-2,-1,-1):
        print(chr(ord('A')+l),end="")
    print()