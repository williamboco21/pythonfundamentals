def count(num):
    odd = 0
    zero = 0
    even = 0

    while num > 0:
        digit = num % 10

        if digit == 0:
            zero += 1
        elif digit % 2 == 0:
            even += 1
        else:
            odd += 1

        num //= 10

    print(f"\nThe number you entered has {odd} odd digits, {even} even digits and {zero} zero digits.")


integer = int(input("Enter a positive integer: "))

while integer < 1:
    print("Integer must be positive. Try again!\n")
    integer = int(input("Enter a positive integer: "))

count(integer)
