n=int(input('enter the number'))
reverse=0
while n!=0:
    d=n%10
    reverse=reverse*10+d
    n=n//10
print(reverse)