n=int(input("enter the number"))
for i in range(1,n+1):
    for j in range(1,i+1):
        num=ord('A')
        print(chr(num+i-1),end="")
        num+=1
    print()