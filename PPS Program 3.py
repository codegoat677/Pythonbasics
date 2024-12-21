# Find Roots of a Quadratic Equation
import math
import cmath
a= float(input("Enter coefficient a: "))
b= float(input("Enter coefficient b: "))
c= float(input("Enter coefficient c: "))
d= (b**2) - (4*a*c)
if d>=0:
    root1= (-b + math.sqrt(d))/2*a
    root2= (-b - math.sqrt(d))/2*a
    print("The roots are:", root1, "and", root2)
else:
    print("The equation has complex roots")
    root1 = (-b + cmath.sqrt(d)) / (2 * a)
    root2 = (-b - cmath.sqrt(d)) / (2 * a)
    print("The roots are:", root1, "and", root2)

