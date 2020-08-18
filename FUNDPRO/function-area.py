PI = 3.1416


def compute_area(radius):
    return float(PI * pow(radius, 2))


rad = float(input("Enter the radius of the circle: "))
area = round(compute_area(rad), 2)

print(f"The area of the circle is {area}.")
