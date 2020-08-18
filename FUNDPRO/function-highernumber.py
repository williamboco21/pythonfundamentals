def max_number(num1, num2):
    if num1 == num2:
        print("\nBoth numbers are equal.")
        exit()
    elif num1 > num2:
        return num1
    else:
        return num2


number1 = int(input("Enter your number 1: "))
number2 = int(input("Enter your number 2: "))

maximum = max_number(number1, number2)

print(f"\nThe higher number is {maximum}.")
