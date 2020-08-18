numerator = float(input("Enter the numerator: "))
denominator = float(input("Enter the denominator: "))

if denominator != 0:
    quotient = int(numerator / denominator)
    print(f'\nThe quotient is {quotient}.')
else:
    print("The division can not take place.")
    print("The denominator is equal to 0.")