a=int(input('enter one number'))
b=int(input('enter two number'))
def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)
print(gcd(a,b))


    