import math

def quad_equation(b, determinant):
    x1 = int((-b + math.sqrt(determinant)) / 2)
    x2 = int((-b - math.sqrt(determinant)) / 2)

    print(f"\nThe values of x are {x1} and {x2}.")


a = int(input("Enter the value for a: "))
b = int(input("Enter the value for b: "))
c = int(input("Enter the value for c: "))

determinant = pow(b, 2) - (4 * a * c)

while determinant < 1:
    print("\nThere is no solution for x. Please try again.\n")
    a = int(input("Enter the value for a: "))
    b = int(input("Enter the value for b: "))
    c = int(input("Enter the value for c: "))
    determinant = pow(b, 2) - (4 * a * c)

quad_equation(b, determinant)

