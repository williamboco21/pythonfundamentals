def height_in_inches(feet, inches):
    return (feet * 12) + inches


def convert_to_meters(feet, inches):
    height = height_in_inches(feet, inches) * 0.0254
    return height


def convert_to_kilograms(weight):
    return int(weight / 2.2)


print("Enter your height in feet and inches.")
feet = int(input("First, enter the feet: "))
inches = int(input("Next, enter the inches: "))
pounds = int(input("Finally, enter your weight in pounds: "))

height_in_meters = convert_to_meters(feet, inches)
weight_to_kilograms = convert_to_kilograms(pounds)
BMI = weight_to_kilograms / pow(height_in_meters, 2)

print(f"\nYour height in meters is {height_in_meters}.")
print(f"Your weight in is {weight_to_kilograms}.")
print(f"Your BMI is {round(BMI, 4)}.")
