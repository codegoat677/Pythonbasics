# Function to calculate roots of a quadratic equation
import cmath
def find_roots(a, b, c):
    # Calculate discriminant
    d = b**2 - 4*a*c
    # Calculate two roots using the quadratic formula
    root1 = (-b + cmath.sqrt(d)) / (2 * a)
    root2 = (-b - cmath.sqrt(d)) / (2 * a)
    # Display results
    print("Root 1:", root1)
    print("Root 2:", root2)
# Example usage
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))
# Running the function to find roots
find_roots(a, b, c)
