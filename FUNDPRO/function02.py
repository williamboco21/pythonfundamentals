def print_message(num):
    print(f"\nMessage for you!")
    count = 0

    for i in range(count, num):
        print("Have a great and blessed day!")

    print("\nThank you!")


times = int(input("Enter a number you wish: "))

while times < 1:
    print("Invalid number. Please enter a number greater than 0.\n")
    times = int(input("Enter a number you wish: "))


print_message(times)
