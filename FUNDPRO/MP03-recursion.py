def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        ans = fib(n-1) + fib(n-2)
        return ans


num = int(input("Enter a positive integer: "))

while num < 0:
    print("\nNumber is less than 1. Please try again!\n")
    num = int(input("Enter a positive integer: "))

result = fib(num)

print(f"The Fibonacci number is {result}.")

choice = input("\nDo you want to try again (Y/N)? ").upper()

while choice != "N" and choice != "Y":
    print("Please enter Y or N only. Thank you!\n")
    choice = input("Do you want to try again (Y/N)? ").upper()

if choice == "N":
    print("Thank you for using this program! Kampai!!!")
    exit()
else:
    while choice.upper() == 'Y':
        num = int(input("\nEnter a positive integer: "))

        while num < 0:
            print("\nNumber is less than 1. Please try again!\n")
            num = int(input("Enter a positive integer: "))

        result = fib(num)

        print(f"The Fibonacci number is {result}.")

        choice = input("\nDo you want to try again (Y/N)? ")

        while choice != "N" and choice != "Y":
            print("Please enter Y or N only. Thank you!\n")
            choice = input("Do you want to try again (Y/N)? ").upper()

        if choice.upper() == "N":
            print("Thank you for using this program! Kampai!!!")
            exit()




