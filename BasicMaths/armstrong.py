n=int(input('enter the number'))
sum=0
c=n
while n!=0:
    d=n%10
    sum=sum+(d*d*d)
    n=n//10
if c==sum:
    print("Armstorng")
else:
    print("Not Armstrong")