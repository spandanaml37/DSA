n=int(input("enter the number"))
for i in range(1,n+1):
    num=ord('A')
    for j in range(1,i+1):
        print(chr(num),end="")
        num+=1
    print()