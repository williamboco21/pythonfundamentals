def circle():
    pi = 3.1416
    print("\nYou have selected a circle.\n")
    radius = int(input("Enter the radius of the circle: "))

    area = round(pi * pow(radius, 2), 2)

    print(f"\nThe area of the circle is {area}.")


def square():
    print("\nYou have selected a square.\n")
    side = int(input("Enter the side of the square: "))

    area = pow(side, 2)

    print(f"\nThe area of the square is {area}.")


def triangle():
    print("\nYou have selected a triangle.")
    base = int(input("Enter the base of the triangle: "))
    height = int(input("Enter the height of the triangle: "))

    area = 0.5 * base * height

    print(f"\nThe area of the triangle is {area}.")


print("This program computes the area of a circle, square or triangle.")
print("Press 1 for a circle, 2 for a square, and 3 for a triangle.")
selection = int(input("Enter your selection: "))

while selection < 1 or selection > 3:
    print("\nPlease enter a number between 1 and 3\n")
    selection = int(input("Enter your selection: "))

if selection == 1:
    circle()
elif selection == 2:
    square()
else:
    triangle()
