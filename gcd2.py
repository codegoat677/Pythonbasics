def gcd(a,b): #a>b
    if a<b:
        (a,b)=(b,a)
    if a % b == 0:
       return b
    else:
       return (gcd(b, a % b))
x= int(input("Enter first number: "))
y= int(input("Enter second number: "))
print("Greatest Common Divisor is: ", gcd(x,y))
