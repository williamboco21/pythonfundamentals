area = None
PI = 3.1416
print("This program computes the area of a circle, square and triangle.")
print("Press 1 for a circle, 2 for a square and 3 for a triangle.")
choice = int(input("Enter your selection: "))

if choice == 1:
    print("You have selected a circle.")
    radius = int(input("Enter the radius of a circle: "))
    area = round(PI * pow(radius, 2), 2)
    print(f'\nThe area of a circle is {area}.')

elif choice == 2:
    print("You have selected a square.")
    side = int(input("Enter the length of a side: "))
    area = round(pow(side, 2), 2)
    print(f'\nThe area of a square is {area}.')

elif choice == 3:
    print("You have selected a triangle.")
    base = int(input("Enter the base of a triangle: "))
    height = int(input("Enter the height of a triangle: "))
    area = round(0.5 * (base * height), 2)
    print(f'\nThe area of a square is {area}.')

else:
    print("\nInvalid entry! Program Terminating!")