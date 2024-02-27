n=int(input('enter the number'))
reverse=0
c=n
while n!=0:
    d=n%10
    reverse=reverse*10+d
    n=n//10
if c==reverse:
    print("It is palindrome")
else:
    print("It is not palindrome")

