#pattern7
n=int(input('enter the number'))
for i in range(n):
        for j in range(n-i-1):
            print(" ",end="")
        for j in range(2*i+1):
            print("*",end="")
        for j in range(n-i-1):
            print(" ",end="")
        print()

#pattern8
n=int(input('enter the number'))
for i in range(n,-1,-1):
        for j in range(n-i):
            print(" ",end="")
        for j in range(2*i-1):
            print("*",end="")
        print()



