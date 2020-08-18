MAX = 10


def get_numbers(numbers):
    for i in range(MAX):
        num = int(input(f"Enter integer {i+1}: "))
        numbers.append(num)


def odd_numbers(numbers):
    odd = 0

    for i in numbers:
        if i % 2 != 0:
            odd += 1

    return odd


numbers = []
get_numbers(numbers)
odd = odd_numbers(numbers)

print(f"\nThere are {odd} odd numbers.\n")

print("Do you want to try again (Y/N)?")
choice = input("Enter Y for Yes and N for No: ").upper()

if choice == "N":
    print(f"\nThank you for using this program!\n"
          f"Program Terminating")
    exit()

while choice != "Y" and choice != "N":
    print("Please Enter Y or N only. Thank you!")
    choice = input("Enter Y for Yes and N for No: ").upper()

while choice == "Y":
    numbers.clear()
    print()
    get_numbers(numbers)
    odd = odd_numbers(numbers)
    print(f"\nThere are {odd} odd numbers.\n")

    print("Do you want to try again (Y/N)?")
    choice = input("Enter Y for Yes and N for No: ").upper()

    if choice == "N":
        print(f"\nThank you for using this program!\n"
              f"Program Terminating")
        exit()

    while choice != "Y" and choice != "N":
        print("Please Enter Y or N only. Thank you!")
        choice = input("Enter Y for Yes and N for No: ").upper()

    if choice == "N":
        print(f"\nThank you for using this program!\n"
              f"Program Terminating")
        exit()
