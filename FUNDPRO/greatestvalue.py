first_integer = int(input("Enter the 1st integer: "))
second_integer = int(input("Enter the 2nd integer: "))
third_integer = int(input("Enter the 3rd integer: "))
highest = None

if first_integer > second_integer:
    highest = first_integer
else:
    highest = second_integer

if third_integer > highest:
    highest = third_integer

print(f'\nthe integer with the highest value is {highest}.')