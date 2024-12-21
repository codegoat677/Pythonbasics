# Find the Largest of Three Numbers
x= float(input("Enter the first number: "))
y= float(input("Enter the second number: "))
z= float(input("Enter the third number: "))
if x >= y and x >= z:
    print(x, "is the largest number")
elif y >= x and y >= z:
    print(y, "is the largest number")
else:
    print(z, "is the largest number")

   