#pattern1
n=int(input("enter the number"))
for i in range(0,n):
    for j in range(0,n):
        print("*",end="")
    print()

#pattern2
n=int(input("enter the number"))
for i in range(0,n):
    for j in range(0,i+1):
        print("*",end="")
    print()

#pattern3
n=int(input("enter the number"))
for i in range(0,n):
    for j in range(0,i+1):
        print(j+1,end="")
    print()

#pattern4
n=int(input("enter the number"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end="")
    print()

#pattern5
n=int(input("enter the number"))
for i in range(n,-1,-1):
    for j in range(0,i):
        print("*",end="")
    print()

#pattern6
n=int(input("enter the number"))
for i in range(n,-1,-1):
    for j in range(0,i):
        print(j+1,end="")
    print()





