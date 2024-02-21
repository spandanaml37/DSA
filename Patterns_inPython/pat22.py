n=int(input("enter the number"))
for i in range(0,2*n-1):
    for j in range(0,2*n-1):
        #top=i
        #left=j
        #right=(2*n-2)-j
        #down=(2*n-2)-i
        print(n-min(i,j,(2*n-2)-j,(2*n-2)-i),end="")
    print()