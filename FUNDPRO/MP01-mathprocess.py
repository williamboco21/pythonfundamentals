import math


def compute_mean(x1, x2, x3, x4, x5):

    return (x1 + x2 + x3 + x4 + x5) / 5


def compute_standard(x1, x2, x3, x4, x5, mean):
    standard = pow(x1 - mean, 2) + pow(x2 - mean, 2) + pow(x3 - mean, 2) + pow(x4 - mean, 2) + pow(x5 - mean, 2)
    standard /= 5
    return math.sqrt(standard)


num1 = int(input("Enter a positive integer: "))
num2 = int(input("Enter a positive integer: "))
num3 = int(input("Enter a positive integer: "))
num4 = int(input("Enter a positive integer: "))
num5 = int(input("Enter a positive integer: "))

mean = compute_mean(num1, num2, num3, num4, num5)
standard = round(compute_standard(num1, num2, num3, num4, num5, mean), 4)

print(f"\nThe mean is {mean}.")
print(f"The standard deviation is {standard}.")
